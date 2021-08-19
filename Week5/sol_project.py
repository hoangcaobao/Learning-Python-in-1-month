#Create a simple version of Projectube
#When run program:
#1. Use program
#2. Stop program
#If user choose 2 stop program immediately
#If user choose 1:
#1. User
#2. Orgination
#Then even user choose 1 or 2:
#1. Sign in 
#2. Sign up
#If user choose 1:
# Email: 
# Password:
#If email and password is not correct ask email and password again
#If user choose 2:
# Email:
# Password:
# Confirm password:
#If 2 passowrd is not the same ask email and 2 password again
#After user login as a User
#1. See events
#2. See orgs
#If user choose 1 list all current name of events with their number
#If user choose number print decriptions of this events
#If user choose 2 list all current name of organizations with their number
#If user choose number print decriptions of this organization
#Then:
#1. Continue to see 
#2. Logout
#If user choose 1 return to ask see events or see orgs
#If user choose 2 return to ask use program or stop program
#After user login as a Organization
#If this organation is new ask their description
#After that
#1. See events
#2. See orgs
#3. Create events
#If user choose 1 or 2 will be the same action above
#If use choose 3
#Ask how many events want to add (maximum 5)
#If number larger than 5 ask again 
#Then ask name of events and description
#Then:
#1. Continue to see or creaete event
#2. Logout
#If user choose 1 return to ask see events or see orgs or create events
#If user choose 2 return to ask use program or stop programs
def create_events(events, des_events):
    repeat=True
    while repeat:
        number=int(input("How many events you want to add: "))
        if number>5:
            print("your number of events is too large. do you want to ask again? ")
        else:
            repeat=False
            for i in range(1, number+1):
                name=input("enter your name of event {}". format(i))
                des=input("enter your description {}". format(i))
                events.append(name)
                des_events.append(des)

def orgs_actions(events, des_events, orgs, des_orgs):
    print(
"""
1. See events
2. See orgs
3. Create events
""")
    option=input()
    if(option=="1"):
        for i in range(0, len(events)):
            print("{0}, {1}".format(i,events[i]))
        
        repeat=True
        while repeat==True:
            number=int(input())
            if number>=0 and number<len(des_events):
                print(des_events[number])
                repeat=False
            else:
                print("Your number is out of range")
    if(option=="2"):
        for i in range(0, len(orgs)):
            print("{0}, {1}".format(i,orgs[i]))
        repeat=True
        while repeat:
            number=int(input())
            if number>=0 and number<len(des_orgs):
                print(des_orgs[number])
                repeat=False
    if (option=="3"):
        create_events(events, des_events)


def sign_in(accounts):
    repeat=True
    while repeat==True:
        email=input("Email ")
        password=input("Password: ")
        if email not in accounts:
            print("Your account not exists")
        elif password!=accounts[email]:
            print("Password is not correct")
        else:
            repeat=False

def sign_up (accounts):
    repeat = True
    while repeat==True:
        user_email = input("What is your email? ")
        user_password = input("What is your password? ")
        confirm_password = input("Confirm password: ")
        if user_password != confirm_password:
            print ("Password does not match")
        elif user_email in accounts:
            print ("account alreasy exists")
        else:
            repeat = False
            accounts[user_email] = user_password

def user_actions(events, des_events, orgs, des_orgs):
    print(
"""
1. See events
2. See orgs
""")
    option=input()
    if(option=="1"):
        for i in range(0, len(events)):
            print("{0}, {1}".format(i,events[i]))
        
        repeat=True
        while repeat==True:
            number=int(input())
            if number>=0 and number<len(des_events):
                print(des_events[number])
                repeat=False
            else:
                print("Your number is out of range")
    if(option=="2"):
        for i in range(0, len(orgs)):
            print("{0}, {1}".format(i,orgs[i]))
        repeat=True
        while repeat:
            number=int(input())
            if number>=0 and number<len(des_orgs):
                print(des_orgs[number])
                repeat=False

accounts={
    
}

events=[]
des_events=[]
orgs=[]
des_orgs=[]

while True:
    print("""
1. Use program
2. Stop program
""")
    use_program=input()
    if use_program=="2":
        break
    print(
"""
1. User
2. Organisation
""")
    role=input()
    print(
"""
1. Sign in 
2. Sign up
""")
    welcome_option=input()
    if(welcome_option == "1"):
        sign_in(accounts)
    else:
        sign_up(accounts)
    if role=="1":
        ask_continue="1"
        while ask_continue=="1":
            user_actions(events, des_events, orgs, des_orgs)
            print("""
1. Continue to see 
2. Logout
            """)
            ask_continue=input()
    
    elif role=="2":
        name_of_orgs=input("Name of orgs")
        if name_of_orgs not in orgs:
            des_orgs=input("Description of orgs")
            orgs.append(name_of_orgs)
            des_orgs.append(des_orgs)
        ask_continue="1"
        while ask_continue=="1":
            orgs_actions(events, des_events, orgs, des_orgs)
            print("""
1. Continue to see 
2. Logout
            """)
            ask_continue=input()
        
