#Week1
#Exercise 1: Use input to ask name, age, and hometown.
#Print Hello, my name is {}. I am {} years old and I live in {}
name=input("Enter your name: ")
age=input("Enter your age: ")
hometown=input("Enter your hometown: ")
print("Hello, my name is {}. I am {} years old and I live in {}".format(name, age, hometown))

#Exercise 2: Use input to ask 3 numbers
#Print average of these 3 numbers
number1=float(input("Enter your number1: "))
number2=float(input("Enter your number2: "))
number3=float(input("Enter your number3: "))
print((number1+number2+number3)/3)

#Exercise 3: Use input to ask gpa of student
#If gpa bigger than 9.0 print excellent
#if gpa bigger than 6.5 print good
#If gpa bigger than 5.0 print average
#Else print Weak
gpa=float(input("Your gpa: "))
if gpa>=9:
    print("excellent")
elif gpa>=6.5:
    print("good")
elif gpa>=5.0:
    print("average")

#Exercise 4: Use input to ask a number 
#After that print result of number after going through flow chart in this link
#https://drive.google.com/file/d/1CXpx60fYVfJGWxP79jlwADtn2aNjj1Ju/view?usp=sharing
x=int(input("enter your number: "))
if(x<5):
    x=x*10
    if(x<2):
        x=x-6
    else:
        x=x+5
elif (x>10):
    x=x*x
else:
    x=x*6
print(x)


#Week2
#Exercise 5: Use input to ask number 
#Print every number divisible by three from 1 to this number
number=int(input("Enter your number: "))
for i in range(1,number+1):
    if(i%3==0):
        print(i)

#Exercise 6: Use input to ask number
#Print yes if this number is a prime number, else print no
#Method 1:
prime=True
number=int(input("Enter your number: "))
for i in range(2, number):
    if(number%i==0):
        prime = False
        break
if prime==True:
    print("Yes")
else:
    print("No")

#Method 2:
count=0
number=int(input("Enter your number: "))
for i in range(1, number+1):
    if(number%i==0):
        count+=1
if(count==2):
    print("Yes")
else:
    print("No")

#We have list zoo = ['cat', 'elephant', 'panda', 'lion']
#Exercise 7: Print the number of animal in zoo
zoo = ['cat', 'elephant', 'panda', 'lion']
print(len(zoo))

#Exercise 8: Use input to ask a animal
#If this animal is not already in zoo print zoo after adding this animal
#Else print This animal already in zoo and ask again (#Hint: use while)
repeat=True
while repeat:
    animal=input("Enter your animal: ")
    if animal in zoo:
        print("This animal already in zoo")
    else:
        zoo.append(animal)
        repeat=False

