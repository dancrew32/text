import random
import text
import yelp
import os

messages = (
    'Dinner time.\n%s',
)

def home():
    message = random.choice(messages)
    searches = yelp.search('dinner', os.environ['HOME_ADDRESS'])
    biz = 'Try %s' % random.choice(searches)
    out = message % biz
    text.me(out)
