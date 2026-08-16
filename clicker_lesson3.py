from random import randint
from time import time
import pygame as pg                                                                 # импорт нужных модулей

pg.init()                                                                           # подключаем возможности pygame в браузер

YELLOW = (255, 255, 0)
BLUE = (80, 80, 255)
BACK = (200, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 51)

DARK_BLUE = (0, 0, 100)
LIGHT_GREEN = (200, 255, 200)
LIGHT_RED = (250, 128, 114)                                                         # для цветов лучше создать переменные заранее


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
time_text = Label(20, 20, 50, 50, BACK)
time_text.set_text('Время:', 40, DARK_BLUE)
time_text.draw(0,0)

timer = Label(50, 55, 50, 40, BACK)
timer.set_text('0', 40, DARK_BLUE)
timer.draw(0,0)


score_text = Label(400, 20, 50, 50, BACK)
score_text.set_text('Счёт:', 45, DARK_BLUE)
score_text.draw(0,0)

score = Label(430, 55, 50, 40, BACK)
score.set_text('0', 40, DARK_BLUE)
score.draw(0,0)


start = time()
points = 0

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
                        points += 1
                    else:
                        cards[i].color = RED                                               # иначе ставим красный!
                        points -= 1
                  cards[i].fill()                                                        # не забываем каждую карточку заполнить изменённым цветом!

                  score.set_text(str(points), 40, DARK_BLUE)
                  score.draw(0,0)

    now_time = time()
    timer.set_text(str(int(now_time - start)), 40, DARK_BLUE)
    timer.draw(0,0)


    if now_time - start  >= 11:
        win = Label(0, 0, 500, 500, LIGHT_RED)
        win.set_text("Время вышло!", 60, DARK_BLUE)
        win.draw(110, 180)
        break

    if points >= 5:
        win = Label(0, 0, 500, 500, LIGHT_GREEN)
        win.set_text("Ты победил!", 60, DARK_BLUE)
        win.draw(140, 180)

        result_time = Label(90, 230, 250, 250, LIGHT_GREEN)
        result_time.set_text(f"Время прохождения: {str(int(new_time - start))} сек", 40, DARK_BLUE)
        result_time.draw(0,0)
        break

    pg.display.update()
    clock.tick(40)                                                                  # не забываем обновлять экран и установить кол-во кадров в секунду (fps)

pg.display.update()

