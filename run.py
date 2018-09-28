#!/usr/bin/env python3.6
import random
import string
from user import User
from user import Credentials
def create_user(firstname,lastname,username,userpassword):
    newuser= User(firstname,lastname,username,userpassword)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

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

                for user in display_users():
                    print(f"{user.firstname} {user.lastname}.....{user.username}")

            elif option =="LogIn":
                print("Enter Username..")
                loginUsername=input()

                print("Enter your password..")
                loginPassword=input()

                if loginUsername == username and loginPassword == userpassword:
                    print("Welcome ")














        print("New User")
        print("-"*10)
        print("First Name..")
        firstname=input()

        print("Last Name..")
        lastname=input()

        print("Set your username")
        username=input()

        print("Set your password")
        userpassword=input()

        save_user(create_user(firstname,lastname,username,userpassword))


        print("\n")
        print(f"{firstname} {lastname}'s account with Username: {username} created")

        print("\n")
        print("Here is a list of all the users")
        print("\n")

        print("New Account")
        print("-"*10)
        print("Account Name")
        accountname=input()

        print("Account Password")
        accountpassword=input()

        save_account(create_account(accountname,accountpassword))
        print("\n")
        print(f"{accountname} {accountpassword}")


        for user in display_users():
            print(f"{user.firstname} {user.lastname}.....{user.username}")

        for user in display_accounts():
            print(f"{user.accountname}......{user.accountpassword}")

if __name__ == '__main__':
    main()
