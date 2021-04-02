"""
game.py:
    Содержит блок на проверку имени модуля (main)
    внутри if блок try/except.
    try запускает функцию play()
    except обрабатывает два исключения: GameOver - выводит сообщение об ошибке, \n
    записывает результат в таблицу рекордов. KeyboardInterrupt - pass
    finally печатает "Good bye!"
"""
from models import Player


def play():
    pl_name = input('Input Your Name : ')
    name = Player(name=pl_name, lives=)


if __name__ == '__main__':
    try:
        play()

    except:



"""
game.py - play():\n"
    Ввод имени игрока\n"
    Создание объекта player\n"
    level = 1\n"
    Создание объекта enemy\n"
    в бесконечном цикле вызывает методы attack и defense объекта player\n"
    при возникновении исключения EnemyDown повышает уровень игры, создает новый объект Enemy с новым уровнем, \n"
    добавляет игроку +5 очков.\n")
"""