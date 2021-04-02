from random import random

from exceptions import EnemyDown, GameOver
from settings import PL

"""
models.py - class Enemy:
    свойства - level, lives.
    конструктор принимает уровень. Уровень жизней противнка = уровень противника.
    содержит два метода:
    Статический - select_attack(): возвращает случайное число от одного до трёх.
    decrease_lives(self): уменьшает количество жизней. Когда жизней становится 0 вызывает исключение EnemyDown.
"""


class Enemy:
    def __init__(self, level, lives):
        self.level = level
        self.lives = lives
        self.level = self.lives

    level = 1

    @staticmethod
    def select_attack():
        enemy_obj = random.randint(1, 3)
        return enemy_obj

    def decrease_lives(self):
        res = self.lives - 1
        if res == 0:
            return EnemyDown


"""
models.py - class Player:
    свойства: name, lives, score, allowed_attacks.
    конструктор принимает имя игрока. Количество жизней указывается из настроек. Счет равен нулю.
    методы: статический fight(attack, defense) - возвращает результат раунда \n
    - 0 если ничья, -1 если атака неуспешна, 1 если атака успешна.
    decrease_lives(self) - то же, что и Enemy.decrease_lives(), вызывает исключение GameOver.
    attack(self, enemy_obj) - получает ввод от пользователя (1, 2, 3),выбирает атаку противника из объекта enemy_obj;\n
    вызывает метод fight(); Если результат боя 0 - вывести "It's a draw!", если 1 = "You attacked successfully!"\n
    и уменьшает количество жизней противника на 1, если -1 = "You missed!"
    defence(self, enemy_obj) - то же самое, что и метод attack(), только в метод fight первым передается атака \n
    противника, и при удачной атаке противника вызывается метод decrease_lives игрока.
"""


class Player:
    def __init__(self, name, lives, score, allowed_attacks):
        self.name = name
        self.lives = lives
        self.score = score
        self.allowed_attacks = allowed_attacks

    score = 0
    lives = PL

    def attack(self, enemy_obj):
        self.fight(self.allowed_attacks, enemy_obj)
        if win == 0:
            print("It's a draw!")
        if win == 1:
            Enemy.decrease_lives()
            print("You attacked successfully!")
        if win == 2:
            print("You missed!")

    def defence(self, enemy_obj):
        self.fight(enemy_obj, self.allowed_attacks)
        if win == 0:
            print("It's a draw!")
        if win == 1:
            print("You attacked successfully!")
        if win == 2:
            Player.decrease_lives()
            print("You missed!")

    @staticmethod
    def fight(attack, defense):
        global win
        if attack == defense:
            win = 0
        if attack == 1 and defense == 2:
            win = 1
        if attack == 1 and defense == 3:
            win = 2
        if attack == 2 and defense == 1:
            win = 2
        if attack == 2 and defense == 3:
            win = 1
        if attack == 3 and defense == 1:
            win = 1
        if attack == 3 and defense == 2:
            win = 2
        return win

    def decrease_lives(self):
        res = self.lives - 1
        if res == 0:
            return GameOver