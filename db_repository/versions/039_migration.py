from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_top_slider_record = Table('camp_top_slider_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('index', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
    Column('img_url_desktop', String(length=255)),
    Column('img_url_mobile', String(length=255)),
    Column('img_url_vertical', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_top_slider_record'].columns['img_url_desktop'].create()
    post_meta.tables['camp_top_slider_record'].columns['img_url_mobile'].create()
    post_meta.tables['camp_top_slider_record'].columns['img_url_vertical'].create()
    post_meta.tables['camp_top_slider_record'].columns['index'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_top_slider_record'].columns['img_url_desktop'].drop()
    post_meta.tables['camp_top_slider_record'].columns['img_url_mobile'].drop()
    post_meta.tables['camp_top_slider_record'].columns['img_url_vertical'].drop()
    post_meta.tables['camp_top_slider_record'].columns['index'].drop()
