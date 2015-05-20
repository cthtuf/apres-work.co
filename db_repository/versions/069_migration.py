from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_dfic_item = Table('camp_dfic_item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('icon_class', String(length=20)),
    Column('img_url', String(length=255)),
    Column('weight', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', Text),
    Column('en_text', Text),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', Text),
    Column('ru_text', Text),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', Text),
    Column('fr_text', Text),
    Column('es_header', String(length=255)),
    Column('es_subheader', Text),
    Column('es_text', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_dfic_item'].columns['img_url'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_dfic_item'].columns['img_url'].drop()
