import unittest
from user import User
from user import Credentials

class TestUser(unittest.TestCase):
    """
    Test class that defines test cases for the User Class behaviours
    """
    def setUp(self):
        """
        Set up method to run before each test cases
        """
        self.newuser=User("Donald","Kiplagat","donaldkiplagat","donald54611")

    def tearDown(self):
        User.userslist=[]

    def test_init(self):
        self.assertEqual(self.newuser.firstname,"Donald")
        self.assertEqual(self.newuser.lastname,"Kiplagat")
        self.assertEqual(self.newuser.username,"donaldkiplagat")
        self.assertEqual(self.newuser.password,"donald54611")

    def test_save_user(self):
        self.newuser.save_user()
        self.assertEqual(len(User.userslist),1)

    def test_save_multiple_users(self):
        self.newuser.save_user()
        testuser= User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()
        self.assertEqual(len(User.userslist),2)


    def test_delete_user(self):
        self.newuser.save_user()
        testuser= User("Anne","Mwangi","072319213","annemwangi@gmail.com")
        testuser.save_user()
        self.newuser.delete_user()
        self.assertEqual(len(User.userslist),1)


    def test_display_all_users(self):
        self.assertEqual(User.display_users(),User.userslist)


    def test_find_user_by_number(self):
        self.newuser.save_user()
        testuser=User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()

        found_user = User.find_by_number("TestPassword")
        self.assertEqual(found_user.password,testuser.password)

    def test_user_exists(self):
        self.newuser.save_user()
        testuser=User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()

        user_exists= User.user_exist("TestUsername")
        self.assertTrue(user_exists)




class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.newaccount = Credentials("donaldkiplagat","Instagram","donald123")

    def tearDown(self):
        Credentials.accounts=[]

    def test_init(self):
        self.assertEqual(self.newaccount.accountusername,"donaldkiplagat")
        self.assertEqual(self.newaccount.accountname,"Instagram")
        self.assertEqual(self.newaccount.accountpassword,"donald123")


    def test_save_account(self):
        self.newaccount.save_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_save_multiple_accounts(self):
        self.newaccount.save_account()
        testaccount=Credentials("TestUsername","TestAccount","Password")
        testaccount.save_account()
        self.assertEqual(len(Credentials.accounts),2)

    def test_delete_account(self):
        self.newaccount.save_account()
        testaccount=Credentials("donaldkiplagat","Twitter","twitter123")
        testaccount.save_account()
        self.newaccount.delete_account()
        self.assertEqual(len(Credentials.accounts),1)

    def test_display_all_accounts(self):
        self.assertEqual(Credentials.display_accounts(),Credentials.accounts)

    def test_find_user_by_number(self):
        self.newaccount.save_account()
        testaccount=Credentials("TestUsername","TestAccount","Password")
        testaccount.save_account()

        found_account = Credentials.find_by_number("TestUsername")
        self.assertEqual(found_account.accountusername,testaccount.accountusername)


if __name__ == '__main__':
    (unittest.main())
