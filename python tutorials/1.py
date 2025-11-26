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

7.#print from 1 to 100 even numbers
def number():
    result=[]
    for i in range(1,100):
        if i%2==0:
            result.append(i)
    return result
        
r=number()
print(r)

8#counting vowels 
def counting(n):
    vowels="aeiou"
    count=0
    for ch in n:
        if ch in vowels:
            count=count+1
    return count
r=counting("neeeha")
print(r)


9. #multiplication table 
def mul_table(n):
    for i in range (1,11):
        print(n, "x", i,"=", i*n)
        
mul_table(6)


10.#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        
    return fact 
r=factorial(5)
print(r)


11.#sum of n numbers
def sum_of_numbers(n):
    
    s=0
    for i in range(1,n+1):
        s=s+1
    return s
print(sum_of_numbers(5))
        




