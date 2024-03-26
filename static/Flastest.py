import unittest
from unittest.mock import patch
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    @patch('app.py')
    def test_index_route_data(self, mock_df):
        # Mocking the DataFrame to avoid dependency on external data
        mock_df.read_csv.return_value = {
            'Crime type': ['Theft', 'Assault'],
            'Last outcome category': ['Under investigation', 'Arrest']
        }

        response = self.app.get('/')
        self.assertIn(b'Crime Type Distribution', response.data)
        self.assertIn(b'Last Outcome Category Distribution', response.data)
        self.assertIn(b'Relationship between Total outcome category and Location', response.data)

if __name__ == '__main__':
    unittest.main()
