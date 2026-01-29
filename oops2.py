class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_score(self):
        sum=0
        for val in self.marks:
            sum += val
        print(sum/3)

s1 = student("aakash", [83,92,89])
s1.avg_score()