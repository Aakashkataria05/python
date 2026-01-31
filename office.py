class employe:
    
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary

    def show_details(self):
        print("name :-",self.name)
        print("role :-",self.role)
        print("salary :-",self.salary)

class engineer(employe):
    def __init__()

e1 = employe("aakash","data scientist",520000)
e1.show_details()
