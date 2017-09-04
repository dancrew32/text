import random
import text
import yelp
import os

messages = (
    'It is lunch time. %s',
    'Eat some lunch. %s',
    'Get some lunch. %s',
)

def work():
    message = random.choice(messages)
    searches = yelp.search('lunch', os.environ['WORK_ADDRESS'])
    biz = 'Try %s' % random.choice(searches)
    text.text(message % biz)


def home():
    message = random.choice(messages)
    searches = yelp.search('lunch', os.environ['HOME_ADDRESS'])
    biz = 'Try %s' % random.choice(searches)
    text.text(message % biz)
