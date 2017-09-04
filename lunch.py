import random
import text

messages = (
    'It is lunch time.',
    'Eat some lunch.',
    'Get some lunch.',
)

def lunch():
    message = random.choice(messages)
    text.text(message)
