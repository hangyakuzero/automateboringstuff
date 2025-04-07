# basically calling another function inside a function
def decorator(func):
    def inner():
        print("decorator function started")
        print("calling the function that was passed")
        func()
        print("the function should have been called")

    return inner


@decorator
def best():
    print("hello everyone")


best()
