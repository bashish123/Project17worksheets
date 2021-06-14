#!/usr/bin/env python
# coding: utf-8

# #### 11. Write a python program to find the factorial of a number.

# In[ ]:


a=1 
i=1 #use to iterate ove the numbers

#implementation of loop is starting from here
x=int(input("Enter number: "))#collecting I/P from user
while i<=x:
    a=a*i
    i+=1
print("Factorial of",x,"is",a)#Display the O/P


# In[ ]:


a=1
x=int(input("Enter number: "))#collecting I/P from user

#implementation of loop is starting from here
for i in range(1,x+1):
    a=a*i
print("Factorial of",x,"is",a)#Display the O/P


# #### 12. Write a python program to find whether a number is prime or composite.

# In[ ]:


num = int(input("Enter any number : "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is NOT a PIME number it is a COMPOSITE number")
            break
    else:
        print(num, "is NOT a COMPOSITE number it is a PRIME number")
elif num == 0 or 1:
    print(num, "is a neither PRIME NOR COMPOSITE number")


# #### 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[ ]:


x=input("Enter a character:")
t=set(x)
a=0

for i in t:
    for j in x:
        if i==j:
            a+=1
    print("frequency of",i,"in sentence is",a)
    a=0


# #### 13. Write a python program to check whether a given string is palindrome or not.

# malayalam

# In[ ]:


x = input("Enter a character:")
c = -1
for i in x:
    for j in x[c]:
        if i == j:
            c-=1
        else:
            break
    if i!=j :
        print("Its is not palindrome string")
        break
    elif i==j:
        pass
else:
    print("Its is palindrome string")


# In[ ]:




