import hashlib
def login():
    '''
    Login with account and it must be registered in the database
    '''
    email_username = input("Enter email or username:" )
    pwd = input("Enter password:" )
    auth = pwd.encode()#password encrtption
    password = hashlib.md5(auth).hexdigest()
    access=email_username+password #merge username and password in one string
    #print(access)

    cntt=0
    flag = 1
    while flag == 1:#if incorrect account or password stay in the loop
        if cntt==1:
            print("incorrect account or password try again\n")
            email_username = input("Enter email or username:")
            pwd = input("Enter password:")
            auth = pwd.encode()
            password = hashlib.md5(auth).hexdigest()
            access = email_username + password
        cntt=1
        flag = 1
        with open(r"User_Data.txt", 'r') as fp:
            for l_no, line in enumerate(fp):
                while access + '\n' == line:
                    print('\nWelcome')
                    flag = 0 #if correct account then exit
                    break

# login()