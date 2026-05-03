"""
Unit tests for the CI/CD Final Project Flask application
"""
import unittest
from service.routes import app


class TestRoutes(unittest.TestCase):
    """Test cases for Flask routes"""

    def setUp(self):
        """Set up test client"""
        self.client = app.test_client()
        self.client.testing = True

    def test_index(self):
        """Test root endpoint returns 200"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        """Test health endpoint returns OK"""
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data["status"], "OK")


if __name__ == "__main__":
    unittest.main()
