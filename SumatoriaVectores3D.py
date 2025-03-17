from abc import ABC, abstractmethod

class VectorBase(ABC):
    @abstractmethod
    def add(self, other):
        pass

class Vector3D(VectorBase):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        if not isinstance(other, Vector3D):
            raise TypeError("Expected a Vector3D instance")
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Ejemplo de uso
v1 = Vector3D(3, 4, 5)
v2 = Vector3D(1, 2, 3)
result = v1.add(v2)
print(result)  # Output: Vector3D(4, 6, 8)