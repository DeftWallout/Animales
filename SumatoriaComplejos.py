from abc import ABC, abstractmethod

class ComplexOperation(ABC):
    @abstractmethod
    def sum_squares(self, c1, c2):
        pass

class ComplexSum(ComplexOperation):
    def sum_squares(self, c1, c2):
        return c1**2 + c2**2

# Ejemplo de uso
num1 = complex(3, 2)  # 3 + 2j
num2 = complex(-1, 4)  # -1 + 4j
operation = ComplexSum()
result = operation.sum_squares(num1, num2)
print(f"La suma de los cuadrados de {num1} y {num2} es: {result}")
