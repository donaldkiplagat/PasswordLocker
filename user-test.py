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
        """
        tearDown method that does clean up after each test case has been return
        """
        User.userslist=[]

    def test_init(self):
        """
        test_init case to test if the object is initialized properly
        """
        self.assertEqual(self.newuser.firstname,"Donald")
        self.assertEqual(self.newuser.lastname,"Kiplagat")
        self.assertEqual(self.newuser.username,"donaldkiplagat")
        self.assertEqual(self.newuser.password,"donald54611")

    def test_save_user(self):
        """
        test_save_user test case to test if the user object is saved into the userslist
        """
        self.newuser.save_user()
        self.assertEqual(len(User.userslist),1)

    def test_save_multiple_users(self):
        """
        test_save_multiple_users to test if we can save multiple user to our userslist
        """
        self.newuser.save_user()
        testuser= User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()
        self.assertEqual(len(User.userslist),2)


    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user list
        """
        self.newuser.save_user()
        testuser= User("Anne","Mwangi","072319213","annemwangi@gmail.com")
        testuser.save_user()
        self.newuser.delete_user()
        self.assertEqual(len(User.userslist),1)


    def test_display_all_users(self):
        """
        method that returns a list of all users saved
        """
        self.assertEqual(User.display_users(),User.userslist)


    def test_find_user_by_number(self):
        """
        test to check if we can find a user by their password and display the user
        """

        self.newuser.save_user()
        testuser=User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()

        found_user = User.find_by_number("TestPassword")
        self.assertEqual(found_user.password,testuser.password)

    def test_user_exists(self):
        """
        test to check if we can return a Boolean if we cannot find the contact
        """
        self.newuser.save_user()
        testuser=User("TestFirst","TestLast","TestUsername","TestPassword")
        testuser.save_user()

        user_exists= User.user_exist("TestUsername")
        self.assertTrue(user_exists)




class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
        Test class that defines test cases for the Credentials Class behaviours
        """
        self.newaccount = Credentials("donaldkiplagat","Instagram","donald123")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has been return
        """
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
