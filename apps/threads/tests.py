from django.test import TestCase

# Create your tests here.
class ThreadTestCase(TestCase):

    def setUp(self):
        self.user1 = User()
    
    def test_user_exist_on_thread(self):
        thread = Thread()
        thread.add(self.user1)
        self.assertContains(self.thread.users, self.user1)
        