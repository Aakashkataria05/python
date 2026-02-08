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

new_arr = np.insert(numpy_array, 3, 100)
print(new_arr)

arr1 = np.array([5,6,7])
arr2 = np.array([5,4,3])

result = arr1 + arr2
print(result)
