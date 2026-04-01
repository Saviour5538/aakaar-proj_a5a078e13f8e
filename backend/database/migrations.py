from flask import current_app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate(db)

def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()