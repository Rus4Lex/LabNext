

class Cash:
    def __get__(self, instance, owner):
        return instance.__dict__["_Client__balance"]

    def __set__(self, instance, value):
        if value < 0:
            print("operation denied!\nLow balance.")
        else:
            instance.__dict__["_Client__balance"] = value