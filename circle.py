class circle:
    def __init__(self,radius):
        self.radius = radius

    def calculate_area(self):
        sum = 22/7*((self.radius)**2)
        return sum

c = circle(3)
print(c.calculate_area())