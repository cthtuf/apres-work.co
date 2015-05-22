from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_calendar_page = Table('camp_calendar_page', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('is_published', Boolean),
    Column('en_page_title', String(length=255)),
    Column('en_page_description', Text),
    Column('en_image_url', String(length=255)),
    Column('ru_page_title', String(length=255)),
    Column('ru_page_description', Text),
    Column('ru_image_url', String(length=255)),
    Column('fr_page_title', String(length=255)),
    Column('fr_page_description', Text),
    Column('fr_image_url', String(length=255)),
    Column('es_page_title', String(length=255)),
    Column('es_page_description', Text),
    Column('es_image_url', String(length=255)),
    Column('en_header', Text),
    Column('en_subheader', Text),
    Column('ru_header', Text),
    Column('ru_subheader', Text),
    Column('fr_header', Text),
    Column('fr_subheader', Text),
    Column('es_header', Text),
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

camp_calendar_record = Table('camp_calendar_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('calendar_id', Integer),
    Column('order_index', Integer),
    Column('record_class', String(length=50)),
    Column('time_from', String(length=20)),
    Column('time_to', String(length=20)),
    Column('day_of_month', Integer),
    Column('en_header', Text),
    Column('en_subheader', Text),
    Column('ru_header', Text),
    Column('ru_subheader', Text),
    Column('fr_header', Text),
    Column('fr_subheader', Text),
    Column('es_header', Text),
    Column('es_subheader', Text),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_calendar_page'].create()
    post_meta.tables['camp_calendar_record'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_calendar_page'].drop()
    post_meta.tables['camp_calendar_record'].drop()
