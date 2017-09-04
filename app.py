import schedule
import time
import wake


schedule.every().day.at('11:10 PDT').do(wake.wake)

while True:
    schedule.run_pending()
    time.sleep(1)

