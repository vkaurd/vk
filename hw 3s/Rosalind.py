#Fibonacci Numbers
'''
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1 = 0
    f2 = 1
    for i in range(2, n + 1):
        current = f1 + f2  # складываем два предыдущих числа
        f1 = f2            # сдвигаем старые значения вперед
        f2 = current
    return f2
print(fib(6))
'''
#