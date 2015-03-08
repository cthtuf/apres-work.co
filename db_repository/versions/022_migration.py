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
    Column('dt_from', DATETIME),
    Column('dt_to', DATETIME),
    Column('img_link', VARCHAR(length=255)),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_created', DateTime),
    Column('dt_event', DateTime),
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
    pre_meta.tables['event'].columns['dt_from'].drop()
    pre_meta.tables['event'].columns['dt_to'].drop()
    post_meta.tables['event'].columns['dt_event'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['event'].columns['dt_from'].create()
    pre_meta.tables['event'].columns['dt_to'].create()
    post_meta.tables['event'].columns['dt_event'].drop()
