import os
import random
import requests
import text

API = 'http://webservices.nextbus.com/service/publicJSONFeed'

messages = (
    '%s\nBus safe! Precious cargo!',
    '%s\nHave the best day!',
    '%s\nSee ya later, alligator!',
    '%s\nLove you to bits!',
    '%s\nYou are the best!',
)


def bub_am_times():
    params = {
        'command': 'predictions',
        'a': 'sf-muni',
        'r': os.environ['BUB_ROUTE_AM'],
        's': os.environ['BUB_STOP_AM'],
    }
    r = requests.get(API, params=params)
    data = r.json()['predictions']
    times = [int(p['minutes']) for p in data['direction']['prediction']]
    last_time = times[-1]
    times[-1] = 'or %s %s' % (last_time, 'minute' if last_time == 1 else 'minutes')
    return u'{title} in {times}.'.format(
        title=data['routeTitle'].replace('-', ' '),
        times=', '.join([str(t) for t in times]))


def bub_am():
    message = random.choice(messages)
    times = bub_am_times()
    out = message % times
    text.bub(out)
