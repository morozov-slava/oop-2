from abc import ABC, abstractmethod

# Абстрактный класс (интерфейс) для взаимодействия с базой данных с помощью Python
class DatabaseHandler(ABC):
	def __init__(self, host: str, port: int):
		self.host = host
		self.port = port

	@abstractmethod
	def select(self, query: str):
		# Метод для отправки произвольного SELECT-запроса в БД
		raise NotImplementedError("Method must be defined in child class")
    

# Дочерний класс (конкретная реализация) класса для взаимодействия с БД PostgreSQL
class PostgreHandler(DatabaseHandler):
	def __init__(self, host: str, port: int):
		super().__init__(host, port)

	def select(self, query: str):
		# Здесь предполагается реализация функционала для отправки SELECT-запроса
		# в БД PostgreSQL
		pass


# Функция, которая выгружает из базы данных список всех новых абонентов
# В рамках этой реализации применяется динамическое связывание, т.к. на
# вход ожидается экземляр объекта, который будет производить манипуляции с БД,
# и внутри данной функции для экземпляра будет вызываться метод select.
# Соответственно, в случае миграции таблиц в другую базу с сохранением структуры
# таблиц, достаточно будет реализовать и передать на вход этой функции 
# соответствующий объект, реализующий взаимодействие с другой базой 
# (например MySqlHandler, ClickHouseHandler и т.п.)
def get_all_new_clients(database_handler):
	query = """
			SELECT 
				ClntId,
				PhoneNumber,
				Age
			FROM
				all_clients
			WHERE
				RegistrationDate >= CURRENT_DATE - INTERVAL '30 days'
			"""
	df_all_new_clients = database_handler.select(query)
	return df_all_new_clients

# Пример:
postgre_handler = PostgreHandler(host, port)
df_all_new_clients = get_all_new_clients(postgre_handler)


