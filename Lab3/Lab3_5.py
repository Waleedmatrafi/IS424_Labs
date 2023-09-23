x = int(input("Enter a number of repetitions"))


def repeat(r):
    def wrapper():
        for i in range(x):
            r()
    return wrapper


@repeat
def hello():
    print('Hello')


hello()
