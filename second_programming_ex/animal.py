#Docstring
#Below I implemented the animal class with Cat and Dog subclasses. Moreover, the Dog class has BigDog subclass.
#All animals have a name and a greet method that is different for every animal


#creating the Animal superclass with name instance variable in the constructor

class Animal:
    #@params: name
    def __init__(self, name):
        self._name = name
    #greet method unimplemented(polymorphism), implemented only in the subclasses
    def greet(self):
        raise NotImplementedError

#Cat class is a subclass of animal class inherits from the animal class
class Cat(Animal):
    #@params: name
    def __init__(self, name):
        super().__init__(name)
    #Implementing the unimplemented greet method with animal specific greeting
    def greet(self):
        print("meow")
#Dog class is a subclass of animal class inherits from the animal class
class Dog(Animal):
    #@params: name
    def __init__(self, name):
        super().__init__(name)
    #Implementing the unimplemented greet method with animal specific greeting
    def greet(self):
        print("woof")

#BigDog class is a subclass of Dog class inherits from the Dog class
class BigDog(Dog):
    #@params: name
    def __init__(self, name):
        super().__init__(name)
    #Implementing the unimplemented greet method with animal specific greeting
    def greet(self):
        print("woof")
        print("woooof")


    


