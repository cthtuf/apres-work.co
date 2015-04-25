from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp = Table('camp', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_create', DateTime),
    Column('dt', DateTime),
    Column('name', String(length=100)),
    Column('description', String(length=3000)),
    Column('url', String(length=255)),
    Column('logo_url', String(length=255)),
    Column('poster_url', String(length=255)),
    Column('is_filled', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp'].drop()
