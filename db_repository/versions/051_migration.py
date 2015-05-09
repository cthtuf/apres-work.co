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
    Column('owm_id', INTEGER),
    Column('address', VARCHAR(length=255)),
    Column('phone', VARCHAR(length=20)),
    Column('bad_wind_direction', INTEGER),
    Column('description', VARCHAR(length=2000)),
    Column('url_img', VARCHAR(length=255)),
    Column('type_id', INTEGER),
    Column('la', VARCHAR(length=10)),
    Column('lo', VARCHAR(length=10)),
    Column('share_text', VARCHAR(length=140)),
    Column('how_to_get', VARCHAR(length=3000)),
    Column('url_fb_comments', VARCHAR(length=255)),
    Column('url_vk_comments', VARCHAR(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['resort'].columns['url_vk_comments'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['resort'].columns['url_vk_comments'].create()
