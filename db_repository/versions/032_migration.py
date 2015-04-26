from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_service_record = Table('camp_service_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=2000)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=2000)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=2000)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=2000)),
    Column('img_link', String(length=255)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_service_record'].columns['en_subheader'].create()
    post_meta.tables['camp_service_record'].columns['es_subheader'].create()
    post_meta.tables['camp_service_record'].columns['fr_subheader'].create()
    post_meta.tables['camp_service_record'].columns['ru_subheader'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_service_record'].columns['en_subheader'].drop()
    post_meta.tables['camp_service_record'].columns['es_subheader'].drop()
    post_meta.tables['camp_service_record'].columns['fr_subheader'].drop()
    post_meta.tables['camp_service_record'].columns['ru_subheader'].drop()
