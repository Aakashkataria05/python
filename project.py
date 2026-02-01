import random

target = random.randint(1,100)

while True:
    userchoice = int(input("guess the number :-"))

    if(userchoice == target):
        print("Success : correct guess !!")
        break
    
    elif(userchoice > target):
        print("wrong guess : guess smaller numbeer")

    else:
        print("wrong guess : guess bigger numbeer")

print("-----GAME OVER-----")