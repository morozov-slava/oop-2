class Item:
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def use(self):
        raise NotImplementedError()

    def get_weight(self) -> float:
        return self.weight


# Расширение класса-родителя `Item`: для класса `Weapon` добавлен параметр урона оружия (damage)
# а также, соответственно, метод для отображения урона
class Weapon(Item):
    def __init__(self, damage: float):
        super().__init__()
        self.damage = damage

    def use(self):
        # Специализируем метод use для оружия: наносим урон.
        print(f"Использовано оружие {self.name}, которое наносит {self.damage} урона!")

    def get_damage(self) -> int:
        return self.damage


# Расширение и специализация класса-родителя `Item`: для класса `CursedItem` изменён родительский метод `get_weight`,
# а также добавлен новый аттрибут `power`                                
class CursedItem(Item):
    def __init__(self, power: int):
        super().__init__()
        self.power = power

    def get_weight(self) -> float:
        # Для проклятых предметов вес определяется по другой логике (в зависимости от мощи проклятого предмета)
        return self.weight * self.power * 0.10

    