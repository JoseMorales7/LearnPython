## is-a  Animal is a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass
## is-a
class Dog(Animal):
    def __init__(self, name):
        ##has-a
        self.name = name
        
##is-a
class Cat(Animal):
    def __init__(self, name):
        ##has-a
        self.name = name
        
##is-a
class Person(object):
    def __init__(self, name):
        ##is-a 
        self.name = name
        
        ##is-a person has a pet of some kind
        self.pet = None
        
##is-a
class Employee(Person):
    def __init__(self, name, salary):
        ##is-a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ##is-a
        self.salary = salary
        
## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass

##is-a
rover = Dog("Rover")

##is-a
satan = Cat("Satan")

##is-a
mary = Person("Mary")

##has-a
mary.pet = satan

##s-a
frank = Employee("Frank", 120000)

##has-a
frank.pet = rover

##has-a
flipper = Fish()

##has-a
crouse = Salmon()

##has-a
harry = Halibut()

