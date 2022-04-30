from flask import Flask, render_template
from sqlalchemy import func
from config import Config

from extensions import db
from flask_migrate import Migrate

from models import Room, Customer, Rack

app = Flask(__name__)
app.config.from_object(Config)


db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    user = {
        'username': 'username'
    }

    return render_template('index.html', title='Home', user=user)


from api import *


if __name__ == '__main__':
    app.run(debug=False)
