from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
resort = Table('resort', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('name', String(length=120)),
    Column('address', String(length=255)),
    Column('phone', String(length=20)),
    Column('url_site', String(length=255)),
    Column('url_ig', String(length=255)),
    Column('url_vk', String(length=255)),
    Column('url_fb', String(length=255)),
    Column('la', Float),
    Column('lo', Float),
    Column('owm_id', Integer),
)

event = Table('event', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('location_id', INTEGER),
    Column('dt', DATETIME),
    Column('resort_id', INTEGER),
    Column('name', VARCHAR(length=50)),
    Column('description', VARCHAR(length=1000)),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('dt_from', DateTime),
    Column('dt_to', DateTime),
    Column('resort_id', Integer),
    Column('name', String(length=50)),
    Column('description', String(length=1000)),
    Column('img_link', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['resort'].columns['address'].create()
    post_meta.tables['resort'].columns['phone'].create()
    pre_meta.tables['event'].columns['dt'].drop()
    pre_meta.tables['event'].columns['location_id'].drop()
    post_meta.tables['event'].columns['dt_created'].create()
    post_meta.tables['event'].columns['dt_from'].create()
    post_meta.tables['event'].columns['dt_to'].create()
    post_meta.tables['event'].columns['img_link'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['resort'].columns['address'].drop()
    post_meta.tables['resort'].columns['phone'].drop()
    pre_meta.tables['event'].columns['dt'].create()
    pre_meta.tables['event'].columns['location_id'].create()
    post_meta.tables['event'].columns['dt_created'].drop()
    post_meta.tables['event'].columns['dt_from'].drop()
    post_meta.tables['event'].columns['dt_to'].drop()
    post_meta.tables['event'].columns['img_link'].drop()
