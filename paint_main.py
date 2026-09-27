from turtle import *
from paint_modul import *                       # подключаем модули (в т.ч. созданный нами)

t = Turtle()                                    # создаём черепашку как объект Черепашка
t.color('red')                                  # и задаём ей необходимые параметры
t.speed(3)
t.shape('circle')

def black_bg():                                 # Далее следуют ФУНКЦИИ-ОБРАБОТЧИКИ.
    scr.bgcolor('black')
def white_bg():
    scr.bgcolor('white')                        # эти меняют цвет фона экрана

def draw(x,y):
    t.goto(x,y)                                 # рисует линию при зажатии на черепашке
def move(x,y):                                  
    t.penup()
    t.goto(x,y)
    t.pendown()                                 # перемещает черепашку в то место, куда кликнет человек

def width1():
    t.width(5)
def width2():
    t.width(10)
def width3():
    t.width(15)                                 # меняют размер пера (аналогично работает pensize)

def green():
    t.color('green')
def blue():
    t.color('blue')
def red():
    t.color('red')
def black():
    t.color('black')
def white():
    t.color('white')
def purple():
    t.color('purple')
def yellow():
    t.color('yellow')                           # меняют цвет пера

def right():
    t.goto(t.xcor() + 5, t.ycor())
def left():
    t.goto(t.xcor() - 5, t.ycor())
def up():
    t.goto(t.xcor(), t.ycor() + 5)
def down():
    t.goto(t.xcor(), t.ycor() - 5)              # перемещают черепашку по прямым линиям


scr = Screen()                                  # Создаём объект ЭКРАН (можно так, можно через scr = t.getscreen())
scr.listen()                                    # Экран должен СЛУШАТЬ клавиатуру, по умолчанию отслеживается только мышь

t.ondrag(draw)
scr.onscreenclick(move)                         # Передвижения мышкой

scr.onkey(red, '1')
scr.onkey(blue, '2')
scr.onkey(green,'3')
scr.onkey(black, '4')
scr.onkey(white, '5')
scr.onkey(purple,'6')
scr.onkey(yellow, '7')                          # Подключаем к клавишам смену цветов пера

scr.onkey(width1, '8')
scr.onkey(width2, '9')
scr.onkey(width3, '0')                          # Подключаем к клавишам смену размера пера

scr.onkey(black_bg,'z')
scr.onkey(white_bg,'x')                         # Подключаем к клавишам смену цвета фона экрана

scr.onkey(right, 'd')
scr.onkey(left, 'a')
scr.onkey(up, 'w')
scr.onkey(down, 's')                            # Перемещение пера по клавишам                        


