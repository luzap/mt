import random


def gen_code(name):
    """Generates a code for the school based upon initials and a random number, to avoid any potential cheating."""
    words = name.split(" ")
    code = "".join([word[0:1].upper() for word in words]) + str(random.randint(1, 571))
    return code

