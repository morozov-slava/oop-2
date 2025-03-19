## 1. Наследование:
# Класс 'Item' является базовым, а классы 'Armor' и 'HealingPotion' наследуются от него.
class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def use(self):
        raise NotImplementedError()
    
    def get_weight(self) -> float:
        return self.weight


# В классах 'Armor' и 'HealingPotion' реализуется своя логика работы метода 'use()'
class Armor(Item):
    def __init__(self, defense: float):
        super().__init__()
        self.defense = defense

    def use(self):
        return f"Вы надели броню '{self.name}', которая дает {self.defense} единиц защиты."


class HealingPotion(Item):
    def __init__(self, healing_amount):
        super().__init__()
        self.healing_amount = healing_amount

    def use(self):
        return f"Вы используете зелье {self.name}, восстанавливающее {self.healing_amount} единиц здоровья."


## 2. Полиморфизм:
# Мы создаем список предметов и вызываем метод 'use()' для каждого из них.

items = [
    Armor("Королевский шлем", 4.5, 50),
    HealingPotion("Зелье шамана", 0.1, 30)
]
for item in items:
    print(item.use())  # Для каждого объекта выполняется своя реализация метода `use()`


# 3. Композиция:
# Класс `Inventory` - объект для хранения предметов (Item). Он работает с объектами типа `Item`
class Inventory:
    def __init__(self, capacity: float):
        self.capacity = capacity
        self.items = {}
        self.current_weight = 0

    def add_item(self, item: Item) -> None:
        if self.current_weight + item.get_weight() > self.capacity:
            raise AssertionError("Not enough space in inventory to add new item")
        item_id = hash(item)
        self.items[item_id] = item # Добавляем предмет в инвентарь
        self.current_weight += item.get_weight()

    def drop_item(self, item: Item) -> None:
        item_id = hash(item)
        del self.items[item_id]
        self.current_weight -= item.get_weight()


# Инициализируем некоторые предметы для инвентаря
armor_1 = Armor("Королевский шлем", 4.5, 50)
hp_1 = HealingPotion("Зелье шамана", 0.1, 30)
# Создадим инвентарь и добавим в него несколько предметов (а затем что-то уберём)
inventory = Inventory()
inventory.add_item(armor_1)
inventory.add_item(hp_1)
inventory.drop_item(armor_1)


