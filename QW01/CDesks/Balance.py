class Balance:
    def __get__(self, instance, owner):
        return instance.__dict__["Balance"]

    def __set__(self, instance, value):
        if isinstance(value, int):
            instance.__dict__["Balance"] = value
        else:
            print("Client Balance Error!")