from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
event = Table('event', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('resort_id', INTEGER),
    Column('name', VARCHAR(length=50)),
    Column('description', VARCHAR(length=1000)),
    Column('dt_created', DATETIME),
    Column('img_link', VARCHAR(length=255)),
    Column('dt_event', DATETIME),
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
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['img_link'].drop()
    post_meta.tables['event'].columns['ig_hashtag'].create()
    post_meta.tables['event'].columns['poster_url'].create()
    post_meta.tables['event'].columns['video_url'].create()
    post_meta.tables['event'].columns['vk_event_url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['img_link'].create()
    post_meta.tables['event'].columns['ig_hashtag'].drop()
    post_meta.tables['event'].columns['poster_url'].drop()
    post_meta.tables['event'].columns['video_url'].drop()
    post_meta.tables['event'].columns['vk_event_url'].drop()
