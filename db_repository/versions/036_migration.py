from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_main_info_block_photo = Table('camp_main_info_block_photo', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('order_index', INTEGER),
    Column('en_alt', VARCHAR(length=255)),
    Column('ru_alt', VARCHAR(length=255)),
    Column('fr_alt', VARCHAR(length=255)),
    Column('es_alt', VARCHAR(length=255)),
    Column('img_link', VARCHAR(length=255)),
)

camp_main_info_block_photo = Table('camp_main_info_block_photo', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_alt', String(length=255)),
    Column('ru_alt', String(length=255)),
    Column('fr_alt', String(length=255)),
    Column('es_alt', String(length=255)),
    Column('img_link_desktop', String(length=255)),
    Column('img_link_mobile', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_main_info_block_photo'].columns['img_link'].drop()
    post_meta.tables['camp_main_info_block_photo'].columns['img_link_desktop'].create()
    post_meta.tables['camp_main_info_block_photo'].columns['img_link_mobile'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_main_info_block_photo'].columns['img_link'].create()
    post_meta.tables['camp_main_info_block_photo'].columns['img_link_desktop'].drop()
    post_meta.tables['camp_main_info_block_photo'].columns['img_link_mobile'].drop()
