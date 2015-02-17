from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
SMS = Table('SMS', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('user_id', Integer),
    Column('text', String(length=560)),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('dt', DateTime),
    Column('resort_id', Integer),
    Column('name', String(length=50)),
    Column('description', String(length=1000)),
)

resort = Table('resort', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('name', String(length=120)),
    Column('url_site', String(length=255)),
    Column('url_ig', String(length=255)),
    Column('url_vk', String(length=255)),
    Column('url_fb', String(length=255)),
    Column('la', Float),
    Column('lo', Float),
)

site = Table('site', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('subdomain', String(length=20)),
)

webcameras = Table('webcameras', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('resort_id', Integer),
    Column('img_link', String(length=255)),
    Column('img_na', String(length=255)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('phone', String(length=10)),
    Column('email', String(length=120)),
    Column('ga_client_id', Integer),
)

subscription = Table('subscription', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('email', String(length=120)),
    Column('ga_client_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['SMS'].create()
    post_meta.tables['event'].create()
    post_meta.tables['resort'].create()
    post_meta.tables['site'].create()
    post_meta.tables['webcameras'].create()
    post_meta.tables['user'].columns['ga_client_id'].create()
    post_meta.tables['user'].columns['site_id'].create()
    post_meta.tables['subscription'].columns['ga_client_id'].create()
    post_meta.tables['subscription'].columns['site_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['SMS'].drop()
    post_meta.tables['event'].drop()
    post_meta.tables['resort'].drop()
    post_meta.tables['site'].drop()
    post_meta.tables['webcameras'].drop()
    post_meta.tables['user'].columns['ga_client_id'].drop()
    post_meta.tables['user'].columns['site_id'].drop()
    post_meta.tables['subscription'].columns['ga_client_id'].drop()
    post_meta.tables['subscription'].columns['site_id'].drop()
