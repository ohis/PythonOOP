class Animal(object):
    def __init__(self,name= None):
        self.health = 100
        self.name = name

    def walk(self):
        self.health-= 1

    def run(self):
        self.health -= 5

    def displayHealth(self):
        print self.name
        print self.health

animal = Animal("male")
animal.walk()
animal.walk()
animal.walk()
animal.displayHealth()
