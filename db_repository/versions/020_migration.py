from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
resort = Table('resort', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('location_id', INTEGER),
    Column('name', VARCHAR(length=120)),
    Column('url_site', VARCHAR(length=255)),
    Column('url_ig', VARCHAR(length=255)),
    Column('url_vk', VARCHAR(length=255)),
    Column('url_fb', VARCHAR(length=255)),
    Column('la', FLOAT),
    Column('lo', FLOAT),
    Column('owm_id', INTEGER),
    Column('address', VARCHAR(length=255)),
    Column('phone', VARCHAR(length=20)),
    Column('bad_wind_direction', INTEGER),
    Column('description', VARCHAR(length=2000)),
    Column('url_img', VARCHAR(length=255)),
    Column('type_id', INTEGER),
)

resort = Table('resort', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('type_id', Integer),
    Column('location_id', Integer),
    Column('name', String(length=120)),
    Column('description', String(length=2000)),
    Column('address', String(length=255)),
    Column('phone', String(length=20)),
    Column('url_site', String(length=255)),
    Column('url_ig', String(length=255)),
    Column('url_vk', String(length=255)),
    Column('url_fb', String(length=255)),
    Column('url_img', String(length=255)),
    Column('la_n', String(length=10)),
    Column('lo_n', String(length=10)),
    Column('owm_id', Integer),
    Column('bad_wind_direction', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['resort'].columns['la'].drop()
    pre_meta.tables['resort'].columns['lo'].drop()
    post_meta.tables['resort'].columns['la_n'].create()
    post_meta.tables['resort'].columns['lo_n'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['resort'].columns['la'].create()
    pre_meta.tables['resort'].columns['lo'].create()
    post_meta.tables['resort'].columns['la_n'].drop()
    post_meta.tables['resort'].columns['lo_n'].drop()
