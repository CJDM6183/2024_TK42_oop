class JapaneseCar:
    def __init__(self, brand, model, year, price):
        self.brand = brand        # Бренд авто (наприклад, Toyota, Honda)
        self.model = model        # Модель авто (наприклад, Corolla, Civic)
        self.year = year          # Рік випуску
        self.price = price        # Ціна

    @property
    def info(self):
        """Метод для виведення інформації про автомобіль"""
        return f"{self.brand} {self.model}, {self.year}, Ціна: ${self.price}"

    @info.setter
    def info(self, new_price):
        """Метод для зміни ціни автомобіля"""
        if new_price > 0:
            self.price = new_price
        else:
            print("Ціна повинна бути більше 0")

class SportCar(JapaneseCar):
    def __init__(self, brand, model, year, price, horsepower):
        super().__init__(brand, model, year, price)
        self.horsepower = 201  # Потужність двигуна в кінських силах

    @property
    def info(self):
        return f"{self.brand} {self.model}, {self.year}, Потужність: {self.horsepower} к.с., Ціна: ${self.price}"
# Створимо об'єкт класу JapaneseCar
car1 = JapaneseCar("Toyota", "Corolla", 1983, 10000)
print(car1.info)  # Виведе: Toyota Corolla, 2022, Ціна: $20000

# Змінимо ціну
car1.info = 21000
print(car1.info)  # Виведе: Toyota Corolla, 2022, Ціна: $21000

# Створимо об'єкт класу SportCar
car2 = SportCar("Nissan", "GTR", 2021, 90000, 658)
print(car2.info)  # Виведе: Nissan GTR, 2021, Потужність: 565 к.с., Ціна: $90000
