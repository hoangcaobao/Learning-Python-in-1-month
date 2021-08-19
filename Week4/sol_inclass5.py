#Exercise 1: Create function with parameter n to print all square number from 1 to n
def print_squre_numbers(n):
    for i in range(1,n+1):
        if(int(i**(1/2))==i**(1/2)):
            print(i)

print_squre_numbers(12)

#Exercise 2: Create function with parameter list a to print sum of all number divisible by 3 in list a 
def print_numbers_divisible_by_3(a):
    for i in a:
        if(i%3==0):
            print(i)

print_numbers_divisible_by_3([1,3,5,7,12,9])

#Exercise 3: Create function with parameter n to receive True if n is a leap year, else recieve False
def is_Leap_Year(n):
    if(n%4==0):
        return True
    else:
        return False

print(is_Leap_Year(100))

#Exercise 4: Create function with parameter n to receive n factorial
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*1
    return result

#Exercise 5: Create function with parameter list a and number n to recieve True if n in a, else receive False
def check_number_in_list(n,a):
    if n in a:
        return True
    else:
        return False

#Exercise 6: Create function with parameter list a to receive reverse of list a
def reverse_list(a):
    result=[]
    for i in range(len(a)-1, -1, -1):
        result.append(a[i])
    return result