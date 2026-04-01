import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def init_app(self, app: Flask):
        db = SQLAlchemy()
        migrate = Migrate(db)
        db.init_app(app)
        migrate.init_app(app, db)

        with app.app_context():
            db.create_all()