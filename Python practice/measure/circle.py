
class Measures:
    PI=3.14
    def __init__(self,radius):
        self.r=radius
    def area(self):
        area=self.PI*self.r*self.r
        return area
    def circumference(self):
        circum=2*self.PI*self.r
        return circum
circle=Measures(4)
print(circle.area())
print(circle.circumference())


    