class Dog(object):
    def __init__(self):
        print("----init方法-----")

    def __del__(self):
        print("----del方法-----")

    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls):  # cls此时是Dog指向的那个类对象

        # print(id(cls))
        # print(id(Dog))

        print("----new方法-----")
        return object.__new__(cls)
        # return object.__new__(Cat)


class Cat:
    pass


xtq = Dog()

print(type(xtq))
