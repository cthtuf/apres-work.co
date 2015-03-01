from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
partner_user = Table('partner_user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=20)),
    Column('email', VARCHAR(length=50)),
    Column('phone', VARCHAR(length=10)),
    Column('password', VARCHAR(length=20)),
)

staff_user = Table('staff_user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('email', String(length=50)),
    Column('phone', String(length=10)),
    Column('password', String(length=20)),
    Column('type_id', Integer),
    Column('partner_id', Integer),
)

resort = Table('resort', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('name', String(length=120)),
    Column('description', String(length=2000)),
    Column('address', String(length=255)),
    Column('phone', String(length=20)),
    Column('url_site', String(length=255)),
    Column('url_ig', String(length=255)),
    Column('url_vk', String(length=255)),
    Column('url_fb', String(length=255)),
    Column('la', Float),
    Column('lo', Float),
    Column('owm_id', Integer),
    Column('bad_wind_direction', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['partner_user'].drop()
    post_meta.tables['staff_user'].create()
    post_meta.tables['resort'].columns['description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['partner_user'].create()
    post_meta.tables['staff_user'].drop()
    post_meta.tables['resort'].columns['description'].drop()
