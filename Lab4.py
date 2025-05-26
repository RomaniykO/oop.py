# Патерн Composite - Кімнати та будівля
class Room:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        print(f"🛏️ Кімната: {self.name}")

class Building:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_details(self):
        print(f"🏢 Будівля: {self.name}")
        for room in self.rooms:
            room.show_details()

# Патерн Facade - Спрощення управління будівлею
class BuildingFacade:
    def __init__(self, building_name):
        self.building = Building(building_name)

    def add_room(self, room_name):
        self.building.add_room(Room(room_name))

    def show_building(self):
        self.building.show_details()

# ✅ Використання
house = BuildingFacade("Будинок")
house.add_room("Спальня")
house.add_room("Кухня")

print("\n🔍 Структура будівлі:")
house.show_building()