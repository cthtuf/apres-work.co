from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
webcamera = Table('webcamera', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('location_id', INTEGER),
    Column('resort_id', INTEGER),
    Column('img_link', VARCHAR(length=255)),
    Column('img_na', VARCHAR(length=255)),
    Column('name', VARCHAR(length=50)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['webcamera'].columns['location_id'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['webcamera'].columns['location_id'].create()
