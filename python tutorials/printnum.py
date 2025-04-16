a=int(input("enter first number"))
b=int(input("enter second number"))
for i in range(a,b+1):
    if i%10==0:
        print("exit")
        break
    elif i%2!=0:
        print(i)

