from random import randrange


def generate_array(length):
    arr = []
    for q in range(0, length):
        arr.append(randrange(1, length * 2))
    return arr
