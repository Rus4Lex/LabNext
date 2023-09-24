class Name:
    def __get__(self, instance, owner):
        return instance.__dict__["Name"]

    def __set__(self, instance, value):
        if isinstance(value, str) or (2 < len(value) <= 20):
            instance.__dict__["Name"] = value
        else:
            print("Client Name Error!")