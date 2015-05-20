from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_dfic_item = Table('camp_dfic_item', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('icon_class', String(length=20)),
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

camp_dfic_items = Table('camp_dfic_items', post_meta,
    Column('page_id', Integer),
    Column('item_id', Integer),
)

camp_dfic_page = Table('camp_dfic_page', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', Text),
    Column('en_subheader', Text),
    Column('en_top_text', Text),
    Column('en_bottom_text', Text),
    Column('ru_header', Text),
    Column('ru_subheader', Text),
    Column('ru_top_text', Text),
    Column('ru_bottom_text', Text),
    Column('fr_header', Text),
    Column('fr_subheader', Text),
    Column('fr_top_text', Text),
    Column('fr_bottom_text', Text),
    Column('es_header', Text),
    Column('es_subheader', Text),
    Column('es_top_text', Text),
    Column('es_bottom_text', Text),
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

camp_visa_page = Table('camp_visa_page', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', Text),
    Column('en_subheader', Text),
    Column('en_text', Text),
    Column('ru_header', Text),
    Column('ru_subheader', Text),
    Column('ru_text', Text),
    Column('fr_header', Text),
    Column('fr_subheader', Text),
    Column('fr_text', Text),
    Column('es_header', Text),
    Column('es_subheader', Text),
    Column('es_text', Text),
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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_dfic_item'].create()
    post_meta.tables['camp_dfic_items'].create()
    post_meta.tables['camp_dfic_page'].create()
    post_meta.tables['camp_visa_page'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_dfic_item'].drop()
    post_meta.tables['camp_dfic_items'].drop()
    post_meta.tables['camp_dfic_page'].drop()
    post_meta.tables['camp_visa_page'].drop()
