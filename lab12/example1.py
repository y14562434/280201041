import math

class Cylinder:
  
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height
  
  def getRadius(self):
    return self.radius
  
  def getHeight(self):
    return self.height

  def setRadius(self, r):
    self.radius = r

  def setHeight(self, h):
    self.height = h

  def base_area(self):
    return math.pi*self.radius**2

  def surface_area(self):
    return 2*math.pi*self.radius*self.height

  def area(self):
    base_area = self.base_area()
    surface_area = self.surface_area()
    return 2*base_area + surface_area

  def volume(self):
    return self.base_area()*self.height


a = Cylinder(3,5)

print(a.area())
print(a.volume())
