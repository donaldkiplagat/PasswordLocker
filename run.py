#!/usr/bin/env python3.6
import string
from random import *

from user import User
from user import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def find_user(number):
    return User.find_by_number(number)


def display_users():
    return User.display_users()


def create_account(accountname,accountpassword):
    newaccount= Credentials(accountname,accountpassword)
    return newaccount

def save_account(user):
    user.save_account()

def delete_account(user):
    user.delete_account()



def display_accounts():
    return Credentials.display_accounts()

def main():


        while True:
            print("Welcome to Password Locker!Choose one of the options to begin")
            print("SignUp -or- LogIn")
            option=input()

            if option == "SignUp":
                print("Create Account")
                print("-"*10)
                print("Enter First Name..")
                firstname=input()

                print("Enter Last Name..")
                lastname=input()

                print("Set your username..")
                username=input()

                print("Set your password..")
                userpassword=input()

                save_user(create_user(firstname,lastname,username,userpassword))

                print("Thank you for registering an account with us.Here are your details:")
                print("-"*10)
                print(f"Name: {firstname} {lastname} \nUsername: {username} \nPassword: {userpassword}")
                print("\nNow you can LogIn using these details")
                print("\n \n")

                # for user in display_users():
                #     print(f"{user.firstname} {user.lastname}.....{user.username}")

            elif option =="LogIn":
                print("Enter Username..")
                loginUsername=input()

                print("Enter your password..")
                loginPassword=input()

                if find_user(loginPassword):
                    print("\n")
                    print("Welcome! Choose any option from the ones provided below:")
                    print("-"*60)

                    print("AddAccount -or- ViewAccounts")

                    choose= input()
                    print("\n")

                    if choose == "AddAccount":
                        print("Add Credentials Account")
                        print("-"*25)
                        print("Account Name")
                        accountname=input()

                        print("\n")
                        print("Generate automatic password(generate) or Create your own personal password(create)?")
                        decision=input()

                        if decision=="generate":
                            characters=string.ascii_letters + string.digits
                            accountpassword="".join(choice(characters)for x in range(randint(8,16)))
                            print(f"Password: {accountpassword}")

                        elif decision=="create":
                            print("Enter your Password")
                            accountpassword=input()

                        else:
                            print("Invalid Choice,try again")

                        save_account(create_account(accountname,accountpassword))
                        print("\n")
                        print(f"Account: {accountname} \nPassword: {accountpassword}")

                    elif choose == "ViewAccounts":
                        print("List of all your accounts: ")
                        print("-"*25)
                        for user in display_accounts():
                            print(f"Account: {user.accountname} \nPassword: {user.accountpassword} \n\n")



                    else:
                        print("Not a valid option,please try again")
                        print("\n")

                else:
                    print("Incorrect username or password,please try again")
                    print("\n")


            else:
                print("Incorrect option,choose from the one's listed")
                print("\n")


if __name__ == '__main__':
    main()
