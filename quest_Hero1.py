from time import sleep

# создаём класс для наших персонажей
class Character():
    def __init__(self, name, health, armor, power, weapon):             # def __init__ - это специальный блок конструктор, в котором мы
        self.name = name                                                # задаём все СВОЙСТВА (данные) о нашем персонаже при его создании.
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon

    def print_info(self):                                               # это МЕТОД класса, т.е. то, что будет уметь делать каждый персонаж класса.
        print('Имя:', self.name)                                        # конкретно здесь мы печатаем все свойства персонажа
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила удара:', self.power)
        print('Оружие:', self.weapon, '\n')

    def strike(self, enemy):                                            # это МЕТОД класса, означающий удар персонажа по своему противнику
        print(f'-> УДАР! {self.name} атакует {enemy.name} с силой {self.power}, используя {self.weapon}\n')
        enemy.armor -= self.power                                       # f перед кавычками и переменные в фигурных скобках позволяют удобнее вставлять данные
        if enemy.armor < 0:
            enemy.health += enemy.armor                                 # здесь мы бьём противника по броне, и если она упала ниже 0, то прибавляем получившееся (например, -5) к здоровью. 15 + -5 = 10, например
            enemy.armor = 0
        print(f'{enemy.name} покачнулся(-ась).\nКласс брони упал до {enemy.armor}, а уровень здоровья до {enemy.health}\n')

    def fight(self, enemy):                                             # это МЕТОД класса, противники бьют друг друга, пока у одного из них есть здоровье
        while self.health > 0 and enemy.health > 0:
            self.strike(enemy)                                          # у нас уже есть метод для самого удара - используем его
            if enemy.health <= 0:
                print(enemy.name, 'пал в этом нелегком бою!\n')
                break
            sleep(2)                                                    # sleep расставляем для красоты. Не забудьте импортировать time в обоих программах!

            enemy.strike(self)
            if self.health <= 0:
                print(self.name, 'пал в этом нелегком бою!\n')
                break        
            sleep(2)



''' ВНИМАНИЕ! Класс мы описываем в одном проекте, сохраняем его, а во втором импортируем класс, создаём персонажей и прописываем игру!!! '''
''' Ниже начинается ПРИМЕР такой программы, но вы должны делать это в отдельном проекте :) '''



from quest_Hero1 import Character
from time import sleep


knight = Character('Ричард', 50, 25, 20, 'меч')                         # создаём персонажей и задаём им все необходимые свойства, их мы прописали в конструкторе
                                                                        # (name, health, armor, power, weapon). Под self здесь подставится сама переменная, которую вы назначили (у меня, например, knight)


# Дальше начинается сама игра. Включите воображение! Сделайте разные разветвления, усиления персонажа, битву с боссом и что угодно ещё. 
# ВСЁ на ваш вкус :) 
# Вы можете использовать и другие модули, например, random, чтобы сгенерировать случайные числа, или что угодно ещё.

print('Средиземье в опасности! На помощь спешит доблестный рыцарь...')
knight.print_info()                                                     # всегда, когда появляется персонаж, печатайте информацию о нём

sleep(4)
print(knight.name + ' идёт по лесу. Вдруг видит на пути мелкого воришку...')

sleep(4)
bandit = Character('Разбойник', 20, 5, 5, 'нож')
bandit.print_info()

sleep(2)
if input('Сразиться? (да/нет) >>') == 'да':                             # у меня механика простая - человек может согласиться на битву с разбойником или отказаться.
    print('\nДА НАЧНЁТСЯ БИТВА!\n')                                     # если соглашается, то начинается бой, 
    sleep(2)                                                            
    knight.fight(bandit)

    sleep(2)
    if knight.health > 0:
        knight.health = 50
        knight.power *= 2
        knight.armor *= 2
        print(f'\n{knight.name} восстановил силы и стал опытнее. Теперь сила его удара: {knight.power}, а класс брони: {knight.armor}\n')


sleep(2)
print('\nНаконец-то ' + knight.name + ' добирается до подземелья!')
dragon = Character('Дракон', 100, 25, 10, 'пламя')
dragon.print_info()

print('\nДА НАЧНЁТСЯ БИТВА!\n')
sleep(4)
knight.fight(dragon)
