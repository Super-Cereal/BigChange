from flask import Flask, render_template
from blueprints import user_authenticate, users, events

from data import db_session

app = Flask(__name__)
app.config.from_object('config')
user_authenticate.login_manager.init_app(app)
db_session.global_init('db/SQLiteBase.sqlite')

app.register_blueprint(user_authenticate.blueprint)
app.register_blueprint(users.blueprint)
app.register_blueprint(events.blueprint)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    if True:
        app.run()
