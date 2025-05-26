from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, attack, defense):
        self.name = name  # Ім'я персонажа
        self.hp = 100  # Початкове значення HP
        self.attack = attack  # Сила атаки
        self.defense = defense  # Сила захисту

    @abstractmethod
    def special_ability(self):
        pass

    def take_damage(self, damage):

        actual_damage = max(damage - self.defense, 0)
        self.hp -= actual_damage
        self.hp = max(self.hp, 0)

    def attack_character(self, target):
        print(f"{self.name} атакує {target.name}!")
        target.take_damage(self.attack)

    def __str__(self):
        return f"Ім'я: {self.name}, HP: {self.hp}, Атака: {self.attack}, Захист: {self.defense}"


class Elf(Character):
    def special_ability(self):
        print(f"{self.name} використовує стрілу! (+10 до атаки)")
        self.attack += 10

    def use_arrow(self, target):
        print(f"{self.name} стріляє стрілою у {target.name}! (50 шкоди)")
        target.take_damage(50)

class Orc(Character):
    def special_ability(self):
        print(f"{self.name} піднімає щит! (+15 до захисту)")
        self.defense += 15

# Створення персонажів
character1 = Elf("Леголас", 30, 10)
character2 = Orc("Орк", 25, 15)

# Демонстрація
print(character1)
print(character2)

character1.attack_character(character2)

character1.use_arrow(character2)  # Використання стріли
character2.special_ability()  # Використання спеціальної здібності
character2.attack_character(character1)

print(character1)
print(character2)