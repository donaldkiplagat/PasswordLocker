#!usr/bin/env python3.6

from user import user
def create_user(firstname,lastname,username,password):
    newuser= User(firstname,lastname,username,password)
    return newuser

def save_user(user):
    user.save_user()

def display_users():
    return User.diplay_users()
