import schedule
import time
import wake


schedule.every().day.at('8:00 PDT').do(wake.wake)

while True:
    schedule.run_pending()
    time.sleep(1)

