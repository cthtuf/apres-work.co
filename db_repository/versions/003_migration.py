from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
webcameras = Table('webcameras', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('site_id', INTEGER),
    Column('resort_id', INTEGER),
    Column('img_link', VARCHAR(length=255)),
    Column('img_na', VARCHAR(length=255)),
)

webcamera = Table('webcamera', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('resort_id', Integer),
    Column('img_link', String(length=255)),
    Column('img_na', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['webcameras'].drop()
    post_meta.tables['webcamera'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['webcameras'].create()
    post_meta.tables['webcamera'].drop()
