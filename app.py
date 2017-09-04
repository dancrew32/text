import datetime
import flask
import schedule
import time
import threading
import wake
import lunch

app = flask.Flask(__name__)

@app.route('/')
def index():
    return str(datetime.datetime.now())


def go():
    schedule.every().day.at('8:00').do(wake.wake)
    schedule.every().day.at('12:00').do(lunch.lunch)

    while True:
        schedule.run_pending()
        time.sleep(1)


thread = threading.Thread(target=go)
thread.daemon = True
thread.start()
