from django.test import TestCase
from django.core.management import call_command


class TestPollTestCase(TestCase):
    def setUp(self):
        print('set up')

    def test_testpoll_succeed(self):
        self.assertEqual(call_command('testpoll', 'action'), 'testpoll')
