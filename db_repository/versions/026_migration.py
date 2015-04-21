from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
location = Table('location', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('suffix', String(length=10)),
    Column('name', String(length=20)),
    Column('description', String(length=200)),
    Column('resorts_header', String(length=100)),
    Column('resorts_subheader', String(length=500)),
    Column('la', String(length=10)),
    Column('lo', String(length=10)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['location'].columns['la'].create()
    post_meta.tables['location'].columns['lo'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['location'].columns['la'].drop()
    post_meta.tables['location'].columns['lo'].drop()
