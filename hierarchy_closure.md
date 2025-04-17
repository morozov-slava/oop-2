Замыкание иерархии классов через класс `None` (для python выбрал `NoneType`), 
т.к. `None` - базовый объект языка.

```py
class General:
    def method(self):
        return "It's method of 'General' class"

class Any(General):
    def method(self):
        return "It's method of 'Any' class (child of 'General' class)"

class FirstAnyChild(Any):
    def method(self):
        return "First 'Any' child"

class SecondAnyChild(Any):
    def method(self):
        return "Second 'Any' child"

# Класс NoneType в данной иерархии - потомок всех конечных классов
class NoneType(FirstAnyChild, SecondAnyChild):
    def method(self):
        return "None value"
```

Полиморфное использование `Void`:

```py
class Void:
    def __init__(self, value):
        self.value = value

    def check_type(self):
        if isinstance(self.value, NoneType):
            raise AssertionError("It's NoneType object") 
        return self.value.method()
```
