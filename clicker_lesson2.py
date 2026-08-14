from random import randint
from time import time
import pygame as pg                                                                 # импорт нужных модулей

pg.init()                                                                           # подключаем возможности pygame в браузер

YELLOW = (255, 255, 0)
BLUE = (80, 80, 255)
BACK = (200, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 51)                                                              # для цветов лучше создать переменные заранее

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

    def collide(self, x, y):                                                        # метод collide ОТСЛЕЖИВАЕТ попадание точки x y в карточку self.rect
        return self.rect.collidepoint(x, y) 

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

wait = 0                                                                            # wait - важный счётчик, благодаря ей надпись click перескочит 
                                                                                    # на след. карточку не мгновенно, а спустя каждые 20 кадров

while True:                                                                         # начинаем игровой цикл!
      
    if wait == 0:                                                                   # если прошло 0 кадров...
        wait = 20                                                                       # устанавливаем кол-во кадров на 20, например (чем меньше, тем быстрее)
        click = randint(0, 3)                                                           # выбираем случайное число от 0 до 3 (так в списке пронумерованы карточки)
        for i in range(4):                                                              # для каждой из 4 карточек (range перебирает числа от 0 до 3, i хранит эти числа)
            cards[i].color = YELLOW                                                     # цвет каждой карточки == жёлтому, например                                                     
            if i == click:                                                              # если число карточки i равно случайному числу...
                cards[i].draw(10, 40)                                                       # то РИСУЕМ эту карточку вместе с текстом!
            else:
                cards[i].fill()                                                             # иначе РИСУЕМ пустой цветной прямоугольник!
    else:                                                                           # иначе... (если число кадров не равно 0)
        wait -= 1                                                                       # уменьшаем кол-во кадров на 1 

    for event in pg.event.get():                                                    # а это обработка нажатий по карточки. MOUSEBUTTONDOWN - событие нажатая кнопка мыши,
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:                  # event.button == 1 - это именно левая кнопка мыши
            x, y = event.pos                                                        # получаем координаты события (нажатия)
            for i in range(4):                                                      # снова перебираем все 4 карточки
                if cards[i].collide(x,y):                                           # если координаты события попали в границы карточки i...
                    if i == click:                                                         # и если её номер совпал с рандомным номером...
                        cards[i].color = GREEN                                                 # то ставим карточке зелёный цвет!
                    else:
                        cards[i].color = RED                                               # иначе ставим красный!
                    cards[i].fill()                                                        # не забываем каждую карточку заполнить изменённым цветом!


    pg.display.update()
    clock.tick(40)                                                                  # не забываем обновлять экран и установить кол-во кадров в секунду (fps)
