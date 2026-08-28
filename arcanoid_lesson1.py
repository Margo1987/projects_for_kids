import pygame as pg
pg.init()                                                                           # импорт нужных модулей, подключаем возможности pygame в браузер

mw = pg.display.set_mode((500, 500))
mw.fill((115, 115, 225))

clock = pg.time.Clock()                                                             # создаём окно размером 500 на 500, заполняем цветом и создаём таймер для фпс

class Area():
    def __init__(self, x, y, width, heigth):
        self.rect = pg.Rect(x, y, width, heigth)                                    # класс Area отвечает за невидимый прямоугольник (границы объектов, хитбоксы)

class Label(Area):
    def set_text(self, text, fsize, color=(0, 0, 0)):
        self.image = pg.font.SysFont('verdana', fsize). render(text, True, color)
    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))                             # класс Label отвечает за текст на экране, он и Area уже были в предыдущих проектах

class Picture(Area):                                                                # класс Picture создаёт не только прямоугольник, но и картинку filename внутри него,
    def __init__(self, x, y, width, heigth, filename):
        super().__init__(x, y, width, heigth)
        self.image = pg.image.load(filename)

    def draw(self):                                                                 # а метод draw его отрисовывает.
        mw.blit(self.image, (self.rect.x, self.rect.y))

ball = Picture(230, 250, 50, 50, 'ball.png')
platform = Picture(200, 400, 100, 30, 'platform.png')                               # создаём объекты платформа и мяч как экземпляры класса Picture


enemys = list()                                                                     # врагов много - создадим их как список
enemy_x = 5
enemy_y = 5                                                                         # у первого врага будут координаты 5 и 5, остальных рассчитаем
n = 9                                                                               # в первом ряду n врагов, то есть 9, в последующих рядах будем уменьшать

for i in range(3):                                                                  # создаём 3 ряда
    x = enemy_x + 27*i                                                                  # каждый монстр следующего ряда будет смещаться по иксу на (начальное положение + (половина от размера картинки* i)), где i - число от 0 до 2, то есть номер ряда 
    y = enemy_y + 50*i                                                                  # каждый монстр следующего ряда будет смещаться по игрику на (начальное положение + (размер картинки* i)), где i - число от 0 до 2, то есть номер ряда
    for en in range(n):                                                             # в одном ряду по n врагов - создаём их в цикле
        monster = Picture(x, y, 50, 50, 'enemy.png')                                
        enemys.append(monster)                                                          #создаём, добавляем врага в список и меняем x для следующего в ряду врага
        x += 55                                                                         
    n -= 1                                                                          # уменьшаем кол-во врагов в ряду                                                                          



game = True                                                                         # создаём игровой цикл с помощью влажочка game
while game:
    ball.draw()
    platform.draw()                                                                 # отрисовываем мяч и платформу

    for enemy in enemys:
        enemy.draw()                                                                # через цикл отрисовываем врагов

    pg.display.update()
    clock.tick(40)                                                                  # ОБЯЗАТЕЛЬНО обновляем экран и ставим фпс
