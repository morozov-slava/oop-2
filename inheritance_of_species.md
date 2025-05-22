Реализуем пайплайн обучения некоторой модели кредитного скоринга `CreditScoringPipeline`.
Пусть в рамках данного пайплайна будут реализованы следующие процедуры:
- Предобработка данных (реализована в рамках иерархии `FeaturesDataPreprocessor`)
- Построение модели (реализовано в рамках иерархии `BaseClassificationModel`)
- Оценка качества модели (реализовано в рамках иерархии `BaseClassificationLossFunc`)

```py
from abc import ABC, abstractmethod

import numpy as np
import pandas as pd


# 1-я иерархия классов: модель классификации
class BaseClassificationModel(ABC):
	def __init__(self):
		self.model = None

	@abstractmethod
	def fit(self, X_train: np.array, y_train: np.array):
		raise NotImplementedError("This method must be implemented in child class")

	@abstractmethod
	def predict(self, X: np.array):
		raise NotImplementedError("This method must be implemented in child class")


class LogisticRegression(BaseClassificationModel):
	def __init__(self):
        super().__init__()

	def fit(self, X_train: np.array, y_train: np.array):
		raise NotImplementedError("This method must be implemented in child class")

	def predict(self, X: np.array):
		raise NotImplementedError("This method must be implemented in child class")


# 2-я иерархия классов: функции ошибки модели классификации
class BaseClassificationLossFunc(ABC):
	@abstractmethod
	def calculate(self, y_true: np.array, y_pred: np.array):
		raise NotImplementedError("This method must be implemented in child class")


class PrecisionLossFunc(BaseClassificationLossFunc):
	@abstractmethod
	def calculate(self, y_true: np.array, y_pred: np.array):
		pass


class AccuracyLossFunc(BaseClassificationLossFunc):
	@abstractmethod
	def calculate(self, y_true: np.array, y_pred: np.array):
		pass


# 3-я иерархия классов: класс обработки данных
class FeaturesDataPreprocessor(ABC):

	@abstractmethod
	def preprocess(self, array: np.array):
		raise NotImplementedError("This method must be implemented in child class")


class CreditScoringFeaturesPreprocessor(FeaturesDataPreprocessor):  
	def preprocess(self, array: np.array):
		pass



# Основной класс, реализующий наследование вида
class CreditScoringPipeline:
	def __init__(self, 
		data_preprocessor: 
		model: BaseClassificationModel, 
		loss_func: BaseClassificationLossFunc
	):
		self.data_preprocessor = data_preprocessor
		self.model = model
		self.loss_func = loss_func
		# Result parameters
		self.fitted_model = None
		self.train_loss = None
		self.test_loss = None

	def run(self, X_train: np.array, y_train: np.array, 
				  X_test: np.array, y_test: np.array
			):
		# Data preprocessing
		X_train_processed = self.data_preprocessor.preprocess(X_train)
		X_test_processed = self.data_preprocessor.preprocess(X_test)
		# Fit model
		self.model.fit(X_train_processed, y_train)
		self.fitted_model = self.model
		# Model evaluation (train)
		y_pred_train = self.model.predict(X_train_processed)
		self.train_loss = loss_func.calculate(y_train, y_pred_train)
		# Model evaluation (test)
		y_pred_test = self.model.predict(X_test_processed)
		self.test_loss = loss_func.calculate(y_test, y_pred_test)

	# Additional methods
	def get_fitted_model(self):
		return self.fitted_model

	def get_train_loss(self):
		return self.train_loss

	def get_test_loss(self):
		return self.test_loss
```
