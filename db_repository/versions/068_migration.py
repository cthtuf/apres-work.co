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
)

camp_dfic_page = Table('camp_dfic_page', post_meta,
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

camp_htgu_page = Table('camp_htgu_page', post_meta,
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

camp_insurance_page = Table('camp_insurance_page', post_meta,
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
    post_meta.tables['camp'].columns['en_image_url'].create()
    post_meta.tables['camp'].columns['en_page_description'].create()
    post_meta.tables['camp'].columns['en_page_title'].create()
    post_meta.tables['camp'].columns['es_image_url'].create()
    post_meta.tables['camp'].columns['es_page_description'].create()
    post_meta.tables['camp'].columns['es_page_title'].create()
    post_meta.tables['camp'].columns['fr_image_url'].create()
    post_meta.tables['camp'].columns['fr_page_description'].create()
    post_meta.tables['camp'].columns['fr_page_title'].create()
    post_meta.tables['camp'].columns['ru_image_url'].create()
    post_meta.tables['camp'].columns['ru_page_description'].create()
    post_meta.tables['camp'].columns['ru_page_title'].create()
    post_meta.tables['camp_dfic_page'].columns['en_image_url'].create()
    post_meta.tables['camp_dfic_page'].columns['en_page_description'].create()
    post_meta.tables['camp_dfic_page'].columns['en_page_title'].create()
    post_meta.tables['camp_dfic_page'].columns['es_image_url'].create()
    post_meta.tables['camp_dfic_page'].columns['es_page_description'].create()
    post_meta.tables['camp_dfic_page'].columns['es_page_title'].create()
    post_meta.tables['camp_dfic_page'].columns['fr_image_url'].create()
    post_meta.tables['camp_dfic_page'].columns['fr_page_description'].create()
    post_meta.tables['camp_dfic_page'].columns['fr_page_title'].create()
    post_meta.tables['camp_dfic_page'].columns['ru_image_url'].create()
    post_meta.tables['camp_dfic_page'].columns['ru_page_description'].create()
    post_meta.tables['camp_dfic_page'].columns['ru_page_title'].create()
    post_meta.tables['camp_visa_page'].columns['en_image_url'].create()
    post_meta.tables['camp_visa_page'].columns['en_page_description'].create()
    post_meta.tables['camp_visa_page'].columns['en_page_title'].create()
    post_meta.tables['camp_visa_page'].columns['es_image_url'].create()
    post_meta.tables['camp_visa_page'].columns['es_page_description'].create()
    post_meta.tables['camp_visa_page'].columns['es_page_title'].create()
    post_meta.tables['camp_visa_page'].columns['fr_image_url'].create()
    post_meta.tables['camp_visa_page'].columns['fr_page_description'].create()
    post_meta.tables['camp_visa_page'].columns['fr_page_title'].create()
    post_meta.tables['camp_visa_page'].columns['ru_image_url'].create()
    post_meta.tables['camp_visa_page'].columns['ru_page_description'].create()
    post_meta.tables['camp_visa_page'].columns['ru_page_title'].create()
    post_meta.tables['camp_htgu_page'].columns['en_image_url'].create()
    post_meta.tables['camp_htgu_page'].columns['en_page_description'].create()
    post_meta.tables['camp_htgu_page'].columns['en_page_title'].create()
    post_meta.tables['camp_htgu_page'].columns['es_image_url'].create()
    post_meta.tables['camp_htgu_page'].columns['es_page_description'].create()
    post_meta.tables['camp_htgu_page'].columns['es_page_title'].create()
    post_meta.tables['camp_htgu_page'].columns['fr_image_url'].create()
    post_meta.tables['camp_htgu_page'].columns['fr_page_description'].create()
    post_meta.tables['camp_htgu_page'].columns['fr_page_title'].create()
    post_meta.tables['camp_htgu_page'].columns['ru_image_url'].create()
    post_meta.tables['camp_htgu_page'].columns['ru_page_description'].create()
    post_meta.tables['camp_htgu_page'].columns['ru_page_title'].create()
    post_meta.tables['camp_insurance_page'].columns['en_image_url'].create()
    post_meta.tables['camp_insurance_page'].columns['en_page_description'].create()
    post_meta.tables['camp_insurance_page'].columns['en_page_title'].create()
    post_meta.tables['camp_insurance_page'].columns['es_image_url'].create()
    post_meta.tables['camp_insurance_page'].columns['es_page_description'].create()
    post_meta.tables['camp_insurance_page'].columns['es_page_title'].create()
    post_meta.tables['camp_insurance_page'].columns['fr_image_url'].create()
    post_meta.tables['camp_insurance_page'].columns['fr_page_description'].create()
    post_meta.tables['camp_insurance_page'].columns['fr_page_title'].create()
    post_meta.tables['camp_insurance_page'].columns['ru_image_url'].create()
    post_meta.tables['camp_insurance_page'].columns['ru_page_description'].create()
    post_meta.tables['camp_insurance_page'].columns['ru_page_title'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp'].columns['en_image_url'].drop()
    post_meta.tables['camp'].columns['en_page_description'].drop()
    post_meta.tables['camp'].columns['en_page_title'].drop()
    post_meta.tables['camp'].columns['es_image_url'].drop()
    post_meta.tables['camp'].columns['es_page_description'].drop()
    post_meta.tables['camp'].columns['es_page_title'].drop()
    post_meta.tables['camp'].columns['fr_image_url'].drop()
    post_meta.tables['camp'].columns['fr_page_description'].drop()
    post_meta.tables['camp'].columns['fr_page_title'].drop()
    post_meta.tables['camp'].columns['ru_image_url'].drop()
    post_meta.tables['camp'].columns['ru_page_description'].drop()
    post_meta.tables['camp'].columns['ru_page_title'].drop()
    post_meta.tables['camp_dfic_page'].columns['en_image_url'].drop()
    post_meta.tables['camp_dfic_page'].columns['en_page_description'].drop()
    post_meta.tables['camp_dfic_page'].columns['en_page_title'].drop()
    post_meta.tables['camp_dfic_page'].columns['es_image_url'].drop()
    post_meta.tables['camp_dfic_page'].columns['es_page_description'].drop()
    post_meta.tables['camp_dfic_page'].columns['es_page_title'].drop()
    post_meta.tables['camp_dfic_page'].columns['fr_image_url'].drop()
    post_meta.tables['camp_dfic_page'].columns['fr_page_description'].drop()
    post_meta.tables['camp_dfic_page'].columns['fr_page_title'].drop()
    post_meta.tables['camp_dfic_page'].columns['ru_image_url'].drop()
    post_meta.tables['camp_dfic_page'].columns['ru_page_description'].drop()
    post_meta.tables['camp_dfic_page'].columns['ru_page_title'].drop()
    post_meta.tables['camp_visa_page'].columns['en_image_url'].drop()
    post_meta.tables['camp_visa_page'].columns['en_page_description'].drop()
    post_meta.tables['camp_visa_page'].columns['en_page_title'].drop()
    post_meta.tables['camp_visa_page'].columns['es_image_url'].drop()
    post_meta.tables['camp_visa_page'].columns['es_page_description'].drop()
    post_meta.tables['camp_visa_page'].columns['es_page_title'].drop()
    post_meta.tables['camp_visa_page'].columns['fr_image_url'].drop()
    post_meta.tables['camp_visa_page'].columns['fr_page_description'].drop()
    post_meta.tables['camp_visa_page'].columns['fr_page_title'].drop()
    post_meta.tables['camp_visa_page'].columns['ru_image_url'].drop()
    post_meta.tables['camp_visa_page'].columns['ru_page_description'].drop()
    post_meta.tables['camp_visa_page'].columns['ru_page_title'].drop()
    post_meta.tables['camp_htgu_page'].columns['en_image_url'].drop()
    post_meta.tables['camp_htgu_page'].columns['en_page_description'].drop()
    post_meta.tables['camp_htgu_page'].columns['en_page_title'].drop()
    post_meta.tables['camp_htgu_page'].columns['es_image_url'].drop()
    post_meta.tables['camp_htgu_page'].columns['es_page_description'].drop()
    post_meta.tables['camp_htgu_page'].columns['es_page_title'].drop()
    post_meta.tables['camp_htgu_page'].columns['fr_image_url'].drop()
    post_meta.tables['camp_htgu_page'].columns['fr_page_description'].drop()
    post_meta.tables['camp_htgu_page'].columns['fr_page_title'].drop()
    post_meta.tables['camp_htgu_page'].columns['ru_image_url'].drop()
    post_meta.tables['camp_htgu_page'].columns['ru_page_description'].drop()
    post_meta.tables['camp_htgu_page'].columns['ru_page_title'].drop()
    post_meta.tables['camp_insurance_page'].columns['en_image_url'].drop()
    post_meta.tables['camp_insurance_page'].columns['en_page_description'].drop()
    post_meta.tables['camp_insurance_page'].columns['en_page_title'].drop()
    post_meta.tables['camp_insurance_page'].columns['es_image_url'].drop()
    post_meta.tables['camp_insurance_page'].columns['es_page_description'].drop()
    post_meta.tables['camp_insurance_page'].columns['es_page_title'].drop()
    post_meta.tables['camp_insurance_page'].columns['fr_image_url'].drop()
    post_meta.tables['camp_insurance_page'].columns['fr_page_description'].drop()
    post_meta.tables['camp_insurance_page'].columns['fr_page_title'].drop()
    post_meta.tables['camp_insurance_page'].columns['ru_image_url'].drop()
    post_meta.tables['camp_insurance_page'].columns['ru_page_description'].drop()
    post_meta.tables['camp_insurance_page'].columns['ru_page_title'].drop()
