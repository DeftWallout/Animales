from abc import ABC, abstractmethod


#Interface (Abstract Base Class)
class Animal(ABC):
    @abstractmethod
    def speak(self) -> str:
        """Method that must be implemented in subclasses"""
        pass
    def leg(self) ->str:
        """Method that must be implemented in subclasses"""
        pass
#Sub-clases
class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"
    def leg(self) -> str:
        return "Four legs"

class Duck(Animal):
    def speak(self) -> str:
        return "Cuack! Cuack!"
    def leg(self) -> str:
        return "Two legs"

#Métodos
def make_animal_speak(animal: Animal):
    print(animal.speak())

def animal_legs(animal: Animal):
    print(animal.leg())
    
#Crear las variables
dog = Dog()
duck = Duck()
#Imprimir los métodos de habla
make_animal_speak(duck)
make_animal_speak(dog)
#Imprimir los métodos de número de patas
animal_legs(dog)
animal_legs(duck)

