from abc import ABC, abstractmethod

# === Патерн Strategy: Різні режими освітлення ===
class LightMode(ABC):
    @abstractmethod
    def apply_mode(self):
        pass

class NormalMode(LightMode):
    def apply_mode(self):
        print("💡 Освітлення в звичайному режимі.")

class NightMode(LightMode):
    def apply_mode(self):
        print("🌙 Освітлення в нічному режимі.")

class EcoMode(LightMode):
    def apply_mode(self):
        print("🔋 Освітлення в енергозберігаючому режимі.")

# === Патерн State: Стан лампи ===
class LightState(ABC):
    @abstractmethod
    def handle(self, light):
        pass

class LightOn(LightState):
    def handle(self, light):
        print("✅ Лампа увімкнена.")

class LightOff(LightState):
    def handle(self, light):
        print("❌ Лампа вимкнена.")

# === Клас Лампи з використанням Strategy та State ===
class SmartLight:
    def __init__(self):
        self.state = LightOff()  # Початковий стан - вимкнена
        self.mode = NormalMode()  # Початковий режим освітлення

    def set_mode(self, mode: LightMode):
        self.mode = mode  # Змінюємо режим освітлення

    def set_state(self, state: LightState):
        self.state = state  # Змінюємо стан лампи

    def operate(self):
        self.state.handle(self)  # Виконується стан лампи
        if isinstance(self.state, LightOn):  # Якщо лампа увімкнена, застосовується режим
            self.mode.apply_mode()

# ✅ Використання
lamp = SmartLight()
lamp.operate()  # Лампа вимкнена

lamp.set_state(LightOn())  # Увімкнути лампу
lamp.set_mode(NightMode())  # Установити нічний режим
lamp.operate()

lamp.set_mode(EcoMode())  # Змінити на енергозберігаючий режим
lamp.operate()