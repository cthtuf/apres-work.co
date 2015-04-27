from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
camp_sign_up_option_record = Table('camp_sign_up_option_record', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('order_index', Integer),
    Column('group', String(length=20)),
    Column('value', String(length=255)),
    Column('cost', Integer),
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
    Column('en_signup_button', String(length=20)),
    Column('ru_signup_button', String(length=20)),
    Column('fr_signup_button', String(length=20)),
    Column('es_signup_button', String(length=20)),
    Column('initial_cost', Integer),
    Column('en_price_info', String(length=2000)),
    Column('ru_price_info', String(length=2000)),
    Column('fr_price_info', String(length=2000)),
    Column('es_price_info', String(length=2000)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_sign_up_option_record'].columns['cost'].create()
    post_meta.tables['camp_sign_up_option_record'].columns['group'].create()
    post_meta.tables['camp_sign_up_option_record'].columns['value'].create()
    post_meta.tables['camp_sign_up_block'].columns['en_price_info'].create()
    post_meta.tables['camp_sign_up_block'].columns['es_price_info'].create()
    post_meta.tables['camp_sign_up_block'].columns['fr_price_info'].create()
    post_meta.tables['camp_sign_up_block'].columns['ru_price_info'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['camp_sign_up_option_record'].columns['cost'].drop()
    post_meta.tables['camp_sign_up_option_record'].columns['group'].drop()
    post_meta.tables['camp_sign_up_option_record'].columns['value'].drop()
    post_meta.tables['camp_sign_up_block'].columns['en_price_info'].drop()
    post_meta.tables['camp_sign_up_block'].columns['es_price_info'].drop()
    post_meta.tables['camp_sign_up_block'].columns['fr_price_info'].drop()
    post_meta.tables['camp_sign_up_block'].columns['ru_price_info'].drop()
