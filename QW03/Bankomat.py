import random as rm
import os, os.path
import csv

from Client import Client
from BDescs.Help import HELP

class Bankomat:

    Help = HELP()

    def __init__(self):
        self.moneys = rm.randint(100, 10000)
        self.clients = {}
        self.Loader()

    def add(self, name, pin, bal=None):
        self.clients[name] = Client(name, pin)
        if bal is not None:
            self.clients[name].balance = bal




    def Saver(self):
        try:
            with open("bnk.csv", 'w', newline='') as f:
                wtr = csv.writer(f)
                for k in self.clients:
                    wtr.writerow(self.clients[k].serialize())
                print(f"Client bnk.csv saved")
        except Exception as e:
            print(e)

    def Loader(self):
        if os.path.exists("bnk.csv"):
            try:
                with open("bnk.csv", 'r', newline='') as f:
                    rdr = csv.reader(f)
                    for ll in rdr:
                        self.add(ll[0], int(ll[2]), float(ll[1]))
                    print(f"bnk.csv loaded")
            except Exception as e:
                print(e)
        else:
            print("File not found!")

    def Interface(self):
        print(self.Help)
        while True:
            cmd = input("Enter Command >>> ")
            if cmd.isdigit():
                cmd = int(cmd)
                if cmd == 0:
                    print(self.Help)
                elif cmd == 1:
                    name = input("Enter your name >>> ")
                    if name in list(self.clients):
                        pin = input("\tEnter pin code (4 digit)>>> ")
                        if pin.isdigit() and len(pin) == 4:
                            if self.clients[name] == pin:
                                print(f"Balance is {self.clients[name].balance}$")
                            else:
                                print("Wrong pin code!!!")
                        else:
                            print("Pin Code must be 4 digit!")
                    else:
                        print("Client not found!")
                elif cmd == 2:
                    name = input("Enter your name >>> ")
                    if name in list(self.clients):
                        pin = input("\tEnter pin code (4 digit)>>> ")
                        if pin.isdigit() and len(pin) == 4:
                            if self.clients[name] == pin:
                                sum = input("Enter sum was you need >>> ")
                                if sum.isdigit():
                                    sum = float(sum)
                                    if sum < self.moneys:
                                        tu = self.clients[name].balance
                                        self.clients[name] -= float(sum)
                                        self.moneys -= (tu - self.clients[name].balance)
                                    else:
                                        print("Error\nBankomat don`t have cash!")
                            else:
                                print("Wrong pin code!!!")
                        else:
                            print("Pin Code must be 4 digit!")
                    self.Saver()
                elif cmd == 3:  # register client
                    name = input("\tEnter Client Name >>> ")
                    if name in list(self.clients):
                        print("Error client registered!")
                    else:
                        pin = 0
                        while True:
                            pin = input("\tEnter pin code (4 digit)>>> ")
                            if pin.isdigit() and len(pin) == 4:
                                break
                            print("Pin Code must be 4 digit!")
                        self.add(name, pin)
                        self.Saver()

                elif cmd == 10:
                    break
                else:
                    print("Unknown command!\n Enter digit 1-10")
            else:
                print("Command must be digit!")


def main():
    c1 = Bankomat()
    c1.Interface()


if __name__ == "__main__":
    main()
