import random
import text
import yelp
import os

messages = (
    'It is lunch time.\n%s',
    'Eat some lunch.\n%s',
    'Get some lunch.\n%s',
)

def work():
    message = random.choice(messages)
    searches = yelp.search('lunch', os.environ['WORK_ADDRESS'])
    biz = 'Try %s' % random.choice(searches)
    out = message % biz
    text.me(out)


def bub():
    message = random.choice(messages)
    searches = yelp.search('lunch', os.environ['BUB_WORK_ADDRESS'])
    biz = 'Try %s' % random.choice(searches)
    out = message % biz
    text.bub(out)


def home():
    message = random.choice(messages)
    searches = yelp.search('lunch', os.environ['HOME_ADDRESS'])
    biz = 'Try %s' % random.choice(searches)
    out = message % biz
    text.me(out)
