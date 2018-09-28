import unittest
from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
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



if __name__ == '__main__':
    (unittest.main())
