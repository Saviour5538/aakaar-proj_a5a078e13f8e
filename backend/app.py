from flask import Flask
from config import Config
from database.migrations import init_db

app = Flask(__name__)
app.config.from_object(Config)
init_db(app)