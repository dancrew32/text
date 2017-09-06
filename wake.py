import random
import text

messages = (
    'Get up.',
    'Get out of bed.',
    'Rise and shine.',
)

def wake():
    message = random.choice(messages)
    text.me(message)
    print(message)
