from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_contact_useful_page = Table('camp_contact_useful_page', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_link', String(length=255)),
    Column('ru_link', String(length=255)),
    Column('fr_link', String(length=255)),
    Column('es_link', String(length=255)),
    Column('icon_class', String(length=20)),
    Column('in_new_window', Boolean),
    Column('en_caption', String(length=1000)),
    Column('ru_caption', String(length=1000)),
    Column('fr_caption', String(length=1000)),
    Column('es_caption', String(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_useful_page'].columns['es_link'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_useful_page'].columns['es_link'].drop()
