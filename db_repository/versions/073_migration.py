from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp = Table('camp', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
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
    Column('dt_create', DateTime),
    Column('dt', DateTime),
    Column('name', String(length=100)),
    Column('description', String(length=3000)),
    Column('url', String(length=255)),
    Column('logo_url', String(length=255)),
    Column('poster_url', String(length=255)),
    Column('seats_left', Integer),
    Column('where', String(length=255)),
    Column('is_filled', Boolean),
    Column('la', String(length=10)),
    Column('lo', String(length=10)),
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
    post_meta.tables['camp'].columns['en_share_email_body'].create()
    post_meta.tables['camp'].columns['en_share_email_subject'].create()
    post_meta.tables['camp'].columns['en_share_sms'].create()
    post_meta.tables['camp'].columns['es_share_email_body'].create()
    post_meta.tables['camp'].columns['es_share_email_subject'].create()
    post_meta.tables['camp'].columns['es_share_sms'].create()
    post_meta.tables['camp'].columns['fr_share_email_body'].create()
    post_meta.tables['camp'].columns['fr_share_email_subject'].create()
    post_meta.tables['camp'].columns['fr_share_sms'].create()
    post_meta.tables['camp'].columns['ru_share_email_body'].create()
    post_meta.tables['camp'].columns['ru_share_email_subject'].create()
    post_meta.tables['camp'].columns['ru_share_sms'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp'].columns['en_share_email_body'].drop()
    post_meta.tables['camp'].columns['en_share_email_subject'].drop()
    post_meta.tables['camp'].columns['en_share_sms'].drop()
    post_meta.tables['camp'].columns['es_share_email_body'].drop()
    post_meta.tables['camp'].columns['es_share_email_subject'].drop()
    post_meta.tables['camp'].columns['es_share_sms'].drop()
    post_meta.tables['camp'].columns['fr_share_email_body'].drop()
    post_meta.tables['camp'].columns['fr_share_email_subject'].drop()
    post_meta.tables['camp'].columns['fr_share_sms'].drop()
    post_meta.tables['camp'].columns['ru_share_email_body'].drop()
    post_meta.tables['camp'].columns['ru_share_email_subject'].drop()
    post_meta.tables['camp'].columns['ru_share_sms'].drop()
