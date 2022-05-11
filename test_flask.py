from unittest import TestCase
from server import app
from model import connect_to_db, db, example_data
from flask import session

# class FlaskTestsDatabase(TestCase):
#     """Flask tests."""

#     def setUp(self):
#         """Stuff to do before every test."""
        
#         # Get the Flask test client
#         self.client = app.test_client()

#         # Show Flask errors that happen during tests
#         app.config['TESTING'] = True

#         # Connect to test database
#         connect_to_db(app, "postgresql:///testdb")

#         # Create tables and add sample data
#         db.create_all()
#         example_data()

#     def tearDown(self):
#         """Do at end of every test."""

#         db.session.remove()
#         db.drop_all()
#         db.engine.dispose()

class FlaskTestsLogInLogOut(TestCase):  # Bonus example. Not in lecture.
    """Test log in and log out."""

    def setUp(self):
        """Before every test"""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        """Test log in form."""

        with self.client as c:
            result = c.post('/login',
                            data={'email': 'test@test.com', 'password': 'test'},
                            follow_redirects=True
                            )
            self.assertEqual(session['logged_in_user_id'], '1')
            self.assertIn(b"Currently logged in as test@test.com!", result.data)

    def test_logout(self):
        """Test logout route."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess['logged_in_user_id'] = '1'

            result = self.client.get('/logout', follow_redirects=True)

            self.assertNotIn(b'logged_in_user_id', session)
            self.assertIn(b'Logged Out', result.data)
      


if __name__ == "__main__":
    import unittest

    unittest.main()