**Пример наследования реализации:**

```py
class Widget:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def move(self, dx: float, dy: float):
        self.x += dx
        self.y += dy

    def draw(self):
        print(f"Draw widget at ({self.x}, {self.y})")


class Button(Widget):
    def draw(self):
        print(f"Draw widget at ({self.x}, {self.y}) as button")
```

Класс `Button` использует реализацию перемещения и хранения координат из класса `Widget`, переопределяя лишь метод `draw()`.



**Пример льготного наследования:**

```py
class BaseStringValidator:
    def __init__(self, string):
        self.string = string
        self._is_valid = None

    def is_valid(self):
        if self._is_valid is None:
            raise NotImplementedError()
        return self._is_valid


class PasswordLengthValidator(BaseStringValidator):
    def __init__(self, string: str):
        super().__init__(string)
        self._is_valid = len(string) >= 12
```

Класс `BaseStringValidator` представляет базовый класс, которому на вход подаётся некоторый объект типа `string`, проверяемый в соответствии с некоторым правилом.
Класс `PasswordLengthValidator` представляет пример льготного наследования при котором происходит проверка некоторого объекта по некоторому правилу (в данному случае проверка на длину строки).
