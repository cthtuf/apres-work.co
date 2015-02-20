from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt_registration', DateTime),
    Column('dt_last_action', DateTime),
    Column('location_id', Integer),
    Column('phone', String(length=10)),
    Column('email', String(length=120)),
    Column('ga_client_id', Integer),
)

subscription = Table('subscription', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('dt', DateTime),
    Column('location_id', Integer),
    Column('email', String(length=120)),
    Column('ga_client_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['dt_last_action'].create()
    post_meta.tables['user'].columns['dt_registration'].create()
    post_meta.tables['subscription'].columns['dt'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['dt_last_action'].drop()
    post_meta.tables['user'].columns['dt_registration'].drop()
    post_meta.tables['subscription'].columns['dt'].drop()
