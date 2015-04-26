from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_partner_record = Table('camp_partner_record', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('order_index', INTEGER),
    Column('en_description', VARCHAR(length=1000)),
    Column('ru_description', VARCHAR(length=1000)),
    Column('fr_description', VARCHAR(length=1000)),
    Column('es_description', VARCHAR(length=1000)),
    Column('url', VARCHAR(length=255)),
    Column('img_link', VARCHAR(length=255)),
)

camp_partner_record = Table('camp_partner_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_name', String(length=100)),
    Column('ru_name', String(length=100)),
    Column('fr_name', String(length=100)),
    Column('es_name', String(length=100)),
    Column('url', String(length=255)),
    Column('img_link', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_partner_record'].columns['en_description'].drop()
    pre_meta.tables['camp_partner_record'].columns['es_description'].drop()
    pre_meta.tables['camp_partner_record'].columns['fr_description'].drop()
    pre_meta.tables['camp_partner_record'].columns['ru_description'].drop()
    post_meta.tables['camp_partner_record'].columns['en_name'].create()
    post_meta.tables['camp_partner_record'].columns['es_name'].create()
    post_meta.tables['camp_partner_record'].columns['fr_name'].create()
    post_meta.tables['camp_partner_record'].columns['ru_name'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_partner_record'].columns['en_description'].create()
    pre_meta.tables['camp_partner_record'].columns['es_description'].create()
    pre_meta.tables['camp_partner_record'].columns['fr_description'].create()
    pre_meta.tables['camp_partner_record'].columns['ru_description'].create()
    post_meta.tables['camp_partner_record'].columns['en_name'].drop()
    post_meta.tables['camp_partner_record'].columns['es_name'].drop()
    post_meta.tables['camp_partner_record'].columns['fr_name'].drop()
    post_meta.tables['camp_partner_record'].columns['ru_name'].drop()
