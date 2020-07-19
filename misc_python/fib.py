def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def gcf(x, y):
    if x > y:
        lesser = y
    else:
        lesser = x
    for i in range(1, lesser + 1):
        if (x % i == 0) and (y % i == 0):
            result = i
    return result


def input_func():
    while True:
        num = input("Please enter a number greater than zero ")
        try:
            val = int(num)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")
    return val


n = input_func()
m = input_func()
x = fib(n)
y = fib(m)

print("The Fibonicci numbers for " + str(n) + " is " + str(x) + " and " + str(m) + ' is ' + str(y))
z = gcf(x, y)
print("The greatest common factor for " + str(x) + ' and ' + str(y) + ' is ' + str(z))
