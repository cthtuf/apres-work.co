from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_contact_record = Table('camp_contact_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('icon_class', String(length=20)),
    Column('link', String(length=255)),
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
    post_meta.tables['camp_contact_record'].columns['in_new_window'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_record'].columns['in_new_window'].drop()
