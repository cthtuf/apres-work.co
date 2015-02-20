import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

WTF_CSRF_ENABLED = True
SECRET_KEY = 'Kds8fdA(*@UJjdfsy&S*A7f65d678&SYAtd56as78'
MONGO_DBNAME = 'apresworkco'

MAILCHIMP_TOKEN = 'c3d906f578511669ed27c60ce4079630-us10'
MAILCHIMP_SUBSCRIPTION_LIST_ID = '55fafc9548'
