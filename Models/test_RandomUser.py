import unittest
from unittest.mock import patch
from Models.RandomUser import RandomUser


class TestRandomUser(unittest.TestCase):
    @patch('Models.RandomUser.requests.get')
    def test_fetch_user_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'results': [{
                'name': {'first': 'John', 'last': 'Doe'},
                'email': 'john.doe@example.com',
                'phone': '123-456-7890',
                'location': {'city': 'New York', 'country': 'USA'}
            }]
        }
        random_user = RandomUser()
        user = random_user.fetch_user()
        self.assertEqual(user['name']['first'], 'John')
        self.assertEqual(user['name']['last'], 'Doe')
        self.assertEqual(user['email'], 'john.doe@example.com')
        self.assertEqual(user['phone'], '123-456-7890')
        self.assertEqual(user['location']['city'], 'New York')
        self.assertEqual(user['location']['country'], 'USA')



    @patch('Models.RandomUser.requests.get')
    def test_fetch_user_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        random_user = RandomUser()
        with self.assertRaises(Exception) as context:
            random_user.fetch_user()
        self.assertTrue('Failed to retrieve data' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
