class TypedMeta(type):
    a = None

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super().__call__(*args, **kwargs)
            return cls.a
        return cls.a


class MyClass(metaclass=TypedMeta):

    def method_1(self):
        pass

    def method_2(self):
        pass


obj_1 = MyClass()
obj_2 = MyClass()

print(obj_1 is obj_2)
