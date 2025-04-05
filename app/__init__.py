from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect 
from flask_wtf.csrf import generate_csrf
from flask_cors import CORS
from app.config import Config
from app.logger import logger  # Import the logger

# Initialize Flask application
app = Flask(__name__)

CORS(app)

app.config.from_object(Config)

@app.after_request
def set_csrf_cookie(response):
    response.set_cookie('csrf_token', generate_csrf())
    return response

# Use the logger
logger.info("Flask application initialized.")

# Instantiate CSRF-Protect library here
csrf = CSRFProtect(app)

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

from app import views