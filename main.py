from flask import Flask, render_template
from flask_ngrok import run_with_ngrok

from blueprints import user_authenticate, users, events, comments

from data import db_session

app = Flask(__name__)
app.config.from_object('config')
user_authenticate.login_manager.init_app(app)
db_session.global_init('db/SQLiteBase.sqlite')

app.register_blueprint(user_authenticate.blueprint)
app.register_blueprint(users.blueprint)
app.register_blueprint(events.blueprint)
app.register_blueprint(comments.blueprint)
run_with_ngrok(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
