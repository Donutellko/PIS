print("""
Задание 3
Нарисовать рамочку шириной w символов и высотой h символов, и толщиной f символов. (оформить в виде функции)
""")


def task3(w, h, f):
    printHorizontal(w, f)
    for i in range(h):
        print(f * '*' + w * ' ' + f * '*')
    printHorizontal(w, f)


def printHorizontal(w, f):
    for i in range(f):
        print((w + f * 2) * '*')


# Демо

"""
Ожидаемый результат:
*******
*******
**   **
**   **
*******
*******
"""
task3(3, 2, 2)