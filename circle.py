class circle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        sum = 22/7*((self.radius)**2)
        return sum
    
    def calculate_parimeter(self):
        par = 2*22/7*self.radius
        return par

c = circle(21)
print(c.calculate_area())
print(c.calculate_parimeter())