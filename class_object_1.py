# defining a class
class Person:
    
    # creating instance variables
    def set_details(self, name, age):
        self.name = name
        self.age = age
    
    # method 1
    def display(self):
        print('I am a person', self.name)
    
    # method 2
    def greet(self):
        print('Hey there, Good Morning! I am this years old', self.age)
        self.display()
        
# Creating p1 as an object of Person class
p1 = Person()
p1.set_details('Modi',50)
p1.display()
p1.greet()

# Creating p2 as an object of Person class
p2 = Person()
p2.set_details('Donald',70)
p2.display()
p2.greet()

# Creating p3 as an object of Person class
p3 = Person()
p3.set_details('Putin', 60)
# instead of calling the p3. display() lets call greet first and inside that let's call display 
# using self.display() as self carries the object reference.
p3.greet()