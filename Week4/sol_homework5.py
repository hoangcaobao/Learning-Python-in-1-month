#Exercise 1: Crate function with three parameter a, b, and c, to PRINT "YES" if c between a and b, else print "NO"

def check(a,b,c):
    if (b-c)*(c-a)>0:
         return 'Yes'
    else: 
         return 'No'
print(check(-3,6,-4))

#Exercise 2: Create function with parameter n to PRINT triangle with * following this rule:
#If n is 1, triangle is:
# *

#If n is 2, triangle is:
# *
# **

#If n is 3, triangle is:
# *
# **
# ***

#If n is 4, triangle is:
# *
# **
# ***
# ****

def triangle(n):
    for i in range(1,n+1):
        print('*'*i)
triangle(4)

#Exercise 3: Create a function with parameter n to RECEIVE value is square of n
def square(n):
    return n**2
print(square(10))