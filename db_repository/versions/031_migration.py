from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_service_record = Table('camp_service_record', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('en_header', VARCHAR(length=255)),
    Column('en_subheader', VARCHAR(length=255)),
    Column('ru_header', VARCHAR(length=255)),
    Column('ru_subheader', VARCHAR(length=255)),
    Column('fr_header', VARCHAR(length=255)),
    Column('fr_subheader', VARCHAR(length=255)),
    Column('es_header', VARCHAR(length=255)),
    Column('es_subheader', VARCHAR(length=255)),
    Column('img_link', VARCHAR(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_service_record'].columns['en_subheader'].drop()
    pre_meta.tables['camp_service_record'].columns['es_subheader'].drop()
    pre_meta.tables['camp_service_record'].columns['fr_subheader'].drop()
    pre_meta.tables['camp_service_record'].columns['ru_subheader'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['camp_service_record'].columns['en_subheader'].create()
    pre_meta.tables['camp_service_record'].columns['es_subheader'].create()
    pre_meta.tables['camp_service_record'].columns['fr_subheader'].create()
    pre_meta.tables['camp_service_record'].columns['ru_subheader'].create()
