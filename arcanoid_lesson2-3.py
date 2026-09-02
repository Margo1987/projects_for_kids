import pygame as pg
pg.init()                                                                           # импорт нужных модулей, подключаем возможности pygame в браузер

mw = pg.display.set_mode((500, 500))                                                # создаём окно размером 500 на 500 
back = pg.transform.scale(pg.image.load('background.jpg'),(500,600))                # ВНИМАНИЕ!!! Вы ЛИБО ставите на фон картинку(строка 5), ЛИБО заполняете фон цветом (строка 6)
mw.fill((115, 115, 225))                                                            # или можно сначала цвет, а потом картинку, но важно - команды для этого разные!!!

clock = pg.time.Clock()                                                             # создаём таймер для фпс

class Area():
    def __init__(self, x, y, width, heigth):
        self.rect = pg.Rect(x, y, width, heigth)                                    # класс Area отвечает за невидимый прямоугольник (границы объектов, хитбоксы)
    def colliderect(self,rect):                                                     # метод colliderect проверяет, столкнулся ли хитбокс rect объекта self с другим объектом
        return self.rect.colliderect(rect)

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

move_right = False
move_left = False
move_x = 3
move_y = 3                                                                          # move_right/left - флаги для движения платформы, move_x/y - постоянное перемещение мяча


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
    mw.fill((115, 115, 225))                                                        # здесь ЛИБО заполняем экран цветом, ЛИБО отоброжаем картинку на фоне! Или и то, и другое именно в таком порядке. Команды разные!!!
    mw.blit(back, (0,0))
    ball.draw()
    platform.draw()                                                                 # отрисовываем мяч и платформу

    for enemy in enemys:
        enemy.draw()                                                                # через цикл отрисовываем врагов
        if enemy.rect.colliderect(ball.rect):                                       # если хитбокс врага столкнулся с хитбоксом мяча, то удаляем врага из списка 
            enemys.remove(enemy)                                                    # и меняем движение мяча на прямо противоположное
            move_y *= -1                                                            # ВАЖНО!!! Если вылезает ошибка, попробуйте за место enemy.rect.colliderect написать просто enemy.colliderect

    for event in pg.event.get():                                                    # получаем все события
        if event.type == pg.KEYDOWN:                                                # если НАЖАТА клавиша определённая, то меняем флаги на True 
            if event.key == pg.K_a:                                                 # - платформа продолжит движение, пока клавиша нажата
                move_left = True
            if event.key == pg.K_d:
                move_right = True
        elif event.type == pg.KEYUP:                                                # как только клавиша ОТПУЩЕНА, меняем флаги на False - платформа остановится
            if event.key == pg.K_a:
                move_left = False
            if event.key == pg.K_d:
                move_right = False

    if move_right and platform.rect.x <= 400:                                       # если флаг равен True и платформа не выходит за границу экрана, 
        platform.rect.x += 3                                                        # то она движется на 3 пикселя вправо/влево (меняем её координату x)
    if move_left and platform.rect.x > 0:
        platform.rect.x -= 3

    ball.rect.x += move_x                                                           # а мяч движется постоянно, без условий (меняем его координаты x и y)
    ball.rect.y += move_y

    if ball.rect.colliderect(platform.rect):                                        # если мяч соприкоснётся с платформой, то меняем его направление
        move_y *= -1                                                                # ВАЖНО!!! Если вылезает ошибка, попробуйте за место ball.rect.colliderect написать просто ball.colliderect
    if ball.rect.y < 0:
        move_y *= -1
    if ball.rect.x > 450 or ball.rect.x < 0:                                        # если координаты мяча выходят за верх, право или лево сцены, то меняем его направления
        move_x *= -1

    if ball.rect.y > 385:                                                           # УСЛОВИЕ ПРОИГРЫША - мяч улетел ниже координаты
        mw.fill((255, 0, 0))                                                        # аналогично предыдущему - ЛИБО заполняете экран цветом, либо ставите картинку проигрыша
        back = pg.transform.scale(pg.image.load('lose.jpg'), (500,600))
        mw.blit(back, (0,0))

        lose = Label(70, 200, 50, 50)                                              # создаёте ТЕКСТ для проигрыша и отрисовываете его
        lose.set_text('GAME OVER', 100)
        lose.draw()

        game = False                                                                # меняете флажочек игры на False и обновляете наполнение экрана
        pg.display.update()

    if len(enemys) == 0:                                                            # УСЛОВИЕ ВЫИГРЫША - список врагов пуст, значит врагов больше нет
        mw.fill((0, 255, 0))                                                        # аналогично предыдущему - ЛИБО заполняете экран цветом, либо ставите картинку выигрыша
        back = pg.transform.scale(pg.image.load('win.jpg'), (500,600))
        mw.blit(back, (0,0))

        win = Label(130, 200, 50, 50)                                               # создаёте ТЕКСТ для выигрыша и отрисовываете его
        win.set_text('YOU WIN!', 100)
        win.draw()

        game = False                                                                # меняете флажочек игры на False и обновляете наполнение экрана
        pg.display.update()


    pg.display.update()
    clock.tick(40)                                                                  # ОБЯЗАТЕЛЬНО обновляем экран и ставим фпс



