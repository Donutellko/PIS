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
    print("    {} км за {} дней".format(distance, task1(distance)))


print("""
Задание 2
Каждый день я пробегаю «следующее простое число» км. 
Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км? (дополнительная задача, понять, как отличается от номера 1)
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
    print("    {} км за {} дней".format(distance, task2(distance)))



print("""
Задание 3
Начав тренировки, спортсмен в первый день пробежал 10 км. 
Для увеличения выносливости ему необходимо повышать норму бега через одну тренировку на 15% от нормы предыдущей тренировки. 
Спортсмен тренируется каждый день. Какой суммарный путь он пробежит за 30 дней.
""")


def task3(days):
    i = 1
    sum = 0
    perDay = 10
    mult = 1.15
    while i <= days:
        sum += perDay
        perDay *= mult
        i += 1
    return sum


# Test
expected = 10 + 10 * 1.15 + 10 * (1.15 ** 2)
actual = task3(3)
assert expected - actual < 0.1
# end test

# Demo
print(f"    За 2 дня пробежит {task3(2)} км")
print(f"    За 30 дней пробежит {task3(30)} км")



print("""
Задание 4
Начав тренировки, спортсмен в первый день пробежал 10 км. 
Каждый следующий день он увеличивал дневную норму на 10% от нормы предыдущего дня. 
Через сколько дней:
а) спортсмен будет пробегать в день больше 20 км;
""")


def task4a(n):
    i = 0
    perDay = 10
    mult = 1.10
    while perDay <= n:
        perDay *= mult
        i += 1
    return i


# Test
expected = 8
assert (10 * (1.10 ** expected - 1)) <= 20
assert (10 * (1.10 ** expected)) > 20
assert expected == task4a(20)
# End test

# Demo
print(f"    Больше 20 км в день через {task4a(20)} дней")


print("""
b) пробежит суммарный путь 100 км.
""")


def task4b(n):
    i = 0
    sum = 0
    perDay = 10
    mult = 1.10
    while sum < n:
        sum += perDay
        perDay *= mult
        i += 1
    return i


# Test
assert 1 == task4b(10)
assert 2 == task4b(21)
# End test

# Demo
print(f"    Пробежит суммарный путь 100 км через {task4b(100)} дней")