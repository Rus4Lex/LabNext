import random as rm

from BDescs.Cash import Cash

class Client:
    balance = Cash()

    def __init__(self, name, pin):
        self.name = name
        self.__pin = pin
        self.__balance = rm.randint(5, 1000)

    def __eq__(self, other):
        return other == self.__pin

    def __isub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.balance -= other
            return self

    def serialize(self):
        return (self.name, self.__balance, self.__pin)