#Exercise 1: Use input ask a number. Check this number is between 5 and 30 or not. 
# If correct print "between 5 and 30"
# If not print "not between 5 and 30"
number=int(input("Hi bro, enter your number: "))
if 5<=number and number<=30:
    print("between 5 and 30")
else:
    print("not between 5 and 30")


#Exercise 2: Vietcode only recruits a person younger than 30 years old and live in Vietnam.
#Use first input ask about age
#Use second input ask about location
#If qualified print "qualified"
#If not print "not qualified"
age=input("Enter your age ")
age=int(age)
location=input("where do you live ")
location=location.lower()
if age<30 and location=="vietnam":
    print("qualified")
else:
    print("not qualified")


#Exercise 3: Teacher Bear love eating cakes but the amount of cakes depend on his emotion
#If his emotion is happy he eats 30 cakes
#If his emotion is nervous he eats 20 cakes
#if his emotion is angry he eats 10 cakes
#If his emotion is sad he eats 5 cakes
#Use input to ask emotion
#print "Teacher Bear eats {0} cakse" with 0 is the amount of cakes
emotion=input("emotion today")
emotion=emotion.lower()
if emotion=="happy":
    amount=30
elif emotion=="nervous":
    amount=20
elif emotion=="angry":
    amount=10
elif emotion=="sad":
    amount=5
print("Teacher Bear eats {} cakse".format(amount))


#Exercise 4: Create a simple chat bot in terminal following these rules:
#Firtsly, print "I can do 2 options. 1) calculate sum of two numbers. 2) calculate product of two numbers"
#Secondly, use input ask options (1 or 2)
#Thirdly, use input ask 2 number: number1 and number2
#If user choose 1 print sum of number 1 and number 2
#If user choose 2 print product of number 1 and number 2
print(""" 
I can do 2 options. 
1) calculate sum of two numbers. 
2) calculate product of two numbers""")
option=int(input("What options do you want to choose (1 or 2): "))
number1=int(input("Your first number "))
number2=int(input("Your second number"))
if option==1:
    result=number1+number2
else:
    result=number1*number2
print("Your result is {}".format(result))