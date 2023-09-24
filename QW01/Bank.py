import random as rm
import os, os.path
import csv
from Client import Client


class Bank:
    def __init__(self):
        self.__clients = []

    def add(self, name, balance=rm.randint(0, 1000)):
        self.__clients.append(Client(name, balance))

    def find(self, name, typ=False):
        for cn in range(len(self.__clients)):
            if self.__clients[cn].Name == name:
                return self.__clients[cn] if not typ else cn

    def change(self, name, newName=None, balance=None):
        ct = self.find(name)
        if isinstance(ct, Client):
            if isinstance(newName, str):
                ct.Name = newName
            if isinstance(balance, int):
                ct.Balance = balance
        else:
            print("Client Not Found!")

    def clear(self):
        self.__clients = []

    def delete(self, name):
        data = self.find(name, True)
        if isinstance(data, int):
            del self.__clients[data]
        else:
            print("Client Not Found!")

    def Info(self, name=None):
        if isinstance(name, str):
            data = self.find(name)
            print(data if isinstance(data, Client) else "Client Not Found!")
        else:
            if not len(self.__clients):
                print("No Clients!")
            for cs in self.__clients:
                print(cs.Name)

    def save(self, fName: str):
        try:
            if ".csv" in fName and not fName.endswith(".csv"):
                fName = fName[:fName.find(".csv")+4]
            if not fName.endswith(".csv"):
                fName = fName + ".csv"
            with open(os.path.normpath(fName), 'w', newline='') as f:
                cw = csv.writer(f)
                for cs in self.__clients:
                    cw.writerow(cs.gIter())

        except IOError as e:
            print(e)

    def load(self, fName: str):
        try:
            self.clear()
            if ".csv" in fName and not fName.endswith(".csv"):
                fName = fName[:fName.find(".csv")+4]
            if not fName.endswith(".csv"):
                fName = fName + ".csv"
            if not os.path.exists(os.path.normpath(fName)):
                raise IOError("File Not found!")
            with open(os.path.normpath(fName), 'r', newline='') as f:
                cw = csv.reader(f)
                for cs in cw:
                    name, balance = cs
                    self.add(name, int(balance))
        except IOError as e:
            print(e)

    def Interface(self):
        print("\t\tBANK")
        while True:
            print("""
1. List Clients
2. Client info
3. Add client
4. Delete client
5. Change client name
6. Change client balance
7. Clear database
8. Load database (loader before load automatic deleting all clients)
9. Save database
10. Exit
            
""")
            cmd = input("Enter Command >>> ")
            if cmd.isdigit():
                cmd = int(cmd)
                if cmd == 1:
                    self.Info()
                elif cmd == 2:
                    self.Info(input("\tEnter Client Name >>> "))
                elif cmd == 3:
                    name = input("\tEnter Client Name >>> ")
                    balance = 0
                    while True:
                        balance = input("\tEnter Client Balance >>> ")
                        if balance.isdigit():
                            balance = int(balance)
                            break
                        print("Balance must be digit!")
                    self.add(name, balance)
                elif cmd == 4:
                    self.delete(input("\tEnter Client Name >>> "))
                elif cmd == 5:
                    name = input("\tEnter Client Name >>> ")
                    balance = 0
                    while True:
                        balance = input("\tEnter Client Balance >>> ")
                        if balance.isdigit():
                            balance = int(balance)
                            break
                        print("Balance must be digit!")
                    self.change(name, balance=balance)
                elif cmd == 6:
                    name = input("\tEnter Client Name >>> ")
                    nname = input("\tEnter New Client Name >>> ")
                    self.change(name, newName=nname)
                elif cmd == 7:
                    self.clear()
                elif cmd == 8:
                    self.load(input("\tEnter File Name >>> "))
                elif cmd == 9:
                    self.save(input("\tEnter File Name >>> "))
                elif cmd == 10:
                    break
                else:
                    print("Unknown command!\n Enter digit 1-10")
            else:
                print("Command must be digit!")




def Test():
    bk1 = Bank()
    bk1.Interface()
    # bk1.add("client1", 20)
    # bk1.add("client2")
    # bk1.add("client3", -50)
    # bk1.Info("client2")
    # bk1.change("client2", newName="client4", balance=711)
    # bk1.Info("client4")
    #
    # bk1.save("test.csv")
    # bk1.clear()
    # bk1.load("test")
    # bk1.Info()
    # bk1.Info("client3")
    # bk1.delete("teddy")
    # bk1.delete("client3")
    # bk1.Info()

if __name__ == "__main__":
    Test()
