class General:
    def assignment_attempt(self, source):
        if isinstance(source, self.__class__):
            return source

class Any(General):
    pass


# Пример:
any_object = Any()
general_object = General()

# Попытка присвоения объекту типа 'General' тип 'Any'
result_1 = general_object.assignment_attempt(any_object) 
print(result_1) # <__main__.Any object at ... >

# Попытка присвоения any_object объекту типа 'Any'
result_2 = any_object.assignment_attempt(any_object)
print(result_2)  # <__main__.Any object ... >


