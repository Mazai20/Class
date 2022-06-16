class Custuners:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}". {self.city}. Баланс: {self.balance} руб.'''

    def get_guest(self):
        return f'''"{self.name}' , {self.surname}" , {self.city}'''


custuner_1 = Custuners("Иван", "Петров", "Москва", 50)
custuner_2 = Custuners("Андрей", "Чикчирик", "Самара", 40)
custuner_3 = Custuners("Макс", "Максимов", "Киров", 25)
custuner_4 = Custuners("Александр", "Евлампиев", "Казань", 20)
custuner_5 = Custuners("Андрей", "Савин", "Нижний-Новгород", 40)

get_list = [custuner_1, custuner_2, custuner_3, custuner_4, custuner_5]

for guest in get_list:
    print(guest.get_guest())
