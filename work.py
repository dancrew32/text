import random
import text

messages = (
    'Go home.',
    'Work is over. Go home.',
    'Stop working. Go home.',
    'git commit -am "finish that shit tomorrow, going home now"',
)

def go_home():
    message = random.choice(messages)
    text.text(message % biz)
