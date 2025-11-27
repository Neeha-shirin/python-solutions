# reverse the string 
def rev(s):
    return s[::-1]

nrev= "neeha"
result=rev(nrev)

print(nrev)
print(result)

#list types 
1. #sum of list 
def sum_list(lst):
    s=0
    for n in lst:
        s=s+n
        
    return s
r=sum_list([1,2,3,4,5])
print(r)

2. #FINDING BIGGEST NUMBER IN LIST

def biggest_list(lst):
    
    big=lst[0]
    
    for i in lst:
        if i>big:
            big=i
            
    return big
r=biggest_list([1,2,3,4,5])
print(r)

3. #count of even numbers in the list 

def count_even(lst):
    c=0
    
    for i in lst:
        if i%2==0:
            c=c+1
    return c

print(count_even([1,2,3,4,5,6,7]))

4. #reverse list 
def reverse_list(lst):
    return lst[::-1]
    
r=reverse_list([1,2,3,4,5])
print(r)

5. #multiply list
def multiply_list(lst):
    p=1
    
    for i in lst:
        p=p*i
    return p

r=multiply_list([1,2,3,])
print(r)

6.#find item in a list

def find(lst,item):
    
    for i in lst:
         if i==item:
            return "found"
    return "not found"
lst=[1,2,3,4,5]
item=int(input("enter the value ="))

print (find(lst,item))


7.decorator. # using decorator 
def show_result(func):      # decorator
    def wrapper(a, b):
        print("Adding numbers...")
        result = func(a, b)
        print("Result is:", result)
        return result
    return wrapper


@show_result
def sumof(a, b):
    c = a + b
    return c

print(sumof(3, 5))


8. count the letters in string 

def count(n):
    
    s={}
    for ch in n:
        if ch in s:
            s[ch]=s[ch]+1
        else:
            s[ch]=1
            
    return s
print(count("apple"))


9. cheaking if key exist in /not 










    
