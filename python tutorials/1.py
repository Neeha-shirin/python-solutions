1# cheak whather the number is odd or even
     
def oddeven(num):
    if num % 2 ==0:
        return "even"

    else:
       return "odd"

result=oddeven(5)
print(r)


2# counting length 


def length(n):
    return len(n)
    
r=length("neeha")
print(r)

3# swapping

def swap(a, b):
    a, b = b, a
    return a, b

r = swap(3, 6)
print(r)


4.#palindrome



def palindrome(n):
    if n==n[::-1]:
        return "palindrome"
        
    else:
        return "not palindrome"
        
r=palindrome("neeha")
print(r)

5 #reverse
def reverse(n):
     rev=n[::-1]
     return rev
    
r=reverse("hello")
print(r)

6.#print numbers from 1 to 50
def num():
        result=[]
        for i in range(1,51):
            result.append(i)
        return result
r=num()
print(r)





