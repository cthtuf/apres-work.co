from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
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
    Column('la', String(length=10)),
    Column('lo', String(length=10)),
    Column('owm_id', Integer),
    Column('bad_wind_direction', Integer),
    Column('share_text', String(length=140)),
    Column('how_to_get', String(length=3000)),
    Column('url_fb_comments', String(length=255)),
    Column('url_vk_comments', String(length=255)),
)

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
    Column('url_fb_comments', String(length=255)),
    Column('url_vk_comments', String(length=255)),
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
    Column('url_fb_comments', String(length=255)),
    Column('url_vk_comments', String(length=255)),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('dt_event', DateTime),
    Column('resort_id', Integer),
    Column('name', String(length=50)),
    Column('description', String(length=1000)),
    Column('poster_url', String(length=255)),
    Column('video_url', String(length=255)),
    Column('ig_hashtag', String(length=20)),
    Column('vk_event_url', String(length=255)),
    Column('url_fb_comments', String(length=255)),
    Column('url_vk_comments', String(length=255)),
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
    Column('url_fb_comments', String(length=255)),
    Column('url_vk_comments', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['resort'].columns['url_fb_comments'].create()
    post_meta.tables['resort'].columns['url_vk_comments'].create()
    post_meta.tables['cameraman'].columns['url_fb_comments'].create()
    post_meta.tables['cameraman'].columns['url_vk_comments'].create()
    post_meta.tables['coach'].columns['url_fb_comments'].create()
    post_meta.tables['coach'].columns['url_vk_comments'].create()
    post_meta.tables['event'].columns['url_fb_comments'].create()
    post_meta.tables['event'].columns['url_vk_comments'].create()
    post_meta.tables['news'].columns['url_fb_comments'].create()
    post_meta.tables['news'].columns['url_vk_comments'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['resort'].columns['url_fb_comments'].drop()
    post_meta.tables['resort'].columns['url_vk_comments'].drop()
    post_meta.tables['cameraman'].columns['url_fb_comments'].drop()
    post_meta.tables['cameraman'].columns['url_vk_comments'].drop()
    post_meta.tables['coach'].columns['url_fb_comments'].drop()
    post_meta.tables['coach'].columns['url_vk_comments'].drop()
    post_meta.tables['event'].columns['url_fb_comments'].drop()
    post_meta.tables['event'].columns['url_vk_comments'].drop()
    post_meta.tables['news'].columns['url_fb_comments'].drop()
    post_meta.tables['news'].columns['url_vk_comments'].drop()
