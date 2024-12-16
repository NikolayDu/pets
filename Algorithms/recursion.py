# Recursion

# Рекурсия - вызов функции самой себя. В каждой рекурсивной функции должно быть два случая: базовый и рекурсивный

def factorial(x):
    """
    :param x: number
    :return: factorial of number
    """
    if x == 1:  # Базовый случай
        return 1
    else:   # Рекурсивный случай
        return x * factorial(x - 1)

print(factorial(3))