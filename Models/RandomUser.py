import requests

class RandomUser:
    def __init__(self):
        self.api_url = 'https://randomuser.me/api/'

    def fetch_user(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            user_data = response.json()
            user = user_data['results'][0]
            return user
        else:
            raise Exception("Failed to retrieve data")

    def display_user(self, user):
        print(f"Name: {user['name']['first']} {user['name']['last']}")
        print(f"Email: {user['email']}")
        print(f"Phone: {user['phone']}")
        print(f"Location: {user['location']['city']}, {user['location']['country']}")
