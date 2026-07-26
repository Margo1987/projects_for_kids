from random import randint
import pygame as pg                                                             # подключаем все нужны модули (as имя - мы можем дать библиотеке своё название)
pg.init()

BACK = (128, 128, 128)
COLR = (208, 208, 208)                                                          # создаём для цветов переменную и содержимое кладём в скобки, как единое целое

mw = pg.display.set_mode((500, 500))
mw.fill(BACK)                                                                   # создаём экран и размером 500 на 500 и заливаем его цветом

clock = pg.time.Clock()                                                         # это таймер для отсчёта fps (сколько кадров игры в секунду)

class TextArea():                                                               # класс для прямоугольников с надписью
    def __init__(self, x, y, weidth, heigth, color):
        self.rect = pg.Rect(x, y, weidth, heigth)
        self.fill_color = color                                                 # прямоугольник в месте x y со сторонами weidth heigth и цветом заливки color
        self.spisok = list()                                                    # НОВОЕ! Создаём список как свойство объекта                                                          


    def set_text(self, num, fsize, color=BACK):                                 # ВНИМАТЕЛЬНО! Теперь за место текста передаём num - это будет индекс                                        
        self.image = pg.font.Font(None, fsize).render(self.spisok[num], True, color)
                                                    # и здесь ^ тоже мы теперь запрашиваем индекс num из списка spisok объекта self

    def draw(self, sh_x, sh_y):                                                 # отрисовка самой карточки draw.rect и текста blit;
        pg.draw.rect(mw, self.fill_color, self.rect)                            # sh_x и sh_y - это отсупы от верхнего левого угла карточки
        mw.blit(self.image, (self.rect.x + sh_x, self.rect.y + sh_y))           # для того, чтобы красиво расположить текст

q_card = TextArea(120, 100, 290, 70, COLR)                                      
q_card.spisok = ['ВОПРОС', 'Твой суженый:', 'Как тебя зовут?', 'Ты сегодня ел:'] # создаём списки для вопросов и аналогично для ответов
q_card.set_text(0, 45)                                                          # ВНИМАТЕЛЬНО! В set_text мы теперь передаём НОМЕР нужного текста!

a_card = TextArea(120, 240, 290, 70, COLR)
a_card.spisok = ['ОТВЕТ', 'Кошка', 'Репэр', 'Джотаро']
a_card.set_text(0, 45)                                                          # создаём карточки для вопроса и для ответа         

while True:                                                                     # Игровой цикл!

    for event in pg.event.get():                                        # отслеживаем все события внешнего мира...
        if event.type == pg.KEYDOWN:                                        # если тип события это нажатая клавиша...

            if event.key == pg.K_q:                                             # если эта клавиша это клавиша Q...
                num = randint(1, len(q_card.spisok)-1)                              # то генерируем рандомное число от 1 до последнего индекса!
                q_card.set_text(num, 45)                                            # у последнего индекса номер - это длина всего списка минус 1 (то есть в списке 5 объектов, len возвращает нам количество, то есть как раз 5, а индексы начинаются с нуля, значит порядок такой: 0, 1, 2, 3, 4. И значит последний индекс, который нам нужен, находится под цифрой 4, то есть длина списка минус 1)

            if event.key == pg.K_a:
                num = randint(1, len(a_card.spisok)-1)
                a_card.set_text(num, 45)                                            # и передаём получившийся номер в set_text для установки текста                                      


    q_card.draw(25, 20)
    a_card.draw(25, 20)                                                         # ОБЯЗАТЕЛЬНО отрисовываем обе карточки!

    pg.display.update()                                                         # обновляем содержимое экрана
    clock.tick(40)                                                              # и устанавливаем 40 кадров в секунду!

