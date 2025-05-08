class Simpler:
    pass

class Student:
    def __init__(self,student_name):
        self.student_name = student_name
        self.state = "sit"
        
    def read(self):
        self.state = "reading"
        print(f"{self.student_name} is reading")
    
    def writing(self):
        self.state = "writing"
        print(f"{self.student_name} is writing")
        
    def show_state(self):
        print(f"{self.student_name} is currently {self.state}")

student = Student("John")
student.show_state()

student.read()
student.show_state()
        
student.writing()
student.show_state()      

class Buket():
    def __init__(self,fruit,vegge):
        self.fruit = fruit
        self.vegge = vegge
    
    def __del__(self):
        print(f"{self.fruit} and {self.vegge} is out from the bukket and now buket is empty")
        
buket = Buket("Watermelon","Ladyfingure")
print(buket.fruit)
print(buket.vegge)

del Buket

class Secrettalks():
    def __init__(self,talks):
        self.__talks = talks
        
    def showtalks(self):
        print(f"{self.__talks} its my secret talks")
        
talks = Secrettalks("I am rise in love with coding 🤣🤣😃😂😁")
talks.showtalks()

class Talkshub(Secrettalks):
    def access_secret(self):
        print(self._Secrettalks__talks)
        

tbox = Talkshub("I am rise in love with coding 🤣🤣😃😂😁")
tbox.access_secret()

class Secretbox():
    def __init__(self,chocolate):
        self._chocolate = chocolate
    
    def chocobox_location(self):
        print(f"{self._chocolate} is in my study table draw")
    
box = Secretbox("Kitkat")
# print(box._chocolate)
box.chocobox_location()

class treasurebox(Secretbox):
    def access_secret(self):
        print(self._chocolate)

tbox = treasurebox("Kitkat")
tbox.access_secret()

class Parents:
    def __init__(self,eye,hairs):
        self.eye = eye
        self.hairs = hairs
        
    def show_properties(self):
        print(f"{self.eye} {self.hairs}")
        
parents = Parents("blue","brown")
parents.show_properties()
        
class Child(Parents):
    def __init__(self,eye,hairs):
        super().__init__(eye,hairs)
        

child = Child("blue","black")
child.show_properties()

class Fish():
    def swim(self):
        print("Flying high")
    
class Bird():
    def fly(self):
        print("Swim deep")
        
class Flyfish(Fish,Bird):
    pass

fly_fish = Flyfish()
fly_fish.fly()
fly_fish.swim()

from abc import ABC, abstractmethod

#Abstract base class
class Vahicle(ABC):
    def __init__(self,model):
        self.model = model
        self.state = "Stop"
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def breack(self):
        pass
    
    def show_status(self):
        print(f"{self.model} {self.__class__.__name__} is {self.state}")
        
#Concrete class
class Car(Vahicle):
    def start(self):
        self.state = "Start"

    def run(self):
        self.state = "Run"
        
    def breack(self):
        self.state = "break"

car = Car("Fortuner")
car.show_status()
car.start()
car.show_status()
car.run()
car.show_status()
car.breack()
car.show_status()
car.run()
car.show_status()


class Bike(Car):
    pass

bike = Bike("Honda")
bike.show_status()
bike.start()
bike.show_status()
bike .run()
bike.show_status()

class Bus(Car):
    pass

bus = Bus("Greenline")
bus.show_status()
bus.start()
bus.show_status()
bus.run()
bus.show_status()


from abc import ABC, abstractmethod

#Abstract base class
class Vahicle(ABC):
    def __init__(self,model):
        self.model = model
        self.state = "Stop"
    
    @abstractmethod
    def start(self):
        self.state = "Start"
    
    @abstractmethod
    def run(self):
        self.state = "Run"
    
    @abstractmethod
    def breack(self):
        self.state = 
    
    def show_status(self):
        print(f"{self.model} {self.__class__.__name__} is {self.state}")
        
#Concrete class
class Car(Vahicle):
    def start(self):
        self.state = "Start"

    def run(self):
        self.state = "Run"
        
    def breack(self):
        self.state = "break"

car = Car("Fortuner")
car.show_status()
car.start()
car.show_status()
car.run()
car.show_status()
car.breack()
car.show_status()
car.run()
car.show_status()


class Bike(Car):
    pass

bike = Bike("Honda")
bike.show_status()
bike.start()
bike.show_status()
bike .run()
bike.show_status()

class Bus(Car):
    pass

bus = Bus("Greenline")
bus.show_status()
bus.start()
bus.show_status()
bus.run()
bus.show_status()