import datetime
import flask
import schedule
import time
import threading
import wake

app = flask.Flask(__name__)

@app.route('/')
def index(path):
    return str(datetime.datetime.now())


def go():
    schedule.every().day.at('8:00').do(wake.wake)

    while True:
        schedule.run_pending()
        time.sleep(1)


threading.Thread(target=go)
t.daemon = True
t.start()
