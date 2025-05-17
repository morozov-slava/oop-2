**Наследование с функциональной вариацией (Functional Variation Inheritance)**

Пример:

```py
class LossFunction:
	def calculate(self, y_true: np.array, y_pred: np.array):
		pass


class MeanSquaredError(LossFunction)
	def calculate(self, y_true: np.array, y_pred: np.array):
		return np.mean((y_true - y_pred)**2)
```

Здесь метод `calculate` переопределён в классе `MeanSquaredError` c сохранением сигнатуры.
Фактически, здесь происходит только изменение формулы расчёта для некоторой функции потерь.


**Наследование с вариацией типа (Type Variation Inheritance)**

Пример:

```py
class LogisticRegression:
    def predict(self, x):
	    pass

class LogisticRegressionWithThreshold(LogisticRegression):
    def predict(self, x, thr: float):
	    pass
```

Здесь метод `predict` переопределён в классе `LogisticRegressionWithThreshold`, c изменением его сигнатуры (добавляется аргумент `thr`).


**Наследование с конкретизацией (Reification Inheritance)**

Пример:

```py
from abc import ABC, abstractmethod


class User(ABC):
	@abstractmethod
	def authorize(self):
		pass


class AdminUser(User):
	def authorize(self):
		pass


class DefaultUser(User):
	def authorize(self):
		pass
```

Здесь `User` — абстрактный класс с абстрактным методом `authorize`, который должен быть реализован в дочерних классах `AdminUser` и `DefaultUser`.


**Структурное наследование (Structure Inheritance)**

Пример:

```py

class Document:
    def __init__(self, text):
        self.text = text


class DatabaseExportable:
    def export(self):
	    pass


class Report(Document, PdfExportable):
    def __init__(self, text):
        super().__init__(text)
```

Здесь класс `DatabaseExportable` добавляет функционал возможности экспорта некоторого документа в формат PDF на базе метода `export`.


