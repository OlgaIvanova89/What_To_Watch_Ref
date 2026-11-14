from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = Config.SECRET_KEY
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from opinions_app import cli_commands, models, views, error_handlers
