from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
webcamera = Table('webcamera', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('resort_id', Integer),
    Column('img_link', String(length=255)),
    Column('iframe_link', String(length=255)),
    Column('img_na', String(length=255)),
    Column('load_from_img', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['webcamera'].columns['iframe_link'].create()
    post_meta.tables['webcamera'].columns['load_from_img'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['webcamera'].columns['iframe_link'].drop()
    post_meta.tables['webcamera'].columns['load_from_img'].drop()
