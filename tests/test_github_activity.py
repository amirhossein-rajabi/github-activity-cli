import unittest
from github_activity import fetch_user_activity

class TestGitHubActivity(unittest.TestCase):
    def test_invalid_user(self):
        events = fetch_user_activity("this_user_does_not_exist_123456789")
        self.assertEqual(events, [])  

if __name__ == '__main__':
    unittest.main()