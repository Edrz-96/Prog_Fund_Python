# add
def add(i, j):
    return i + j


# subtract
def subtract(i, j):
    return i - j


# divide
def divide(i, j):
    if j == 0:
        raise ArithmeticError
    else:
        return i / j


# multiply
def multiply(i, j):
    return i * j
