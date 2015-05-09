from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_contact_block = Table('camp_contact_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('email_for_letters', String(length=255)),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('en_right_subheader', String(length=255)),
    Column('en_right_usefullpages', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('ru_right_subheader', String(length=255)),
    Column('ru_right_usefullpages', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('fr_right_subheader', String(length=255)),
    Column('fr_right_usefullpages', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
    Column('es_right_subheader', String(length=255)),
    Column('es_right_usefullpages', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_block'].columns['en_right_usefullpages'].create()
    post_meta.tables['camp_contact_block'].columns['es_right_usefullpages'].create()
    post_meta.tables['camp_contact_block'].columns['fr_right_usefullpages'].create()
    post_meta.tables['camp_contact_block'].columns['ru_right_usefullpages'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_block'].columns['en_right_usefullpages'].drop()
    post_meta.tables['camp_contact_block'].columns['es_right_usefullpages'].drop()
    post_meta.tables['camp_contact_block'].columns['fr_right_usefullpages'].drop()
    post_meta.tables['camp_contact_block'].columns['ru_right_usefullpages'].drop()
