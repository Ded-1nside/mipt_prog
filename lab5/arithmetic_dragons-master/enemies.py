# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def divs(num):
    divisors = []
    for i in range(1, num // 2):
        if num % i == 0:
            divisors.append(i)
    return divisors.sort()


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest


class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest


class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class SmallLOLTroll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 30
    
    def question(self):
        x = randint(1,5)
        self.__quest = "Угадай число от 1 до 5"
        self.set_answer(x)
        return self.__quest


class MediumTroll(Troll):
    def __init__(self):
        self._health = 500
        self._attack = 5
    
    def question(self):
        x = randint(1, 100)
        self.__quest = "Число" + str(x) + "простое?"
        self.set_answer(is_prime(x))
        return self.__quest


class BigTroll(Troll):
    def __init__(self):
        self._health = 300
        self._attack = 10
    
    def question(self):
        x = randint(1,100)
        self.__quest = "Разложите" + str(x) + "на множители и введите их в виде отс"
        self.set_answer(divs(x)) 
        return self.__quest
    
    def check_answer(self, answer):
        return self._answer == answer.split(',')
enemy_types = [GreenDragon, RedDragon, BlackDragon, SmallLOLTroll, MediumTroll, BigTroll]