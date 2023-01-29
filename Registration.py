# LIB
from datetime import date
import hashlib
#import itertools
from email_validator import validate_email  # يتاكد من الاميل
# pip install email-validator

# Dictionary
# Dictionary in Python is a collection of keys values, used to store data
users = {
    'firstName': "",
    'userName': "",
    'lastName': "",
    'age': 0,
    'email': "",
    'password': ""
}


# Registration Function
def Registration():
    '''
    Register a new account and it must be unique per user
    '''
    newFirstName = input('Enter your First Name: ')
    newLastName = input('Enter your lastName: ')

    newUsername = input('Create new Username: ')
    # I have to check if the username exists in the database or not
    # If not then add it
    # f = open("User_Data.txt", "a+")
    # f.write(' \n ')
    # f = open("User_Data.txt", 'r')
    # info = f.read()

    flag=1
    while flag==1:
        flag=0
        with open(r"User_Data.txt", 'r') as fp:
            for l_no, line in enumerate(fp):
                while newUsername + '\n' == line:
                    print('\nUsername already exists!')
                    newUsername = input('Try another Username:')
                    flag=1
                    break

    while True:
        try:
            while True:
                birthdate_day = int(input('Enter birthdate day : '))
                if birthdate_day >0 and birthdate_day <= 31:
                    break
                else:
                    print("you entered wrong value😱😱")
                    continue

            while True:

                birthdate_month = int(input('Enter birthdate month : '))

                if birthdate_month>0 and birthdate_month <= 12:
                    break
                else:
                    print("you enter wrong value😱😱")
                    continue
            while True:

                birthdate_year = int(input('Enter birthdate year : '))

                if birthdate_year >= 1922 and birthdate_year <= 2010:

                    break
                else:
                    print("your so young😱😱")
                    continue

            birthDate = date(birthdate_year, birthdate_month, birthdate_day)
            days_in_year = 365.2425
            age = int((date.today() - birthDate).days / days_in_year)
            age = str(age)
            break
        except Exception as ex:
            print(ex)
            print("you enter wrong value😱😱")

    #check if email valid or not
    #you can comment this code if it take much time
    while True:
        try:
            newEmail = input('Create new email: ')
            validate_email(newEmail)
            break
        except ValueError as err:
            print(err)
            print('Wrong Email!😱😱')

    #newEmail = input('Create new email: ')
    # I have to check if the email exists in the database or not
    # If not then add it
    flag = 1
    while flag == 1:
        flag = 0
        with open(r"User_Data.txt", 'r') as fp:
            for l_no, line in enumerate(fp):
                while newEmail + '\n' == line:
                    print('\nEmail already exists!')
                    newEmail = input('Try another Email:')
                    flag = 1
                    break

    newPassword = input('Create new password: ')
    confirmpassword = input('confirm password: ')
    while newPassword != confirmpassword:
        print("Password is not same as above!😱😱 \n")
        newPassword = input('Create new password: ')
        confirmpassword = input('confirm password: ')

    #password encrtption
    Encrypted_password = newPassword.encode()
    Password = hashlib.md5(Encrypted_password).hexdigest()

    # Append to dictionary(users)
    users['firstName'] = newFirstName
    users['userName'] = newUsername
    users['lastName'] = newLastName
    users['age'] = age
    users['email'] = newEmail
    users['password'] = Password

    #write data in txt file
    print('\nAccount created successfully!\n')
    f = open("User_Data.txt", "a+")
    f.write(str("new user") + "\n")
    f.write(str(users['userName']) + "\n")
    f.write(str("First,last Name = " + users['firstName'] + "," + users['lastName']) + "\n")
    f.write(str("age = " + users['age']) + "\n")
    f.write(str("password = " + users['password']) + "\n")
    f.write(str(users['email']) + "\n")
    f.write(str(users['email']) + str(users['password']) + "\n")
    f.write(str(users['userName']) + str(users['password']) + "\n")
    f.close()
# Registration()
# print(users)