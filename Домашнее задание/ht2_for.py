print("""
Задание 1
Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...
""")
print("    Примечание: индексы считаю с 1")


def task1(n):
    if n <= 2:
        return 1
    a = 1
    b = 1
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    return b


# Test
assert 1 == task1(1)
assert 1 == task1(2)
assert 2 == task1(3)
assert 3 == task1(4)
assert 5 == task1(5)
# end test

# Demo
print(f"    3  член последовательности: {task1(3)}")
print(f"    10 член последовательности: {task1(10)}")


print("""
Задание 2
Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17...
""")


def task2(n):
    if n <= 3:
        return 1
    a = 1
    b = 1
    c = 1
    for i in range(n - 3):
        d = a + b + c
        a = b
        b = c
        c = d
    return c


# Test
assert 1 == task2(1)
assert 1 == task2(2)
assert 1 == task2(3)
assert 3 == task2(4)
assert 5 == task2(5)
assert 9 == task2(6)
# end test

# Demo
print(f"    4  член последовательности: {task2(4)}")
print(f"    10 член последовательности: {task2(10)}")


print("""
Задание 3
Вывести квадраты нечетных чисел до N. (генератором списков)
""")


def task3(n):
    return [i ** 2 for i in range(1, n + 1, 2)]


# Test
expected = [1, 9, 25, 49]
actual = task3(7)
assert expected == actual
# end test


# Demo
print("N=7: ", task3(7))


print("""
Задание 5
Даны натуральные числа А и В. Вывести сначала все чётные числа, заключённые
между ними, потом все нечётные (генератором/ами списков).
""")


def task5(a, b):
    next_even = 2 * (a + 1 // 2)
    next_odd = 2 * (a // 2) + 1
    return [i for i in range(next_even, b, 2)] + \
           [i for i in range(next_odd, b, 2)]


# Test
expected = [4, 6, 8] + [3, 5, 7]
actual = task5(2, 9)
assert expected == actual
# End test


# Demo
print("Между 1 и 3:", task5(1, 3))
print("Между 2 и 9:", task5(2, 9))


print("""
Задание 6
Исходный список содержит положительные и отрицательные числа. Требуется
положительные поместить в один список, а отрицательные - в другой (генератором/ами списков)
""")


def task6(list):
    positive = [i for i in list if i > 0]
    negative = [i for i in list if i < 0]
    return positive, negative


# Test
source = [1, -10, 0, 15, -123, -432, 123]
expectedPos = [1, 15, 123]
expectedNeg = [-10, -123, -432]

actualPos, actualNeg = task6(source)

assert expectedPos == actualPos
assert expectedNeg == actualNeg
# End test


# Демо
print("Исходный список:", source)
print("Положительные из него:", actualPos)
print("Отрицательные из него:", actualNeg)
