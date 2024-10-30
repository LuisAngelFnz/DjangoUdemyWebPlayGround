from django.test import TestCase
from django.contrib.auth.models import User
from threads.models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1', email='user1@example.com', password='password'
        )
        self.user2 = User.objects.create_user(
            username='user2', email='user2@example.com', password='password'
        )
        self.user3 = User.objects.create_user(
            username='user3', email='user3@example.com', password='password'
        )

        self.thread = Thread.objects.create()

    def test_add_users_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.users.all()), 2)
    
    def test_filter_threads_by_users(self):
        self.thread.users.add(self.user1, self.user2)
        threads = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, threads)
    
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.find(self.user1, self.user2)
        self.assertIsNone(threads)
    
    def test_add_message_to_thread(self):
        self.thread.users.add(self.user1, self.user2)
        messageOne = Message.objects.create(user=self.user1, content='Hello, this is a message')
        messageTwo = Message.objects.create(user=self.user2, content='Hi, this is another message')
        self.thread.messages.add(messageOne, messageTwo)
        self.assertEqual(len(self.thread.messages.all()), 2)
    
    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1, self.user2)
        messageOne = Message.objects.create(user=self.user1, content='Hi, this is a message')
        messageTwo = Message.objects.create(user=self.user2, content='Hello, this is another message')
        messageThree = Message.objects.create(user=self.user3, content='Soy un espia, estoy viendo esto')
        self.thread.messages.add(messageOne, messageTwo, messageThree)
        self.assertEqual(len(self.thread.messages.all()), 2)
    
    def test_find_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)

    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.users.add(self.user1, self.user2)
        thread = Thread.objects.findOrCreate(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.findOrCreate(self.user1, self.user3)
        self.assertIsNotNone(thread)