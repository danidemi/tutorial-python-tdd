print("Hello World")

class Person:

    def __init__(self, name):
        self.name = name
        print("I'm a new person")


    def greetings(self):
        return "Hello, I'm " + self.name

class Worker(Person):

    def wage(self):
        return 1000.00

    def greetings(self):
        return Person.greetings(self) + " and I earn " + str( self.wage() ) + " credits per month"

    def greetings2(self):
        return super().greetings()

    def greetings3(self):
        return super().greetings()  + " and I earn " + str( self.wage() ) + " credits per month"

p = Person("John")
print(p.greetings())

p = Worker("Mary")
print(p.greetings())
print(p.greetings2())
print(p.greetings3())


print( __name__ )
