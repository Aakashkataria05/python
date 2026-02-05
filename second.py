# str = "aakash"
# str2 = " kataria shabh"

# print(str + str2)
# print(str[0]+str[2])
# print(str2[1:9])

# list = [2,3,4,1]
# list.append(9)
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)

# a = str(input("enter fav movie1 :"))
# b = str(input("enter fav movie2 :"))
# c = str(input("enter fav movie3 :"))

# list=[ a, b, c]
# print(list)

class account:
    def __init__(self, ball, acc):
        self.ball = ball
        self.account_no = acc

    def debit(self, amount):
        self.ball -= amount
        print("Rs.",amount ,"has been debited from your account")
        print("total ball is " ,self.ball)

    def credit(self, amount):
        self.ball += amount
        print("Rs.", amount ,"has been credited from your account")
        print("total ball is ", self.ball)
    
account1 = account(9000,1234)
account1.debit(300)