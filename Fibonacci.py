# Simple Fibonacci sequence
print('Simple Fibonacci sequence')
a, b = 0, 1
for i in range(0, 10):
    print(a)
    a, b = b, a + b


# Fibonacci sequence function
def fib(num):
    a, b = 0, 1
    for i in range(0, num):
        print(i + 1, ': ', a)
        a, b = b, a + b


def fib_generator(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i + 1, a)
        a, b = b, a + b


print("Fibonacci sequence function:")
fib(10)

print('\n' + 'Fibonacci sequence using generator:')
for item in fib_generator(10):
    print(item)
