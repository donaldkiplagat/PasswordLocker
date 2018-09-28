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


class Credentials:
    accounts=[]
    def __init__(self,accountname,password):
        self.accountname = accountname
        self.password = TestPassword

    def save_account(self):
        Credentials.accounts.append(self)

    def delete_account(self):
        Credentials.accounts.remove(self)

    @classmethod
    def display_accounts(cls):
        return cls.accounts
