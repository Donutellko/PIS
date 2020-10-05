print(f"(Сумма букв в полном имени) % 4 + 1  =  {len('Донат') % 4 + 1}")

print("""
Задача 2.
Создайте приложение для перевода из одной системы счисления в другую
""")

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.upper()


def convert(number, s1, s2):
    decimal = toDecimal(number, s1)
    return toBase(decimal, s2)


def toDecimal(number, base):
    if base == 10:
        return int(number)
    decimal = 0
    for i in range(len(number)):
        digit = number[-1 - i]
        decimal += digitToDecimal(digit) * (base ** i)
    return decimal


def toBase(number, base):
    if number == 0:
        return ""
    return toBase(number // base, base) + decimalToDigit(number % base)


def digitToDecimal(digit):
    return digits.find(digit.upper())


def decimalToDigit(decimal):
    return digits[decimal]


def main():
    print(f"Max supported number base is {len(digits) - 1}")
    print(f"Supported digits are: {digits} \n")

    number = input("Введите число: ")
    s1 = int(input("Исходная система счисления: "))
    s2 = int(input("Результирующая система счисления: "))

    result = convert(number, s1, s2)
    print("Результат:", result)


def demo(number, s1, s2):
    print(f"({s1} -> {s2})\t {number} = {convert(number, s1, s2)}")


demo('1A', 16, 10)
demo('26', 10, 16)
demo('1A', 16, 2)
