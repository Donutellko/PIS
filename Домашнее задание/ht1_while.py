print("""
Задание 1
Каждый день я пробегаю «следующую степень двойки» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км?
""")


# Сколько дней пройдет, пока я в сумме пробегу distance км
def task1(distance):
    sum = 0
    i = 0
    while sum < distance:
        sum += 2 ** i
        i += 1
    return i


# Test
expected = 14
actual = task1(10000)
assert expected == actual
# End test


# Демо
for i in range(5):
    distance = 10 ** i
    print("{} км за {} дней".format(distance, task1(distance)))


print("""
Задание 2
Каждый день я пробегаю «следующее простое число» км. Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км? (дополнительная задача, понять, как отличается от номера 1)
""")


# Сколько дней пройдет, пока я в сумме пробегу distance км
def task2(distance):
    sum = 0
    prime = 2
    i = 0
    while sum < distance:
        sum += prime
        prime = nextPrime(prime)
        i += 1
    return i


# Получить следующее простое число
def nextPrime(prevPrime):
    i = prevPrime + 1
    while not isPrime(i):
        i += 1
    return i


# Является ли число простым
def isPrime(number):
    i = 2
    while i <= number / 2:
        if number % i == 0:
            return False
        i += 1
    return True


# Test
expected = 68
actual = task2(10000)
assert expected == actual
# End test


# Демо
for i in range(5):
    distance = 10 ** i
    print("{} км за {} дней".format(distance, task2(distance)))

