class NonNegative:

    def __set__(self, instance, value):
        if value != int(value) or value <= 0:
            raise ValueError("Введите неотрицательное целое число")
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = NonNegative()
    width = NonNegative()

    thickness = 0.05
    weight = 25

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asphalt_mass(self):
        return round(self.length * self.width * self.thickness * self.weight) / 1000


a = Road(5000, 20)
print(f"Масса асфальта, необходимого для покрытия всего дорожного полотна равна {a.asphalt_mass()} т ")
