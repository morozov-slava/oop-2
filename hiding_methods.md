Из 4-х вариантов скрытия методов в Python формально возможны только два, т.к. Python не поддерживает жёсткую систему доступа.
Это решается на уровне условных соглашений между разработчиками:

`public_method` - метод без нижних подчёркиваний (доступен на уровне пользователя)

`_protected_method` - метод с одним нижним подчёркиванием (соглашение о внутреннем использовании, но доступ при этом не ограничен)

`__private_method` - метод с двумя нижними подчёркиваниями (по сути метод переименовывается в `obj._MyClass__myPrivateMethod()`, но доступ к нему всё же возможен, хоть и затруднён)


1. Метод публичен в родительском классе A и публичен в потомке B.

Это обычное переопределение метода:

```py
class Parent:
    def method(self):
        print("Parent class")

class Child(Parent):
    def method(self):
        print("Child class")
```


3. Метод "скрыт" в родителе A и публичен в потомке B.

Да, ты можешь определить в родителе метод с двумя подчёркиваниями, а в потомке публичный:

```py
class Parent:
    def __method(self):
        print("Parent class")

class Child(Parent):
    def method(self):
        print("Child class")

child = Child()
child.method()  # вызовет Child.method()

# Но по факту к методу родительского класса можно обратиться следующей командой:
child._Parent__method()
```


4. Метод скрыт в родителе A и скрыт в потомке B

Можно определить "приватный" метод с двумя подчёркиваниями и в A, и в B, и это будут два разных метода:

```py
class Parent:
    def __method(self):
        print("Parent class")

class Child(Parent):
    def __method(self):
        print("Child class")

child = Child()
# В таком случае мы можем обратиться и к дочернему приватному методу и к родительскому:
child._Child__method() # вызовет Child.__method()
child._Parent__method() # вызовет Parent.__method()
```






