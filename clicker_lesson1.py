from random import randint
from time import time
import pygame as pg                                                                 # импорт нужных модулей

pg.init()                                                                           # подключаем возможности pygame в браузер

YELLOW = (255, 255, 0)
BLUE = (80, 80, 255)
BACK = (200, 255, 255)                                                              # для цветов лучше создать переменные заранее

mw = pg.display.set_mode((500, 500))
mw.fill(BACK)                                                                       # создаём окно размером 500 на 500, заполняем цветом (у меня это BACK),
clock = pg.time.Clock()                                                             # и создаём таймер для фпс


class Area():                                                                       # класс Area СОЗДАЁТ прямоугольник в координатах x y и размерами weidth и heigth
    def __init__(self, x, y, weidth, heigth, color):
        self.rect = pg.Rect(x, y, weidth, heigth)
        self.color = color
    
    def fill(self):                                                                 # метод fill РИСУЕТ залитый прямоугольник self.rect в окне mw цвета self.color
        pg.draw.rect(mw, self.color, self.rect) 

    def outline(self, color, width):                                                # метод outline РИСУЕТ ободок для self.rect в окне mw цвета color с шириной width
        pg.draw.rect(mw, color, self.rect, width)


class Label(Area):                                                                  # класс Label СОЗДАЁТ прямоугольник по тем же правилам, что и Area, ведь он его наследник
    def set_text(self,text , fsize, color=(0, 0, 0)):
        self.image = pg.font.SysFont("verdana", fsize).render(text, True, color)    # а метод set_text СОЗДАЁТ текст в этом прямоугольнике (SysFont - системный шрифт)
                        # настраиваем шрифт          # применяем его к тексту text
    def draw(self, sh_x, sh_y):                                                     # draw РИСУЕТ текст в прямоугольнике с отступами от его верхнего левого угла (sh_x, sh_y)
        self.fill()
        mw.blit(self.image, (self.rect.x + sh_x, self.rect.y + sh_y))


cards = []                                                                          # создаём список карточек и задём положение x для первой карточки
x = 70

for i in range(4):                                                                  # СОЗДАЁМ 4 карточки через класс Label, задаём ободок через outline и текст set_text
    new_card = Label(x, 170, 70, 100, YELLOW)
    new_card.outline(BLUE, 10)
    new_card.set_text("CLICK", 26)
    cards.append(new_card)                                                          # добавляем карточку в список карточек cards
    x += 100                                                                        # и меняем положение x для следующей карточки


while True:                                                                         # начинаем игровой цикл!
    for card in cards:                                                              # для каждой карточки в списке cards...
        card.draw(10,40)                                                                # НАРИСОВАТЬ карточку (в скобках указывает отступ для текста)

    pg.display.update()
    clock.tick(40)                                                                  # не забываем обновлять экран и установить кол-во кадров в секунду (fps)



    
