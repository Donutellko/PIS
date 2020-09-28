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
