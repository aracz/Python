# implement commonly used functions here

import random
import string


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate_random(table):
    generated = ''
    generated += random.choice(string.ascii_lowercase)
    generated += random.choice(string.ascii_uppercase)
    generated += random.choice(string.digits)
    generated += random.choice(string.digits)
    generated += random.choice(string.ascii_uppercase)
    generated += random.choice(string.ascii_lowercase)
    generated += random.choice('$#@&')
    generated += random.choice('$#@&')

    if generated in [item[0] for item in table]:
        generated = generate_random(table)
    return generated
