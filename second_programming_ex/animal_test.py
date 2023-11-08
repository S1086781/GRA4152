def Animal_test():
    from animal import Animal, Dog, Cat, BigDog
    import argparse
    parser=argparse.ArgumentParser(description="""This is the test function for the Animal class. The animal class has Cat and Dog subclasses. Moreover, the Dog subclass has BigDog subclass. All animals have a name and a greet method that is different for every animal.
                                   Method1: -greet Greet method prints the specific greeting of the given animal for instance meow for cat.
                                   
                                   Explanation of inheritance, overriding and polymorphism: -inheritance: The subclasses(Cat, Dog, BigDog) inherit the self._name instance variable from the superclass Animal. -overriding: for the greet method I used overriding. I modified the greet method for the subclasses to print an animal specific greeting. -Polymorphism: the greet method is different for different types of animals but the method is callable for all of them. That is why the greet method is created in the superclass without implementing it completely. """)
    parser.parse_args()

    cat=Cat('cat1')
    dog=Dog('dog1')
    bigdog=BigDog('bigdog1')

    cat.greet()
    print("Expected: meow")
    dog.greet()
    print("Expected: woof")
    bigdog.greet()
    print("Expected: woof\n woooof")

Animal_test()

