class Car:
  def __init__(self, color, wgt, height, speed,name):
    self.color = color
    self.wgt = wgt
    self.height = height
    self.speed = speed
    self.name = name
    
   
  def drive(self):
     print("The name of my car is " + str(self.name))
     print("I am driving at a speed of " + str(self.speed))
     print("The weight of my car is " + str(self.wgt))
     print("The height of my car is " + str(self.height))
     print("The color of my car is " + str(self.color))
  def brake(self):
     print("I stopped my car") 
  def honk(self):
    print("I am honking at another car")
  def turn(self):
    print("I am turning to the highway")
  def crash(self):
    print("Whoops! I mistakenly crashed into a tree")

Vehicle = Car("green", 1000, "6ft", "300mph","Ferrari")
Vehicle.drive()
Vehicle.brake()
Vehicle.honk()
Vehicle.turn()
Vehicle.crash()