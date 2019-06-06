from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# setting up configuration
app.config.from_object(DevConfig)


# intializing flask extensions
bootstrap = Bootstrap(app)


from app import views
