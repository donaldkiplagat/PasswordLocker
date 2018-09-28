#!/usr/bin/env python3.6

from user import User
def create_user(firstname,lastname,username,password):
    newuser= User(firstname,lastname,username,password)
    return newuser

def save_user(user):
    user.save_user()

def delete_user(user):
    user.delete_user()

def display_users():
    return User.display_users()

def main():
    while True:
        print("Welcome to your password locker!Let's start by creating your account")

        print("New User")
        print("-"*10)
        print("First Name..")
        firstname=input()

        print("Last Name..")
        lastname=input()

        print("Set your username")
        username=input()

        print("Set your password")
        password=input()

        save_user(create_user(firstname,lastname,username,password))
        print("\n")
        print(f"{firstname} {lastname}'s account with Username: {username} created")

        print("\n")
        print("Here is a list of all the users")
        print("\n")

        for user in display_users():
            print(f"{user.firstname} {user.lastname}.....{user.username}")

if __name__ == '__main__':
    main()
