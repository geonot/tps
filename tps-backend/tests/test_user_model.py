import unittest
import sys
import os

# Add project root to sys.path to allow imports from app, models etc.
# This assumes 'tps-backend' is the project root for the backend app.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Now we can import from models
from models import User

# Mock db and app context if tests require them (not strictly for User model methods here)
# For more complex tests involving db interactions, you'd need to set up a test app and db.
# This simple test focuses only on password hashing logic within the User model itself,
# which does not directly require a live app or db connection.

class TestUserModel(unittest.TestCase):

    def test_password_setting(self):
        u = User(username='testuser', email='test@example.com')
        u.set_password('cat')
        self.assertIsNotNone(u.password_hash)
        self.assertNotEqual(u.password_hash, 'cat')
        # Test that it's a string (Werkzeug produces strings)
        self.assertIsInstance(u.password_hash, str)

    def test_password_checking(self):
        u = User(username='susan', email='susan@example.com')
        u.set_password('dog')
        self.assertTrue(u.check_password('dog'))
        self.assertFalse(u.check_password('cat'))

    def test_password_salts_are_random(self):
        # This test verifies that two different users with the same password
        # get different password hashes, due to the random salt used by Werkzeug.
        u1 = User(username='john', email='john@example.com')
        u1.set_password('password123')

        u2 = User(username='jane', email='jane@example.com')
        u2.set_password('password123')

        self.assertIsNotNone(u1.password_hash)
        self.assertIsNotNone(u2.password_hash)
        self.assertNotEqual(u1.password_hash, u2.password_hash)

if __name__ == '__main__':
    # This allows running the test file directly like `python tests/test_user_model.py`
    unittest.main()
