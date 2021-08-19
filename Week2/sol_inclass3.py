#Exercise 1: Use for to print every odd number between 1 and 100 in 2 different way
#Method 1:
for i in range(1, 101):
    if (i%2 != 0):
        print(i)

#Method 2:
for i in range(1,101,2):
    print(i)

#Exercise 2: Use while to solve exercise 1
#Method 1:
shiba=1
while shiba<101:
    if (shiba%2!=0):
        print(shiba)
    shiba=shiba+1

#Method 2:
shiba=1
while shiba <101:
    print(shiba)
    shiba=shiba+2

#Exercise 3: Use for and continue to print all the numbers from 0 to 100 except number divided by 10.
for shiba in range(0,101):
    if(shiba%10==0):
        continue
    print(shiba)

#Exercise 4: Use while to solve exercise 3
shiba=0
while shiba<101:
    if shiba%10!=0:
        print(shiba)
    print(shiba)

#Exercise 5: Create a simple chat bot in terminal following these rules:
#Firtsly, print "I can do 2 options. 1) calculate sum of two numbers. 2) calculate product of two numbers"
#Secondly, use input ask options (1 or 2)
#Thirdly, use input ask 2 number: number1 and number2
#If user choose 1 print sum of number 1 and number 2
#If user choose 2 print product of number 1 and number 2
#After print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again
ask="Y"
while ask=="Y":
    print(
"""
I can do 2 options. 
1) calculate sum of two numbers. 
2) calculate product of two numbers
"""
    )
    option=int(input("What option do you want to use (1 or 2) "))
    number1=int(input("What is your number1 ? "))
    number2=int(input("What is your number2 ? "))
    if(option==1):
        result=number1+number2
    else:
        result=number1*number2
    print("Your result is {}".format(result))
    ask=input("Do you want to continue using chat bot (Y/N) ? ")