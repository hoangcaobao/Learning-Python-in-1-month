#Exercise 1: Create a simple chatbot following these rules:
#Firstly, create a dictionary named manage_subjects
#Use input to ask number of subjects want to manage
#After that use input to ask each name of subject and its score (out of 10) and add them to dictionary
#Secondly print "We can do 2 options. 1) Check every subjects with score lower than 5 2) print average score of all subjects 3) add new subject score or change subject score"
#Use input to ask options
#If user choose 1 
#Print "Here is a list of your weak subjects {0}" with 0 is a value of list contain every weak subjects
#If user choose 2 
#Print "Here is your average scores: {0}" with 0 is a average score
#If user choose 3
#Use input to ask name of subject and its score and add it to or change it in dictionary
#After finishing print "Do you want to continue using chat bot (Y/N) ?"
#Use input ask options (Y or N)
#If N out terminal
#If Y continue to ask again

manage_subjects={}

number=int(input("Enter your number of subjects: "))

for i in range(1, number+1):
    name=input("name of subject {}: ". format(i))
    score=float(input("score of subject {} (out of 10): ". format(i)))
    manage_subjects[name]=score

print("""
We can do 3 options.
1) Check every subjects with score lower than 5
2) print average score of all subject
3) add new subject score or change subject score
""")

ask="Y"
while ask=="Y":
    option=int(input("enter your option (1,2 or 3): "))
    if option==1:
        list=[]
        for score in manage_subjects:
            if manage_subjects[score]<5:
                list.append(score)
        print("Here is a list of your weak subjects {}". format(list))

    elif option==2:
        s=0
        for score in manage_subjects:
            s+=manage_subjects[score]
        print("Here is your average scores: {}". format(s/number))

    else:
        new_name=input("enter your name of subject: ")
        new_score=float(input("enter your score of subject (out of 10): "))
        manage_subjects[new_name]=new_score
        print(manage_subjects)

    ask=input("Do you want to continue using chat bot (Y/N)? ")