from turtle import *                                # подключаем модули

ti = Turtle()
ti.speed(0)
ti.hideturtle()                                     # создаём объект - черепашку для интерфейса

def square(x, y, col):                              # эта функция нарисует нам квадраты (x, y - расположение, col - цвет заливки)
    ti.color('gray', col)                           
    ti.seth(0)                                      # seth - направление для черепашки, где 0 - вправо
    ti.penup()
    ti.goto(x, y)
    ti.pendown()
    ti.begin_fill()
    for i in range(4):
        ti.forward(20)
        ti.left(90)
    ti.end_fill()

def symb(x, y, text):                               # эта функция напишет нам текст на экране (x, y - расположение, text - нужный текст)
    ti.color('darkgrey')
    ti.seth(0)
    ti.penup()
    ti.goto(x, y)
    ti.pendown()
    ti.write(text, font = ('Arial', 15, 'bold'))

def circ(x, y, r):                                  # эта функция нарисует круг (x, y - расположение, r - радиус круга)
    ti.color('grey')
    ti.seth(0)
    ti.penup()
    ti.goto(x, y)
    ti.pendown()
    ti.begin_fill()
    ti.circle(r)
    ti.end_fill()



square(-200, -100, 'black')                         # вызываем нужные функции для рисования интерфейса
square(-175, -100, 'white')                         # это для кнопок смены фона                         

symb(-195, -75, 'z')
symb(-170, -75, 'x')                                # и названия клавиш для них 

square(-100, -100, 'red')
square(-75, -100, 'blue')
square(-50, -100, 'green')
square(-25, -100, 'black')
square(0, -100, 'white')
square(25, -100, 'purple')
square(50, -100, 'yellow')                          # это для кнопок смены цвета пера

symb(-95, -75, '1')
symb(-70, -75, '2')
symb(-45, -75, '3')
symb(-20, -75, '4')
symb(5, -75, '5')
symb(30, -75, '6')
symb(55, -75, '7')                                  # это для кнопок смены цвета пера

circ(110, -94, 5)
circ(130, -98, 10)
circ(160, -102, 15)                                 # это для кнопок смены размера пера

symb(106, -70, '8')
symb(125, -70, '9')
symb(155, -70, '0')                                 # это для кнопок смены размера пера
