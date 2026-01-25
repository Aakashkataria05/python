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

list = (1,4,9,16,25,36,49,64,89,100)
x = int(input("which number you want to find :"))

i = 0
while i<len(list):
    if(list[i] == x):
        print("the number fount at list.index :", i)
    i+=1
