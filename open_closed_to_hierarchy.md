В Python нет встроенной возможности для запрета переопределения методов в потомках напрямую.

Одно из возможных решений - это использование декоратора `@final`, который находится в модуле `typing`.
Декорированный метод класса отмечает как метод, который не подлежит переопределению.
Обнаружить в таком случае проблему может помочь анализатор кода (например, MyPy).

Пример:

```py
from typing import final

class Population:
    def __init__(self):
        self.population = 0

    @final
    def add_unit(self):
        return self.population += 1


class HumanPopulation(Population):
    # При попытке переопределить данный метод анализатор кода выдаст ошибку
    def add_unit(self):
        return self.population += 2
```


