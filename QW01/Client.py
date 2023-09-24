import random as rm
from CDesks.Balance import Balance
from CDesks.Name import Name

class Client:
    Name = Name()
    Balance = Balance()
    
    def __init__(self, name, balance):
        self.Name = name
        self.Balance = balance

    def __str__(self):
        return f"""
Name - {self.Name}
Balance - {self.Balance}$
"""

    def gIter(self):
        return [self.Name, self.Balance]


