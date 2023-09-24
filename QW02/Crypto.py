import random as rm
import csv
import os, os.path

from CDesks.Name import Name
from CDesks.USD import USD
from CDesks.Help import HELP

class Crypto:
    Name = Name()
    USD = USD()
    Help = HELP()

    def __init__(self):
        self.Name = "@"
        self.wallets = {}
        self.__costs = {}

    def add(self, name, balance):
        while True:
            if self.Name == "@":
                self.Name = input("Enter client name >>> ")
            if self.Name != "@":
                break
        self.wallets[name] = balance
        self.__costs[name] = float(rm.randint(1, 5000) / 1000)  # додання доларової вартості
        tvar = self.USD  # оновлення доларової вартості

    def __sort(self):
        tvar = self.USD  # оновлення доларової вартості
        out = [(k, self.wallets[k], self.__costs[k]) for k in self.wallets]
        for i in range(len(out)):
            checked = True
            for j in range(len(out)):
                if checked:
                    continue
                if out[i][2] > out[j][2]:
                    out[i], out[j] = out[j], out[i]
                    checked = False
        return out

    def __str__(self):
        if len(self.wallets) == 0:
            return "Wallets is empty!"
        tout = self.__sort()
        out = ""
        out += f"Client name - {self.Name}\n"
        for i in tout:
            out += f"Name: {i[0]}, Count: {i[1]}, USD: {i[2]}\n"
        return out

    def Clear(self):
        self.__costs = {}
        self.wallets = {}
        self.Name = "@"

    def Saver(self):
        try:
            with open(self.Name+".csv", 'w', newline='') as f:
                csv.writer(f).writerows(self.__sort())
                print(f"Client {self.Name}.csv saved")
        except Exception as e:
            print(e)

    def Loader(self, name):
        if os.path.exists(name+".csv"):
            try:
                with open(name+".csv", 'r', newline='') as f:
                    self.Clear()
                    rdr = csv.reader(f)
                    self.Name = name
                    for ll in rdr:
                        self.add(ll[0], int(ll[1]))
                    print(f"Client {self.Name}.csv loaded")
            except Exception as e:
                print(e)
        else:
            print("Client not fount!")


    def Info(self, name=None, portf=None):
        if name is None and portf is None:
            print(self.Help)
        elif portf is not None and name is None:
            print(self.__str__())
        else:
            if name in list(self.wallets):
                print(f"""
Portfolio: {self.Name}
Wallet name: {name}
Count {name}s: {self.wallets[name]}
USD cost: {self.__costs[name]}
USD count: {self.USD[name]}               
                """)
            else:
                print("Wallet not found!")

    def Interface(self):
        print(self.Help)
        while True:
            cmd = input("Enter Command >>> ")
            if cmd.isdigit():
                cmd = int(cmd)
                if cmd == 0:
                    self.Info()
                elif cmd == 1:
                    self.Info(portf=0)
                elif cmd == 2:
                    self.Info(input("Enter wallet name >>> "))
                elif cmd == 3:  # add wallet
                    name = input("\tEnter wallet Name >>> ")
                    balance = 0
                    while True:
                        balance = input("\tEnter wallet count >>> ")
                        if balance.isdigit():
                            balance = int(balance)
                            break
                        print("Count must be digit!")
                    self.add(name, balance)
                elif cmd == 4:  # delete wallet
                    name = input("\tEnter wallet Name >>> ")
                    if not (name in list(self.wallets)):
                        print("Wallet not found!")
                        continue
                    else:
                        del self.wallets[name]
                        del self.__costs[name]
                        print(f"Wallet {name} deleted")

                elif cmd == 5:  # Loader
                    self.Loader(input("Enter client name >>> "))

                elif cmd == 6:  # Save
                    self.Saver()

                elif cmd == 7:
                    self.Clear()
                    print(f"Cleared")

                elif cmd == 8:
                    self.Name = input("Enter client name: ")

                elif cmd == 9:
                    name = input("Enter client name: ")
                    if os.path.exists(name + ".csv"):
                        os.remove(name+".csv")
                        print(f"Client {name}.csv deleted")
                    else:
                        print("Client not found!")

                elif cmd == 10:
                    break

                else:
                    print("Unknown command!\n Enter digit 1-10")
            else:
                print("Command must be digit!")


def main():
    c1 = Crypto()
    c1.Interface()


if __name__ == "__main__":
    main()
