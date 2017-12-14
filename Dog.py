from Animals import Animal
class Dog(Animal):
      def __init__(self):
        super(Dog,self).__init__(name)
        self.health = 150

      def pet(self):
            self.health += 5
            print self.health

harry = Dog()
harry.walk()
harry.walk()
harry.walk()

harry.run()
harry.run()

 harry.pet()

harry.displayHealth()
