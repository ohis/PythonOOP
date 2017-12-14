import arithmetic
class Bike(object): #TO DO CHAIN METHOD LIKE BIKE.RIDE().RIDE().reverse MAKE THE METHODS IN The
                                                    #CLASS RETURN SELF
    def __init__(self,price,max_speed,miles = 0):
        self.price = price;
        self.max_speed = max_speed;
        self.miles = miles;

    def displayInfo(self):
         print "The bike's price ,max speed and total miles are",self.price, self.max_speed,self.miles
         return self

    def ride(self):
        print "Riding"
        self.miles+=10
        print self.miles
        return self
    def reverse(self):
        print "Reversing"
        if self.miles > 0 :
            self.miles -= 5
        else:
            print "You cannot have negative miles"
        print self.miles
        return self

print arithmetic.add(5,8)

m = Bike(300,"20mph")
#m.price = 200
#m.max_speed = "50mph"
m.miles = 35

m.ride()
m.ride()
m.ride()
m.reverse()
m.displayInfo()
p = Bike(100,"35mph")
#p.miles = 5
#p.ride()
#p.ride()
#p.reverse()
#p.reverse()
p.ride().ride().reverse().reverse().displayInfo()
