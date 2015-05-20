from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_htgu_page = Table('camp_htgu_page', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', Text),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', Text),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', Text),
    Column('es_header', String(length=255)),
    Column('es_subheader', Text),
    Column('en_share_email_subject', String(length=255)),
    Column('en_share_email_body', Text),
    Column('en_share_sms', Text),
    Column('ru_share_email_subject', String(length=255)),
    Column('ru_share_email_body', Text),
    Column('ru_share_sms', Text),
    Column('fr_share_email_subject', String(length=255)),
    Column('fr_share_email_body', Text),
    Column('fr_share_sms', Text),
    Column('es_share_email_subject', String(length=255)),
    Column('es_share_email_body', Text),
    Column('es_share_sms', Text),
)

camp_htgu_route = Table('camp_htgu_route', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('icon_class', String(length=20)),
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

camp_htgu_routes = Table('camp_htgu_routes', post_meta,
    Column('htgu_page_id', Integer),
    Column('route_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_htgu_page'].create()
    post_meta.tables['camp_htgu_route'].create()
    post_meta.tables['camp_htgu_routes'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_htgu_page'].drop()
    post_meta.tables['camp_htgu_route'].drop()
    post_meta.tables['camp_htgu_routes'].drop()
