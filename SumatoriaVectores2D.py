from abc import ABC, abstractmethod

class VectorBase(ABC):
    @abstractmethod
    def add(self, other):
        pass

class Vector2D(VectorBase):
    def __init__(self, x, y): #Esta parte inicializa un vector en 2D.
        self.x = x
        self.y = y

    def add(self, other): #Esta parte suma este vector con otro vector 2D
        if not isinstance(other, Vector2D):
            raise TypeError("Expected a Vector2D instance")
        return Vector2D(self.x + other.x, self.y + other.y)

    def __repr__(self): #Representación en cadena del vector
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
result = v1.add(v2)
print(result)





