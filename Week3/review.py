#homework1
#Exercise 1: Assign value 5 to variable a and -3 to variable b and product of a and b to variable c. Then print c
a=5
b=-3
c=a*b
print(c)

# #Exercise 2: Use input ask address and city. 
# Print "I live in {0} , {1}" with 0 is address and 1 is city
adress=input()
city=input()
print("I live in {0} , {1}".format(adress,city))

#Exercise 3: Use input ask 2 number: number1 and number2. Print divison of number1 and number2.  
number1=float(input())
number2=float(input())
print(number1/number2)

#homework2
#Exercise 1: Use input ask year. 
#Pseudocode:
#print "yes" if this year is leap year
#print "no" if this year is not leap year
# year=int(input())
# if year%4==0:
#     print("yes")
# else:
#     print("no")
# if (year is not divisible by 4) then (it is a common year)
# else if (year is not divisible by 100) then (it is a leap year)
# else if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

year=int(input())
if(year%4!=0):
    print("no")
elif (year%100!=0):
    print("yes")
elif (year%400!=0):
    print("no")
else:
    print("yes")


#Exercise 2: Create a simple chat bot in terminal following these rules:
#Firstly, use input ask name
#Then print "Hello {0}, how can I help you" with 0 is the value of name
#print "I can do 2 options. 1) calculate substraction of two numbers. 2) calculate division of two numbers"
#Secondly, use input ask options (1 or 2)
#Thirdly, use input ask 2 number: number1 and number2
#If user choose 1 print substraction of number 1 and number 2
#If user choose 2 print division of number 1 and number 2

name=input()
print( "Hello {0}, how can I help you".format(name))
print("""
I can do 2 options. 
1) calculate substraction of two numbers. 
2) calculate division of two numbers
""")
option=input("Your option: ")
while option!="1" and option!="2":
    print("You can only choose 1 or 2. Not type other thing")
    option=input("Type your option again: ")
option=int(option)
number1=int(input("Number 1: "))
number2=int(input("NUmber 2: "))
if option==1:
    print(number1-number2)
else:
    print(number1/number2)

#Check type wrong option
# name=input()
# print( "Hello {0}, how can I help you".format(name))
# print("""
# I can do 2 options. 
# 1) calculate substraction of two numbers. 
# 2) calculate division of two numbers
# """)
option=input("Your option")
type_correctly=False
while type_correctly==False:
    if option=="1" or option=="2":
        type_correctly=True
    else:
        option=input("You type wrongly. Your option: ")
option=int(option)
number1=int(input("Number 1: "))
number2=int(input("Number 2: "))
if option==1:
    print(number1-number2)
else:
    print(number1/number2)

#Homework3
#Exercise 1: Use for to print every square number between 1 and 100
#Method 1
import math
number=math.sqrt(100)
number=int(number)

#Method 2
for i in range(1, 11):
    print(i*i)

#Method 3
import math
for i in range(1,101):
    if(int(math.sqrt(i))==math.sqrt(i)):
        print(i)

#Exercise 2: Use while to solve exercise 1
import math
number=math.sqrt(100)
number=int(number)
i=0
while i<=number:
    print(i*i)

#Exercise 3: Create a simple chat bot in terminal following these rules:
#Firstly, use input ask name
#Then print "Hello {0}, how can I help you" with 0 is the value of name
#Use input ask current_money
#print "I can do 2 options. 1) withdraw money 2) add more money"
#Use input to ask option
#If user choose 1 use input ask withdraw money
#Then print "Now you have {0} $" with 0 is the current money AFTER WITHDRAW
#If user choose 2 use input ask add money
#Then print "Now you have {0) $" with 0 is the current money AFTER ADD
#After print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again
# name=input("Your name: ")
# print("Hello {0}, how can I help you".format(name))
# current_money=int(input())
# print("""
# I can do 2 options. 
# 1) withdraw money 
# 2) add more money
# """)
ask="Y"
option=int(input())
while ask=="Y":
    if(option==1):
        withdraw_money=int(input("Amount of money you want to withdraw"))
        current_money-=withdraw_money
        print("Now you have {0} $".format(current_money))
    else:
        add_money=int(input("Amount of money you want to withdraw"))
        current_money+=add_money
        print("Now you have {0) $".format(current_money))
    ask=input("Do you want to continue using chat bot (Y/N) ?")

#homework4
#Exercise 1: Create a simple chat bot in terminal following these rules:
#Firstly, use input ask name
#Then print "Hello {0}, welcome to our service" with 0 is the value of name
#Print current list refrigerator (if first time it is empty)
#Print "We can do 2 options. 1) Add new food to refrigerator 2) remove food from refrigerator"
#Use input to ask options
#If user choose 1 use input ask new food
#Print "Here is your refrigerator after adding new food"
#Then print list refrigerator after add newfood
#If user choose 2 print "Here is your current refrigerator"
#Then print list refrigerator
#Then use input to ask the index user want to remove
#If this index is valid, print "Here is your refrigerator after removing food", then print list refrigerator
#If not, print "The index you input must larger than {0} and smaller than {1}", then ask again until index is valid
#After finishing print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again

name=input()
print("Hello {0}, welcome to our service".format(name))
refrigerator=[]
print(refrigerator)
print("""
We can do 2 options. 
1) Add new food to refrigerator 
2) remove food from refrigerator
""")
option=int(input())
ask="Y"
while ask=="Y":
    if(option==1):
        add_food=input()
        refrigerator.append(add_food)
    else:
        print("Here is your current refrigerator")
        print(refrigerator)
        index=int(input())
        index_valid=False
        while index_valid==False:
            if index>=0 and index<=len(refrigerator)-1:
                refrigerator.pop(index)
                index_valid=True
            else:
                print("The index you input must larger than {0} and smaller than {1}".format(-1, len(refrigerator)))
                index=int(input())
    ask=input("Do you want to continue using chat bot (Y/N) ?")
