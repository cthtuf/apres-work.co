from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_main_info_block = Table('camp_main_info_block', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('camp_id', INTEGER),
    Column('en_header', VARCHAR(length=255)),
    Column('en_subheader', VARCHAR(length=255)),
    Column('ru_header', VARCHAR(length=255)),
    Column('ru_subheader', VARCHAR(length=255)),
    Column('fr_header', VARCHAR(length=255)),
    Column('fr_subheader', VARCHAR(length=255)),
    Column('es_header', VARCHAR(length=255)),
    Column('es_subheader', VARCHAR(length=255)),
    Column('en_top_text', VARCHAR(length=1000)),
    Column('en_hidden_text', VARCHAR(length=1000)),
    Column('en_bottom_text', VARCHAR(length=1000)),
    Column('ru_top_text', VARCHAR(length=1000)),
    Column('ru_hidden_text', VARCHAR(length=1000)),
    Column('ru_bottom_text', VARCHAR(length=1000)),
    Column('fr_top_text', VARCHAR(length=1000)),
    Column('fr_hidden_text', VARCHAR(length=1000)),
    Column('fr_bottom_text', VARCHAR(length=1000)),
    Column('es_top_text', VARCHAR(length=1000)),
    Column('es_hidden_text', VARCHAR(length=1000)),
    Column('es_bottom_text', VARCHAR(length=1000)),
    Column('en_text_header', VARCHAR(length=255)),
    Column('en_text_subheader', VARCHAR(length=255)),
    Column('es_text_header', VARCHAR(length=255)),
    Column('es_text_subheader', VARCHAR(length=255)),
    Column('fr_text_header', VARCHAR(length=255)),
    Column('fr_text_subheader', VARCHAR(length=255)),
    Column('ru_text_header', VARCHAR(length=255)),
    Column('ru_text_subheader', VARCHAR(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_main_info_block'].columns['en_hidden_text'].drop()
    pre_meta.tables['camp_main_info_block'].columns['es_hidden_text'].drop()
    pre_meta.tables['camp_main_info_block'].columns['fr_hidden_text'].drop()
    pre_meta.tables['camp_main_info_block'].columns['ru_hidden_text'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_main_info_block'].columns['en_hidden_text'].create()
    pre_meta.tables['camp_main_info_block'].columns['es_hidden_text'].create()
    pre_meta.tables['camp_main_info_block'].columns['fr_hidden_text'].create()
    pre_meta.tables['camp_main_info_block'].columns['ru_hidden_text'].create()
