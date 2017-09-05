import datetime
import flask
import schedule
import time
import threading

import wake
import lunch
import work

app = flask.Flask(__name__)

@app.route('/')
def index():
    return str(datetime.datetime.now())


def go():
    schedule.every().day.at('8:00').do(wake.wake)

    schedule.every().monday.at('12:00').do(lunch.work)
    schedule.every().monday.at('18:00').do(work.go_home)

    schedule.every().tuesday.at('12:00').do(lunch.work)
    schedule.every().tuesday.at('18:00').do(work.go_home)

    schedule.every().wednesday.at('12:00').do(lunch.work)
    schedule.every().wednesday.at('18:00').do(work.go_home)

    schedule.every().thursday.at('12:00').do(lunch.work)
    schedule.every().thursday.at('18:00').do(work.go_home)

    schedule.every().friday.at('12:00').do(lunch.work)
    schedule.every().friday.at('17:00').do(work.go_home)

    schedule.every().saturday.at('12:00').do(lunch.home)
    schedule.every().sunday.at('12:00').do(lunch.home)

    while True:
        schedule.run_pending()
        time.sleep(1)


thread = threading.Thread(target=go)
thread.daemon = True
thread.start()
