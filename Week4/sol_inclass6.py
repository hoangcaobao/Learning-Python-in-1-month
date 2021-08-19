#Exercise 1: Use input to ask a number. 
#Create a dictionary named square_numbers with key is from 1 to number and value is square of its key
number=int(input("Nhap mot so"))
square_numbers={}
for i in range(1, number+1):
    square_numbers[i]=i**2
print(square_numbers)

#Exercise 2: Print average of all value in square_numbers
sum=0
for key in square_numbers:
    sum+=square_numbers[key]
print(sum/number)

#Excersie 3: number=[1,1,1,2,2,3,3,4,4,4,5,5]
#Create a dictionary named frequency with key is a element in list number and value is number of this element appears
number=[1,1,1,2,2,3,3,4,4,4,5,5]
freqency={}
#Method 1:
for i in number:
    if(i in freqency):
        freqency[i]+=1
    else:
        freqency[i]=0
#Method 2:
for i  in number:
    if i not in freqency:
        freqency[i]=0
    freqency[i]+=1

#Exercise 4: Create a simple chat bot following these rules:
#Firstly, create a empty dictionary named students
#Secondly, use input to ask number of students want to add
#After use input to ask name of each students and their weigth and add them to dictionary
#Thirdly, ask what student do you want to see his weight
#After print this student's weight
#Finally, print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again
students={}
number=int(input("Your number of students: "))
for i in range(1, number+1):
    name=input("Student {} ".format(i))
    weight=int(input("Weight of student {} ".format(i)))
    students[name]=weight

ask="Y"
while ask=="Y":
    name=input("Student you want to see weight ")
    print(students[name])
    ask=input("Do you want to continue using chat bot (Y/N)")
