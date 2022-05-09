"""Test suite for Foodie Guide"""

import server
from unittest import TestCase


class FoodyGuideIntegrationTest(TestCase):

    def setUp(self):
        
        #print("(setUp ran)")
        
        #Flask app has a test_client method on it, 
        #which returns a pretend web browser.
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_index(self):
        result = self.client.get("/")
        self.assertIn(b'<h3>Log In</h3>', result.data)

#Check if AJAX means testing the login page isn't possible with flask testing
    # def test_login(self):
    #     result = self.client.post("/login",
    #                                 data={"e-mail": "test@test.com","password": "test"},
    #                                 follow_redirects=True)
    #     self.assertIn(b"Currently logged in as test@test.com!", result.data)

    
if __name__ == '__main__':
    # If called like a script, run our tests
    import unittest
    unittest.main()