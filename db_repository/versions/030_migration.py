from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_contact_block = Table('camp_contact_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('email_for_letters', String(length=255)),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
)

camp_contact_record = Table('camp_contact_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('icon_class', String(length=20)),
    Column('link', String(length=255)),
    Column('en_caption', String(length=1000)),
    Column('ru_caption', String(length=1000)),
    Column('fr_caption', String(length=1000)),
    Column('es_caption', String(length=1000)),
)

camp_contact_records = Table('camp_contact_records', post_meta,
    Column('block_id', Integer),
    Column('contact_id', Integer),
)

camp_main_info_block = Table('camp_main_info_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
    Column('en_top_text', String(length=1000)),
    Column('en_hidden_text', String(length=1000)),
    Column('en_bottom_text', String(length=1000)),
    Column('ru_top_text', String(length=1000)),
    Column('ru_hidden_text', String(length=1000)),
    Column('ru_bottom_text', String(length=1000)),
    Column('fr_top_text', String(length=1000)),
    Column('fr_hidden_text', String(length=1000)),
    Column('fr_bottom_text', String(length=1000)),
    Column('es_top_text', String(length=1000)),
    Column('es_hidden_text', String(length=1000)),
    Column('es_bottom_text', String(length=1000)),
)

camp_main_info_block_photo = Table('camp_main_info_block_photo', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_alt', String(length=255)),
    Column('ru_alt', String(length=255)),
    Column('fr_alt', String(length=255)),
    Column('es_alt', String(length=255)),
    Column('img_link', String(length=255)),
)

camp_main_info_block_photos = Table('camp_main_info_block_photos', post_meta,
    Column('block_id', Integer),
    Column('photo_id', Integer),
)

camp_partner_record = Table('camp_partner_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_description', String(length=1000)),
    Column('ru_description', String(length=1000)),
    Column('fr_description', String(length=1000)),
    Column('es_description', String(length=1000)),
    Column('url', String(length=255)),
    Column('img_link', String(length=255)),
)

camp_partners_block = Table('camp_partners_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
)

camp_partners_records = Table('camp_partners_records', post_meta,
    Column('block_id', Integer),
    Column('partner_id', Integer),
)

camp_service_record = Table('camp_service_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
    Column('img_link', String(length=255)),
)

camp_services_block = Table('camp_services_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
)

camp_services_records = Table('camp_services_records', post_meta,
    Column('services_block_id', Integer),
    Column('service_record_id', Integer),
)

camp_sign_up_block = Table('camp_sign_up_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
    Column('en_form_header', String(length=255)),
    Column('en_mailchimp_token', String(length=20)),
    Column('ru_form_header', String(length=255)),
    Column('ru_mailchimp_token', String(length=20)),
    Column('fr_form_header', String(length=255)),
    Column('fr_mailchimp_token', String(length=20)),
    Column('es_form_header', String(length=255)),
    Column('es_mailchimp_token', String(length=20)),
)

camp_staff_block = Table('camp_staff_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
)

camp_staff_record = Table('camp_staff_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('en_name', String(length=255)),
    Column('en_role', String(length=255)),
    Column('ru_name', String(length=255)),
    Column('ru_role', String(length=255)),
    Column('fr_name', String(length=255)),
    Column('fr_role', String(length=255)),
    Column('es_name', String(length=255)),
    Column('es_role', String(length=255)),
    Column('en_info', String(length=1000)),
    Column('ru_info', String(length=1000)),
    Column('fr_info', String(length=1000)),
    Column('es_info', String(length=1000)),
    Column('en_hidden', String(length=1000)),
    Column('ru_hidden', String(length=1000)),
    Column('fr_hidden', String(length=1000)),
    Column('es_hidden', String(length=1000)),
    Column('en_contacts', String(length=1000)),
    Column('ru_contacts', String(length=1000)),
    Column('fr_contacts', String(length=1000)),
    Column('es_contacts', String(length=1000)),
    Column('img_link', String(length=255)),
)

camp_staff_records = Table('camp_staff_records', post_meta,
    Column('staff_block_id', Integer),
    Column('staff_record_id', Integer),
)

camp_top_info_block = Table('camp_top_info_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
)

camp_top_slider_block = Table('camp_top_slider_block', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('camp_id', Integer),
    Column('camp_name', String(length=20)),
)

camp_top_slider_record = Table('camp_top_slider_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('en_header', String(length=255)),
    Column('en_subheader', String(length=255)),
    Column('ru_header', String(length=255)),
    Column('ru_subheader', String(length=255)),
    Column('fr_header', String(length=255)),
    Column('fr_subheader', String(length=255)),
    Column('es_header', String(length=255)),
    Column('es_subheader', String(length=255)),
)

camp_top_slider_records = Table('camp_top_slider_records', post_meta,
    Column('slider_block_id', Integer),
    Column('slide_record_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_block'].create()
    post_meta.tables['camp_contact_record'].create()
    post_meta.tables['camp_contact_records'].create()
    post_meta.tables['camp_main_info_block'].create()
    post_meta.tables['camp_main_info_block_photo'].create()
    post_meta.tables['camp_main_info_block_photos'].create()
    post_meta.tables['camp_partner_record'].create()
    post_meta.tables['camp_partners_block'].create()
    post_meta.tables['camp_partners_records'].create()
    post_meta.tables['camp_service_record'].create()
    post_meta.tables['camp_services_block'].create()
    post_meta.tables['camp_services_records'].create()
    post_meta.tables['camp_sign_up_block'].create()
    post_meta.tables['camp_staff_block'].create()
    post_meta.tables['camp_staff_record'].create()
    post_meta.tables['camp_staff_records'].create()
    post_meta.tables['camp_top_info_block'].create()
    post_meta.tables['camp_top_slider_block'].create()
    post_meta.tables['camp_top_slider_record'].create()
    post_meta.tables['camp_top_slider_records'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_contact_block'].drop()
    post_meta.tables['camp_contact_record'].drop()
    post_meta.tables['camp_contact_records'].drop()
    post_meta.tables['camp_main_info_block'].drop()
    post_meta.tables['camp_main_info_block_photo'].drop()
    post_meta.tables['camp_main_info_block_photos'].drop()
    post_meta.tables['camp_partner_record'].drop()
    post_meta.tables['camp_partners_block'].drop()
    post_meta.tables['camp_partners_records'].drop()
    post_meta.tables['camp_service_record'].drop()
    post_meta.tables['camp_services_block'].drop()
    post_meta.tables['camp_services_records'].drop()
    post_meta.tables['camp_sign_up_block'].drop()
    post_meta.tables['camp_staff_block'].drop()
    post_meta.tables['camp_staff_record'].drop()
    post_meta.tables['camp_staff_records'].drop()
    post_meta.tables['camp_top_info_block'].drop()
    post_meta.tables['camp_top_slider_block'].drop()
    post_meta.tables['camp_top_slider_record'].drop()
    post_meta.tables['camp_top_slider_records'].drop()
