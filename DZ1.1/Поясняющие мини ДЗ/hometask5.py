"""
В течени практики, мы с вами учились писать
такие фигуры:
=
==
===
====
=====
Для этого мы выясняли какие символы в них есть,
сколько их и как они изменяются и использовали for
Например здесь быд такой код
"""
for i in range(1, 7):
    print(i*"=")
"""
а в таком случае
     =
    ==
   ===
  ====
 =====
======
код выглядед так:
(сколько-то пробелов + сколько-то '=')
"""
for i in range(1, 7):
    print((7-i)*" " + i*"=")


##########################################
# TODO задание 1
##########################################
"""Напищите код, изображающий фигуру
======
 =====
  ====
   ===
    ==
     =
     """
print("Результат задания 1")

c = 5
for i in range(c):
    print(i * " " + (c - i) * "=")


##########################################
# конец задания
##########################################

##########################################
# TODO задание 2
##########################################
"""Напищите код, изображающий фигуру
    =    
   ===   
  =====  
 =======
=========
(подумайте о том, из сокольки частей состоит фигура,
например x*" " + y*"=" + z * " ")
     """
print("Результат задания 2")

c = 5
for i in range(c):
    print((c - i) * " " + (i * 2 + 1) * "=" + (c - i) * " ")


##########################################
# конец задания
##########################################


##########################################
# TODO задание 3
##########################################
"""Напищите код, изображающий фигуру
=========
 =======
  =====  
   ===
    =
     """
print("Результат задания 3")

c = 5
for i in range(c - 1, -1, -1):
    print((c - i) * " " + (i * 2 + 1) * "=" + (c - i) * " ")

##########################################
# конец задания
##########################################


##########################################
# TODO задание 4 дополнительное
##########################################
"""Напищите код, любую красивую фигуру по
вашему желанию
     """
print("Результат задания 4")

for i in range(30):
    print(i * 'A' + i * '!')

##########################################
# конец задания
##########################################