# what is a lambda function
x = lambda a: a * 5
print(x(6))


# or a better, more cleaner way of doing it would be
def setter(n):
    return lambda a, b: a + b * n  # do you know what the arithmetic priority is?


m = setter(3)
print(m(4, 5))
