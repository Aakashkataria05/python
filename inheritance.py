class A:
    var_a = "welcome to class A"

class B:
    var_b = "wlecome to class B"

class C(A,B):
    var_c = "welcome to class C"

c1=C()
print(c1.var_b)