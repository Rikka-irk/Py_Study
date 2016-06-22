# Fibonacci sequence function
def fib(num1, num2, len):
    a, b = num1, num2
    for i in range(0, len):
        print(i + 1, ': ', a)
        a, b = b, a + b


def fib_generator(num):
    a, b = 0, 1
    for i in range(0, num):
        yield "{}: {}".format(i + 1, a)
        a, b = b, a + b


print("Fibonacci sequence function:")
fib(5,19,8)

# print('\n' + 'Fibonacci sequence using generator:')
# for item in fib_generator(10):
#     print(item)
