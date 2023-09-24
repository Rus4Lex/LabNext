import random as rm
class USD:

    def __get__(self, obj, owner):
        tout = obj.__dict__["wallets"].copy()
        tset = obj.__dict__["_Crypto__costs"]
        for k in tout:
            tset[k] += float(rm.randint(-100,100)/10000)  # симуляція валютного коливання
            if tset[k] < 0.0001:
                tset[k] = 0.0001
            tout[k] *= tset[k]
        return tout

