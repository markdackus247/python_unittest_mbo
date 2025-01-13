from Models.RandomUser import RandomUser

if __name__ == "__main__":
    random_user = RandomUser()
    try:
        user = random_user.fetch_user()
        random_user.display_user(user)
    except Exception as e:
        print(e)