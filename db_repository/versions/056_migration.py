from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_contact_useful_page = Table('camp_contact_useful_page', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('order_index', INTEGER),
    Column('icon_class', VARCHAR(length=20)),
    Column('link', VARCHAR(length=255)),
    Column('in_new_window', BOOLEAN),
    Column('en_caption', VARCHAR(length=1000)),
    Column('ru_caption', VARCHAR(length=1000)),
    Column('fr_caption', VARCHAR(length=1000)),
    Column('es_caption', VARCHAR(length=1000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_contact_useful_page'].columns['link'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_contact_useful_page'].columns['link'].create()
