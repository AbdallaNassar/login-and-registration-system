from Login import login
from Registration import Registration

while 1:
    '''
    Working as main function and show main menu
    '''
    print("********** Login System **********")
    print("1.Registration")
    print("2.Login")
    print("3.Exit")
    ch = str(input("Enter your choice: "))
    if ch == str(1):
        Registration()
    elif ch == str(2):
        login()
    elif ch == str(3):
        print("👉 thx to use project II Group F 👈")
        break
    else:
        print("Wrong Choice! 😱😱"+"\n"+"choice from 1 -🤍-> 3")
