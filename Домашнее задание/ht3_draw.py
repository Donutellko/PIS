print("""
Задание 1
Нарисовать рамочку шириной w символов и высотой h символов.
""")


def task1(w, h):
    s = '*'
    if h > 0:
        print(w * s)
    for i in range(h - 2):
        print(s + (w - 2) * ' ' + s)
    if h > 2:
        print(w * s)

# Демо

print("""
Ввод: w = 3, h = 3
Ожидаемый результат:
***
* *
***
На самом деле:""")

task1(3, 3)


print("""
Ввод: w = 1, h = 1
Ожидаемый результат:
*
На самом деле:""")
task1(1, 1)



print("""
Задание 2
Пускай символ, которым рисуется рамочка – тоже входной параметр.
""")


def task2(w, h, s):
    if h > 0:
        print(w * s)
    for i in range(h - 2):
        print(s + (w - 2) * ' ' + s)
    if h > 2:
        print(w * s)

# Демо
print("""
Ввод: w = 4, h = 4, s = 🐧
Ожидаемый результат:
🐧🐧🐧
🐧 🐧
🐧🐧🐧
На самом деле:""")
task2(3, 3, '🐧')


print("""
Задание 3
Нарисовать рамочку шириной w символов и высотой h символов, и толщиной f символов. (оформить в виде функции)
""")


def task3(w, h, f):
    fw = min(f, w // 2)
    fh = min(f, h // 2)
    printHorizontal(w, fh)
    for i in range(h - 2 * fh):
        print(fw * '*' + (w - 2 * fw) * ' ' + fw * '*')
    printHorizontal(w, fh)


def printHorizontal(w, fh):
    for i in range(fh):
        print(w * '*')


# Демо

print("""
Ввод: w = 4, h = 3, f = 10
Ожидаемый результат:
****
****
****
На самом деле:""")
task3(4, 3, 10)


print("""
Ввод: w = 7, h = 6, f = 2
Ожидаемый результат:
*******
*******
**   **
**   **
*******
*******
На самом деле:""")
task3(7, 6, 2)
