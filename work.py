import random
import text

messages = (
    'Go home.',
    'Work is over. Go home.',
    'Stop working. Go home.',
    'git commit -am "todo, going home"',
)

def go_home():
    message = random.choice(messages)
    text.me(message)
