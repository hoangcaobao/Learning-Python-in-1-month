numbers=[1,3,4,5,2]

#Exercise 1: Do not use len(). print the length of list numbers.
#Hint: Use for in list
length=0
for number in numbers:
    length=length+1
print(length)

#Exercise 2: Use input to ask number. Add this number at the end of list numbers.
print(numbers)
number=int(input("Your number: "))
numbers.append(number)
print(numbers)
numbers.insert(len(numbers), number)
print(numbers)

#Exercise 3: Similar to exercise 2 but if add number already exist in list numbers. Do not add and print "This number already exists"
#Method 1:
print(numbers)
number=int(input("Your number: "))
already_exists=False
for i in numbers:
    if i==number:
        already_exists=True
        break
if already_exists==False:
    numbers.append(number)
    print(numbers)
else:
    print("This number already exists")

#Method 2:
print(numbers)
number=int(input("Your number: "))
if (number in numbers):
    print("This number already exists")
else:
    numbers.append(number)
    print(numbers)

#Exercise 4: Use input to ask index. 
#If this index is valid, remove element at this index in this list
#If not, print index is invalid
print(numbers)
index=int(input("Your index you want to remove: "))
if index<=len(numbers)-1 and index>=0:
    numbers.pop(index)
    print(numbers)
else:
    print("This index is invalid")


#Exercise 5: Use input to ask number. Remove this number from list numbers if it exists
print(numbers)
number=int(input("Your number you want to delete: "))
if number in numbers:
    numbers.remove(number)
    print(numbers)
else:
    print("Your number already not in list")

#Exercise 6: Print all element larger than 3 in list numbers
for number in numbers:
    if(number>3):
        print(number)

#Exercise 7: Print second smallest number and second largest number in list numbers
numbers.sort()
print(numbers[1])
print(numbers[len(numbers)-2])

#Exercise 8: Add even numbers from 1 to 100 to a new list and print it
new=[]
for i in range(1,101):
    if(i%2==0):
        new.append(i)
print(i)