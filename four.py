# i = 1
# while i<=100:
#     print(i)
#     i += 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# n = int(input("table of number : "))
# i = 1
# while i <= 10:
#     print(i*n)
#     i += 1

# list = [1,4,9,16,25,36,49,64,89,100]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

# list = (1,4,9,16,25,36,49,64,89,100)
# x = int(input("which number you want to find :"))

# i = 0
# while i<len(list):
#     if(list[i] == x):
#         print("the number fount at list.index :", i)
#     i+=1

# for i in range(100,0,-1):
#     print(i)

# n = int(input("required number for table :"))
# for i in range(1,11):
#     print(i*n)

# n = int(input("required number for first n natural number sum : "))
# sum = 0
# for i in range(1, n+1):
#     sum = sum + i

# print(sum)

# def sum_num(a,b):
#     sum = a + b
#     print(sum)


# sum_num(1,2)

# def average_num(a,b,c):
#     avg = (a+b+c)/3
#     print(avg)

# average_num(1,3,5)

def prnt_list(list):
    i = 0
    while i < len(list):
        print(list[i], end=" ")
        i += 1

games = ["hokey", "cricket", "football", "tennis"]
# prnt_list(games)

def fac(n):
    i = 1
    mul = 1
    while i <= n:
        mul = mul*i
        i += 1
    print(mul)

# fac(8)

def rec(a):
    if(a == 0):
        return 0
    return rec(a-1) + a

sum = rec(4)
# print(sum)

class student