import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        self.newuser=User("Donald","Kiplagat","donaldkiplagat","donald54611")

        self.newaccount = Credentials("Instagram","donald123")

    def tearDown(self):
        User.userslist=[]
        Credentials.accounts=[]

    def test_init(self):
        self.assertEqual(self.newuser.firstname,"Donald")
        self.assertEqual(self.newuser.lastname,"Kiplagat")
        self.assertEqual(self.newuser.username,"donaldkiplagat")
        self.assertEqual(self.newuser.password,"donald54611")


        self.assertEqual(self.newaccount.accountname,"Instagram")
        self.assertEqual(self.newaccount.password,"donald123")


    def test_save_user(self):
        self.newuser.save_user()
        self.assertEqual(len(User.userslist),1)


        self.newaccount.save_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_save_multiple_users(self):
        self.newuser.save_user()
        testuser= User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()
        self.assertEqual(len(User.userslist),2)


        self.newaccount.save_account()
        testaccount=Credentials("TestAccount","TestPassword")
        testaccount.save_account()
        self.assertEqual(len(Credentials.accounts),2)

    def test_delete_user(self):
        self.newuser.save_user()
        testuser= User("Anne","Mwangi","072319213","annemwangi@gmail.com")
        testuser.save_user()
        self.newuser.delete_user()
        self.assertEqual(len(User.userslist),1)

        self.newaccount.save_account()
        testaccount=Credentials("Twitter","twitter123")
        testaccount.save_account()
        self.testaccount.delete_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_display_all_users(self):
        self.assertEqual(User.display_users(),User.userslist)

        self.assertEqual(Credentials.display_accounts(),Credentials.accounts)



if __name__ == '__main__':
    (unittest.main())
