import random


def decor(f):
    def inner(*args, **kwargs):
        print('-' * 45)
        res = f(*args, **kwargs)
        print('-' * 45)
        return res
    return inner


class Card:

    def __init__(self):
        self.numbers = []
        self.indexes = []
        self.card = [list(' ' * 20), list(' ' * 20), list(' ' * 20)]
        self.string_1 = []

    def __number_generator(self):
        numbers = set()

        while len(numbers) < 15:
            number = random.randint(1, 91)
            numbers.add(number)
        numbers = list(numbers)
        self.numbers.append(sorted(list(numbers[0:5])))
        self.numbers.append(sorted(list(numbers[5:10])))
        self.numbers.append(sorted(list(numbers[10:15])))

    def __string_generator(self):
        indexes = set()
        while len(indexes) < 5:
            number = random.randint(0, 19)
            indexes.add(number)
        self.indexes.append(list(indexes))

    def __card_form_generator(self):
        for i in range(3):
            self.__string_generator()

    @decor
    def card_generator(self):
        self.__card_form_generator()
        self.__number_generator()
        self.numbers = sorted(self.numbers)

        for i in range(3):
            for j in range(5):
                self.card[i][self.indexes[i][j]] = self.numbers[i][j]
        for i in range(3):
            my_str = ''
            for el in self.card[i]:
                my_str += str(el) + ' '
                self.card[i] = my_str
        print(self.card[0])
        print(self.card[1])
        print(self.card[2])


card = Card()
card.card_generator()
