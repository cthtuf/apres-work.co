from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_main_info_block = Table('camp_main_info_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
    Column('en_text_header', String(length=255)),
    Column('en_text_subheader', String(length=255)),
    Column('ru_text_header', String(length=255)),
    Column('ru_text_subheader', String(length=255)),
    Column('fr_text_header', String(length=255)),
    Column('fr_text_subheader', String(length=255)),
    Column('es_text_header', String(length=255)),
    Column('es_text_subheader', String(length=255)),
    Column('en_top_text', String(length=1000)),
    Column('en_hidden_text', String(length=1000)),
    Column('en_bottom_text', String(length=1000)),
    Column('ru_top_text', String(length=1000)),
    Column('ru_hidden_text', String(length=1000)),
    Column('ru_bottom_text', String(length=1000)),
    Column('fr_top_text', String(length=1000)),
    Column('fr_hidden_text', String(length=1000)),
    Column('fr_bottom_text', String(length=1000)),
    Column('es_top_text', String(length=1000)),
    Column('es_hidden_text', String(length=1000)),
    Column('es_bottom_text', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_main_info_block'].columns['en_text_header'].create()
    post_meta.tables['camp_main_info_block'].columns['en_text_subheader'].create()
    post_meta.tables['camp_main_info_block'].columns['es_text_header'].create()
    post_meta.tables['camp_main_info_block'].columns['es_text_subheader'].create()
    post_meta.tables['camp_main_info_block'].columns['fr_text_header'].create()
    post_meta.tables['camp_main_info_block'].columns['fr_text_subheader'].create()
    post_meta.tables['camp_main_info_block'].columns['ru_text_header'].create()
    post_meta.tables['camp_main_info_block'].columns['ru_text_subheader'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_main_info_block'].columns['en_text_header'].drop()
    post_meta.tables['camp_main_info_block'].columns['en_text_subheader'].drop()
    post_meta.tables['camp_main_info_block'].columns['es_text_header'].drop()
    post_meta.tables['camp_main_info_block'].columns['es_text_subheader'].drop()
    post_meta.tables['camp_main_info_block'].columns['fr_text_header'].drop()
    post_meta.tables['camp_main_info_block'].columns['fr_text_subheader'].drop()
    post_meta.tables['camp_main_info_block'].columns['ru_text_header'].drop()
    post_meta.tables['camp_main_info_block'].columns['ru_text_subheader'].drop()
