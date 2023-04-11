class NonNegative:

    def __init__(self, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):
        if value != str(value):
            raise ValueError("Не может быть числом")
        instance.__dict__[self.my_attr] = value


class Worker:

    name = NonNegative('name')
    surname = NonNegative('surname')
    position = NonNegative('position')

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Worker("Иван", "Иванов", "программист", 20000, 50000)
print(f"{worker_1.get_full_name()} - {worker_1.position}: доход с учетом премии составляет "
      f"{float(worker_1.get_total_income())} рублей")

worker_2 = Worker("Петр", "Петров", "директор", 100000, 80000)
print(f"{worker_2.get_full_name()} - {worker_2.position}: доход с учетом премии составляет "
      f"{float(worker_2.get_total_income())} рублей")
