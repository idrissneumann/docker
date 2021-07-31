from flask_sqlalchemy import SQLAlchemy

import os

class DbConnection():
    app = None
    db = None

    def __init__(self, app):
        self.app = app

        psql_user = os.environ['PSQL_USER']
        psql_password = os.environ['PSQL_PASSWORD']
        psql_host = os.environ['PSQL_HOST']
        psql_port = os.environ['PSQL_PORT']
        psql_dbname = os.environ['PSQL_DBNAME']

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://{}:{}@{}:{}/{}'.format(psql_user, psql_password, psql_host, psql_port, psql_dbname)
        self.db = SQLAlchemy(self.app)

    def get_db(self):
        return self.db
