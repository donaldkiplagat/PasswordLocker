import random
import string
class User:
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password

    def save_user(self):
        User.userslist.append(self)

    def delete_user(self):
        User.userslist.remove(self)

    @classmethod
    def display_users(cls):
        return cls.userslist

    @classmethod
    def find_by_number(cls,number):
        for user in cls.userslist:
            if user.password == number:
                return user

    @classmethod
    def user_exist(cls,number):
        for user in cls.userslist:
            if user.username == number:
                return True
                return False



class Credentials:
    accounts=[]
    def __init__(self,accountusername,accountname,accountpassword):
        self.accountusername= accountusername
        self.accountname = accountname
        self.accountpassword = accountpassword

    def save_account(self):
        Credentials.accounts.append(self)

    def delete_account(self):
        Credentials.accounts.remove(self)


    #Changes made here that might affect code
    @classmethod
    def display_accounts(cls):
        for account in cls.accounts:
            return cls.accounts

    @classmethod
    def find_by_number(cls,number):
        for account in cls.accounts:
            if account.accountusername ==number:
                return account
