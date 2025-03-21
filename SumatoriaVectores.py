from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class Vector(ABC):
    def __init__(self, *components):
        self.components = components

    @abstractmethod
    def sumar(self, otro):
        pass

    def __repr__(self):
        return f"Vector{len(self.components)}D{self.components}"


class Vector2D(Vector):
    def __init__(self, x, y):
        super().__init__(x, y)

    def sumar(self, otro):
        if isinstance(otro, Vector2D):
            x = self.components[0] + otro.components[0]
            y = self.components[1] + otro.components[1]
            return Vector2D(x, y)
        raise TypeError("Solo se pueden sumar vectores de la misma dimensión")


class Vector3D(Vector):
    def __init__(self, x, y, z):
        super().__init__(x, y, z)

    def sumar(self, otro):
        if isinstance(otro, Vector3D):
            x = self.components[0] + otro.components[0]
            y = self.components[1] + otro.components[1]
            z = self.components[2] + otro.components[2]
            return Vector3D(x, y, z)
        raise TypeError("Solo se pueden sumar vectores de la misma dimensión")


# Ejemplo de uso
v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1.sumar(v2))  # Vector2D(4, 6)

v3 = Vector3D(1, 2, 3)
v4 = Vector3D(4, 5, 6)
print(v3.sumar(v4))  # Vector3D(5, 7, 9)





