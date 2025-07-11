class Rectangle():
       def _init_(self, l,w):
              self.lenght = l
              self.wisth = w
       def rectangle_area(self):
              return self.lenght*self.width
newRectangle = Rectangle(12,10)
print("Dimension of Rectangle")
print("area of a rectangle :", newRectangle.rectangle_area)