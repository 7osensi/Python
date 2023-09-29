class person:
    
    name = ""
    age = ""
    
    def __init__(self, myname, myage):
        self.name = myname
        self.age = myage

    def sayHello(self):
        """
        Function that says hello.
        """
        print(f"Hello {self.name}")

    def __del__(self):
        pass

person1 = person("Hussein", 24) #person1 is object from class person
person2 = person("Mahmoud", 17)

print(person1.name)
print(person2.name)

print(person1.age)
print(person2.age)

print(person1.sayHello.__doc__)
