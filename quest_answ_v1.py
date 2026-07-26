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

    def set_text(self, text, fsize, color=BACK):                                # метод set_text устанавливает и меняет текст карточки
        self.image = pg.font.Font(None, fsize).render(text, True, color)        # Font настраивает шрифт, .render применяет его на текст text

    def draw(self, sh_x, sh_y):                                                 # отрисовка самой карточки draw.rect и текста blit;
        pg.draw.rect(mw, self.fill_color, self.rect)                            # sh_x и sh_y - это отсупы от верхнего левого угла карточки
        mw.blit(self.image, (self.rect.x + sh_x, self.rect.y + sh_y))           # для того, чтобы красиво расположить текст

q_card = TextArea(120, 100, 290, 70, COLR)
q_card.set_text('Вопрос', 45)

a_card = TextArea(120, 240, 290, 70, COLR)
a_card.set_text('Ответ', 45)                                                    # создаём карточки для вопроса и для ответа

while True:                                                                     # Игровой цикл!

    for event in pg.event.get():                                        # отслеживаем все события внешнего мира...
        if event.type == pg.KEYDOWN:                                        # если тип события это нажатая клавиша...

            if event.key == pg.K_q:                                             # если эта клавиша это клавиша Q...
                num = randint(1, 3)                                                 # то генерируем рандомное число от 1 до 3
                if num == 1:
                    q_card.set_text('Твой суженый:', 45)
                if num == 2:
                    q_card.set_text('Как тебя зовут?', 45)                          # и в зависимости от числа устанавливаем текст в карточке вопроса
                if num == 3:
                    q_card.set_text('Ты сегодня ел:', 45)

            if event.key == pg.K_a:                                             # если эта клавиша это клавиша A...
                num = randint(1, 3)                                                 # то генерируем рандомное число от 1 до 3
                if num == 1:    
                    a_card.set_text('Кошка', 45)
                if num == 2:
                    a_card.set_text('Репэр', 45)                                    # и в зависимости от числа устанавливаем текст в карточке ответа
                if num == 3:                                                        # должно быть минимум 3 формулировки! 
                    a_card.set_text('Джотаро', 45)                                  # (но лучше не сильно много, на следующем уроке доработаем :)

    q_card.draw(25, 20)
    a_card.draw(25, 20)                                                         # ОБЯЗАТЕЛЬНО отрисовываем обе карточки!

    pg.display.update()                                                         # обновляем содержимое экрана
    clock.tick(40)                                                              # и устанавливаем 40 кадров в секунду!

