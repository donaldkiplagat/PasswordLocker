import random
import string
class User:
    """
    Class that generates new instances of users
    """
    userslist=[]
    def __init__(self,firstname,lastname,username,password):
            """
        __init__ method that helps us define properties for our objectsself.

        Args:
        firstname: New user first name
        lastname: New user last name
        username: New user username
        password: New user password
        """
        self.firstname=firstname
        self.lastname=lastname
        self.username=username
        self.password=password

    def save_user(self):
        """
        save_user method saves user objects into user userslist
        """
        User.userslist.append(self)

    def delete_user(self):
        """
        delete_user method deletes a saved user from the userslist
        """
        User.userslist.remove(self)

    @classmethod
    def display_users(cls):
        """
        method that returns the userlist
        """
        return cls.userslist

    @classmethod
    def find_by_number(cls,number):
        """
        Method that takes in a username and returns a user that matches that number

        Args:
        number: Phone number to search for Returns: Contact of person that matches the number.
        """
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
    """
    Class that generates new instances of Credentials
    """
    accounts=[]
    def __init__(self,accountusername,accountname,accountpassword):
        """
        __init__ method that helps us define properties for our objectsself.

        Args:
        accountusername: New Credentials accountusername
        accountname: New Credentials accountname
        accountpassword: New Credentials accountpassword
        """
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
