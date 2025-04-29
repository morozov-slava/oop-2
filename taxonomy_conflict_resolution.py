# Пример с добавлением атрибута `notification_type`
class Notification:
    def __init__(self, notification_type: str):
        self.notification_type = notification_type

    def send(self, message: str):
        if self.notification_type == "email":
	        pass
        elif self.notification_type == "sms":
            pass
        elif self.notification_type == "push":
            pass


# Пример с наследованием 
# (для каждого `notification_type` создаём отдельный дочерних класс)
class Notification:
    def send(self, message: str):
        raise NotImplementedError("Method must be implemented in child class")


class EmailNotification(Notification):
    def send(self, message: str):
        pass


class SMSNotification(Notification):
    def send(self, message: str):
        pass


class PushNotification(Notification):
    def send(self, message: str):
        pass


