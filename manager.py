from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

import config
from model import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
