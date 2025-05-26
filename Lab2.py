# SRP - Клас Transport тільки містить базову інформацію
class Transport:
    def __init__(self, name):
        self.name = name

# OCP - Створимо базовий клас, який можна розширювати
class TransportCostCalculator:
    def calculate_cost(self, distance):
        pass

# Реалізуємо різні варіанти розрахунку вартості поїздки
class CarCostCalculator(TransportCostCalculator):
    def calculate_cost(self, distance):
        return distance * 5  # 5 грн за 1 км

class BusCostCalculator(TransportCostCalculator):
    def calculate_cost(self, distance):
        return distance * 2  # 2 грн за 1 км

class BicycleCostCalculator(TransportCostCalculator):
    def calculate_cost(self, distance):
        return 5  # Їзда на велосипеді безкоштовна 🚴

# Клас для визначення вартості поїздки
class Trip:
    def __init__(self, transport: Transport, cost_calculator: TransportCostCalculator, distance):
        self.transport = transport
        self.cost_calculator = cost_calculator
        self.distance = distance

    def get_trip_cost(self):
        cost = self.cost_calculator.calculate_cost(self.distance)
        print(f"Поїздка на {self.transport.name} коштує {cost} грн за {self.distance} км.")

# ✅ Використання
car = Transport("Автомобіль")
bus = Transport("Автобус")
bike = Transport("Велосипед")

car_trip = Trip(car, CarCostCalculator(), 10)
bus_trip = Trip(bus, BusCostCalculator(), 10)
bike_trip = Trip(bike, BicycleCostCalculator(), 10)

car_trip.get_trip_cost()  # Поїздка на Автомобілі коштує 50 грн
bus_trip.get_trip_cost()  # Поїздка на Автобусі коштує 20 грн
bike_trip.get_trip_cost()  # Поїздка на Велосипеді коштує 0 грн 🚴