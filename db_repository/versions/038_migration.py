from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_partner_record = Table('camp_partner_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_name', String(length=100)),
    Column('ru_name', String(length=100)),
    Column('fr_name', String(length=100)),
    Column('es_name', String(length=100)),
    Column('en_description', String(length=3000)),
    Column('ru_description', String(length=3000)),
    Column('fr_description', String(length=3000)),
    Column('es_description', String(length=3000)),
    Column('url', String(length=255)),
    Column('img_link', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_partner_record'].columns['en_description'].create()
    post_meta.tables['camp_partner_record'].columns['es_description'].create()
    post_meta.tables['camp_partner_record'].columns['fr_description'].create()
    post_meta.tables['camp_partner_record'].columns['ru_description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_partner_record'].columns['en_description'].drop()
    post_meta.tables['camp_partner_record'].columns['es_description'].drop()
    post_meta.tables['camp_partner_record'].columns['fr_description'].drop()
    post_meta.tables['camp_partner_record'].columns['ru_description'].drop()
