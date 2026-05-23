class Person:
    number = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def say_hi(self):
        print("Hello, my name is " + self.name)

    def __str__(self):
        return "I am " + self.name

    def __eq__(self, other):
        return self.name == other.name



p1 = Person("Adam", 100)
p2 = Person("John", 100)


print(p1.number)
p1.number = 1
print(p1.number)
print(p2.number)

p2.health = 300
print(p2.health)

p1.say_hi()
p2.say_hi()

Person.say_hi(p2)

def say_hi(self):
    print("Hello, my name is " + self)

#say_hi()


p3 = Person("Eva", 100)
p4 = Person("Eva", 100)
print()
print(p3)
print(p4)
print(p3 == p4)


print(Person.__eq__(p1, p2))