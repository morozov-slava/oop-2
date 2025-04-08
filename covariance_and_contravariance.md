Ввиду того, что в Python утиная типизация, то отдельные механизмы для применения ковариантности и контравариантности не обязательны.

Но для более понятной и явной реализации можно использовать обобщённые типы (генерики), которые в Python можно применить через `TypeVar` объект.

**Пример ковариантности:**

```py
from typing import List, TypeVar, Generic

import pandas as pd


T = TypeVar('T', covariant=True) 


class PreprocessHandler(Generic[T]):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError("Метод run должен быть переопределён")


class FilterActiveClientsHandler(PreprocessHandler['FilterActiveClientsHandler']):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[df['is_active'] == 1]


class FilterHighRevenueHandler(PreprocessHandler['HighRevenueHandler']):
    def run(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[df['revenue'] >= 80000]


class PreprocessingPipeline:
	def __init__(self):
		self.pipeline = []

	def add(self, handler: T):
		self.pipeline.append(handler)

	def run(self, df: pd.DataFrame) -> pd.DataFrame:
		df_processed = df.copy()
		for handler in self.pipeline:
			df_processed = handler.run(df_processed)
		return df_processed

# Example:
pipeline = PreprocessingPipeline()
pipeline.add(FilterActiveClientsHandler())
pipeline.add(FilterHighRevenueHandler())
df_processed = pipeline.run(df)
```

**Пример контравариантности:**

```py
from typing import Callable, Generic, List, TypeVar, 


T = TypeVar('T', contravariant=True) 


class BinaryClassificationModel(Generic[T]):
	def __init__(self):
		self.model = None

	def fit(self):
		pass

	def predict(self):
		pass


class MultiClassClassificationModel:
	def __init__(self):
		self.model = None

	def fit(self):
		pass

	def predict(self):
		pass


class LogisticRegression(BinaryClassificationModel):
	def __init__(self):
		self.model = None

	def fit(self):
		pass

	def predict(self):
		pass


def train_binary_classification_model(
	model: Callable[BinaryClassificationModel, None],
	X_train,
	y_train
) -> None:
	model.fit()
	return model


def train_logistic_regression_model(
	model: Callable[LogisticRegression, None],
	X_train,
	y_train
) -> None:
	model.fit()
	return model


# Example
binary_classifier = BinaryClassificationModel()
log_reg = LogisticRegression()

train_binary_classification_model(log_reg)
train_binary_classification_model(binary_classifier)

```

