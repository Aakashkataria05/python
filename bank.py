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

