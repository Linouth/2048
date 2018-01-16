import json
import os
import datetime

from flask import (
        Flask, request, render_template
)
from peewee import TextField, DateTimeField, IntegerField
from playhouse.flask_utils import FlaskDB

app = Flask(__name__)

APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATABASE = 'sqlite:///{}'.format(os.path.join(app.instance_path, 'logger.db'))
DEBUG = False
SECRET_KEY = 'asdf'
SITE_NAME = '2048 Scoreboard'

app.config.from_object(__name__)

flask_db = FlaskDB(app)
database = flask_db.database


''' Models '''


class Score(flask_db.Model):
    player = TextField()
    score = IntegerField()
    timestamp = DateTimeField(default=datetime.datetime.now, index=True)

    class Meta:
        database = database


''' Views '''


@app.route('/')
def root():
    query = Score.select().order_by(Score.score.desc())
    # return f'{query.player} - {query.score}'
    return render_template('scoreboard.html', query=query)

@app.route('/new', methods=['POST'])
def new():
    data = json.loads(request.data)
    q = Score.select().where(Score.player==data['player']).first()

    if q == None:
        Score.create(player=data['player'], score=data['score'])
    else:
        q.score = data['score']
        q.save()
    return 'Ok.'


if __name__ == '__main__':
    database.create_tables([Score], safe=True)
