# swapping numbers


def swap(a, b):
    a, b = b, a
    return a, b

num1 = 10
num2 = 20
print("before swapping")
print("a =", num1)
print("b =", num2)

num1, num2 = swap(num1, num2)
print("after swapping")
print("a =", num1)
print("b =", num2)


# without using function
'''
a=12
b=30
print("before swapping")
print("a=",a)
print("b=",b)

a,b=b,a

print("after swapping")
print("a=",a)
print("b=",b)

'''



