import copy

# Клас Рослини з методом клонування (Prototype)
class Plant:
    def __init__(self, species, height):
        self.species = species  # Вид рослини
        self.height = height  # Висота рослини

    def grow(self, amount):
        self.height += amount  # Рослина росте

    def clone(self):
        return copy.deepcopy(self)  # Глибоке копіювання

    def show_info(self):
        print(f"🌱 Вид: {self.species}, Висота: {self.height} см")

# ✅ Використання
original_plant = Plant("Бамбук", 100)
original_plant.show_info()

# Створення клонів
cloned_plant = original_plant.clone()
cloned_plant.grow(20)  # Клон виростає на 20 см
cloned_plant.show_info()