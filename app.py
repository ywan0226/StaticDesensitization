from flask import Flask

from API.api import *
from model import db

app = Flask(__name__)
db.init_app(app)

app.register_blueprint(api, url_prefix='/hello')

if __name__ == '__main__':
    app.run()
