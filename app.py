import datetime
import flask
import schedule
import time
import threading

import text
import wake
import bus
import dinner
import lunch
import work

app = flask.Flask(__name__)

@app.route('/')
def index():
    return str(datetime.datetime.now())


def go():
    schedule.every().day.at('7:00').do(wake.wake)

    schedule.every().monday.at('7:25').do(bus.bub_am)
    schedule.every().monday.at('12:00').do(lunch.work)
    schedule.every().monday.at('12:00').do(lunch.bub)
    schedule.every().monday.at('18:00').do(work.go_home)

    schedule.every().tuesday.at('7:30').do(bus.bub_am)
    schedule.every().tuesday.at('12:00').do(lunch.work)
    schedule.every().tuesday.at('12:00').do(lunch.bub)
    schedule.every().tuesday.at('18:00').do(work.go_home)

    schedule.every().wednesday.at('7:30').do(bus.bub_am)
    schedule.every().wednesday.at('12:00').do(lunch.work)
    schedule.every().wednesday.at('12:00').do(lunch.bub)
    schedule.every().wednesday.at('18:00').do(work.go_home)
    schedule.every().wednesday.at('18:15').do(dinner.home)

    schedule.every().thursday.at('7:30').do(bus.bub_am)
    schedule.every().thursday.at('12:00').do(lunch.work)
    schedule.every().thursday.at('12:00').do(lunch.bub)
    schedule.every().thursday.at('18:00').do(work.go_home)

    schedule.every().friday.at('7:30').do(bus.bub_am)
    schedule.every().friday.at('12:00').do(lunch.work)
    schedule.every().friday.at('12:00').do(lunch.bub)
    schedule.every().friday.at('17:00').do(work.go_home)

    schedule.every().saturday.at('12:00').do(lunch.home)
    schedule.every().saturday.at('17:30').do(dinner.home)

    schedule.every().sunday.at('12:00').do(lunch.home)
    schedule.every().sunday.at('17:30').do(dinner.home)

    while True:
        schedule.run_pending()
        time.sleep(1)


thread = threading.Thread(target=go)
thread.daemon = True
thread.start()
text.me('Running!')
