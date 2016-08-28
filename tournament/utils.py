import random


def gen_code(name):
    words = name.split(" ")
    code = "".join([word[0:1].upper() for word in words]) + str(random.randint(1, 571))
    return code

