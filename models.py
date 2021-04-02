from random import random

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

    @staticmethod
    def select_attack():
        return random.randint(1, 3)

    def decrease_lives(self):
        pass


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

    @staticmethod
    def fight(attack, defense):
        pass