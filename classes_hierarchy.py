import copy
from typing import Self


class General(object):
    def __init__(self):
        self.data = []

    def __eq__(self, other) -> bool:
        pass
          
    def __repr__(self) -> str:
        pass
    
    def __str__(self) -> str:
        pass
    
    def is_deep_equal(self) -> bool:
        pass

    def copy(self, is_deepcopy: bool) -> Self:
        pass

    def clone(self) -> Self:
        pass

    def isinstance(self, type_: object):
        pass

    def type(self):
        pass



class Any(General):
    def __init__(self):
        super().__init__(self)

    def __eq__(self, other) -> bool:
        return self.data == other.data
          
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}()"
    
    def __str__(self) -> str:
        return f"<{self.__class__.__name__} instance at {hex(id(self))}>"
    
    def is_deep_equal(self, other) -> bool:
        return id(self.data) == id(other.data)

    def copy(self, deepcopy: bool) -> Self:
        if deepcopy:
            return copy.deepcopy(self)
        return self

    def clone(self) -> Self:
        return Any(self.data[:]) 

    def isinstance(self, type_: object) -> bool:
        return isinstance(self, type_)

    def type(self) -> object:
        return type(self)


