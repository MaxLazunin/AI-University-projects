import random

class Bag:

    total = 0
    keg_list = []

    def __init__(self):
        self.total = 90
        self.keg_list = list(i for i in range(1, 91))
        print('Игра началась')

    def get_keg(self):
        last_numbers = [0]
        number = 0
        while number in last_numbers:
            number = random.randint(1, 10)
            print(number)
        self.keg_list.remove(number)
        return number

if __name__ == '__main__':
    bag = Bag()
    bag.get_keg()