from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
cameraman = Table('cameraman', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('location_id', Integer),
    Column('name', String(length=255)),
    Column('description', String(length=1000)),
    Column('photo', String(length=255)),
    Column('video_url', String(length=255)),
    Column('ig_profile', String(length=20)),
    Column('vk_profile', String(length=255)),
    Column('fb_profile', String(length=255)),
)

coach = Table('coach', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('location_id', Integer),
    Column('name', String(length=255)),
    Column('description', String(length=1000)),
    Column('photo', String(length=255)),
    Column('video_url', String(length=255)),
    Column('ig_hashtag', String(length=20)),
    Column('vk_link', String(length=255)),
)

news = Table('news', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('dt_news', DateTime),
    Column('resort_id', Integer),
    Column('location_id', Integer),
    Column('name', String(length=50)),
    Column('description', String(length=1000)),
    Column('poster_url', String(length=255)),
    Column('video_url', String(length=255)),
    Column('ig_hashtag', String(length=20)),
)

rider = Table('rider', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('location_id', Integer),
    Column('name', String(length=255)),
    Column('description', String(length=1000)),
    Column('photo', String(length=255)),
    Column('video_url', String(length=255)),
    Column('ig_profile', String(length=20)),
    Column('vk_profile', String(length=255)),
    Column('fb_profile', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['cameraman'].create()
    post_meta.tables['coach'].create()
    post_meta.tables['news'].create()
    post_meta.tables['rider'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['cameraman'].drop()
    post_meta.tables['coach'].drop()
    post_meta.tables['news'].drop()
    post_meta.tables['rider'].drop()
