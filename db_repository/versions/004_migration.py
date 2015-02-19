from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
location = Table('location', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('site_id', Integer),
    Column('suffix', String(length=10)),
    Column('name', String(length=20)),
    Column('description', String(length=200)),
)

partner = Table('partner', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=120)),
    Column('resort_id', Integer),
)

partner_user = Table('partner_user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=20)),
    Column('email', String(length=50)),
    Column('phone', String(length=10)),
    Column('password', String(length=20)),
)

promo_code = Table('promo_code', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt', DateTime),
    Column('user_id', Integer),
    Column('sms_id', Integer),
    Column('promotion_id', Integer),
    Column('code', String(length=10)),
    Column('is_unique', Boolean),
    Column('dt_used', DateTime),
)

promotion = Table('promotion', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt', DateTime),
    Column('partner_id', Integer),
    Column('has_group_promocode', Boolean),
    Column('event_id', Integer),
)

SMS = Table('SMS', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt', DateTime),
    Column('user_id', Integer),
    Column('promocode_id', Integer),
    Column('text', String(length=560)),
)

webcamera = Table('webcamera', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('site_id', INTEGER),
    Column('resort_id', INTEGER),
    Column('img_link', VARCHAR(length=255)),
    Column('img_na', VARCHAR(length=255)),
)

webcamera = Table('webcamera', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('resort_id', Integer),
    Column('img_link', String(length=255)),
    Column('img_na', String(length=255)),
)

resort = Table('resort', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('site_id', INTEGER),
    Column('name', VARCHAR(length=120)),
    Column('url_site', VARCHAR(length=255)),
    Column('url_ig', VARCHAR(length=255)),
    Column('url_vk', VARCHAR(length=255)),
    Column('url_fb', VARCHAR(length=255)),
    Column('la', FLOAT),
    Column('lo', FLOAT),
)

resort = Table('resort', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('name', String(length=120)),
    Column('url_site', String(length=255)),
    Column('url_ig', String(length=255)),
    Column('url_vk', String(length=255)),
    Column('url_fb', String(length=255)),
    Column('la', Float),
    Column('lo', Float),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('phone', VARCHAR(length=10)),
    Column('email', VARCHAR(length=120)),
    Column('ga_client_id', INTEGER),
    Column('site_id', INTEGER),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('phone', String(length=10)),
    Column('email', String(length=120)),
    Column('ga_client_id', Integer),
)

event = Table('event', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('site_id', INTEGER),
    Column('dt', DATETIME),
    Column('resort_id', INTEGER),
    Column('name', VARCHAR(length=50)),
    Column('description', VARCHAR(length=1000)),
)

event = Table('event', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('dt', DateTime),
    Column('resort_id', Integer),
    Column('name', String(length=50)),
    Column('description', String(length=1000)),
)

subscription = Table('subscription', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('email', VARCHAR(length=120)),
    Column('ga_client_id', INTEGER),
    Column('site_id', INTEGER),
)

subscription = Table('subscription', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('location_id', Integer),
    Column('email', String(length=120)),
    Column('ga_client_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['location'].create()
    post_meta.tables['partner'].create()
    post_meta.tables['partner_user'].create()
    post_meta.tables['promo_code'].create()
    post_meta.tables['promotion'].create()
    post_meta.tables['SMS'].columns['dt'].create()
    post_meta.tables['SMS'].columns['promocode_id'].create()
    pre_meta.tables['webcamera'].columns['site_id'].drop()
    post_meta.tables['webcamera'].columns['location_id'].create()
    pre_meta.tables['resort'].columns['site_id'].drop()
    post_meta.tables['resort'].columns['location_id'].create()
    pre_meta.tables['user'].columns['site_id'].drop()
    post_meta.tables['user'].columns['location_id'].create()
    pre_meta.tables['event'].columns['site_id'].drop()
    post_meta.tables['event'].columns['location_id'].create()
    pre_meta.tables['subscription'].columns['site_id'].drop()
    post_meta.tables['subscription'].columns['location_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['location'].drop()
    post_meta.tables['partner'].drop()
    post_meta.tables['partner_user'].drop()
    post_meta.tables['promo_code'].drop()
    post_meta.tables['promotion'].drop()
    post_meta.tables['SMS'].columns['dt'].drop()
    post_meta.tables['SMS'].columns['promocode_id'].drop()
    pre_meta.tables['webcamera'].columns['site_id'].create()
    post_meta.tables['webcamera'].columns['location_id'].drop()
    pre_meta.tables['resort'].columns['site_id'].create()
    post_meta.tables['resort'].columns['location_id'].drop()
    pre_meta.tables['user'].columns['site_id'].create()
    post_meta.tables['user'].columns['location_id'].drop()
    pre_meta.tables['event'].columns['site_id'].create()
    post_meta.tables['event'].columns['location_id'].drop()
    pre_meta.tables['subscription'].columns['site_id'].create()
    post_meta.tables['subscription'].columns['location_id'].drop()
