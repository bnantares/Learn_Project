# Работа с пользователями

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def check_user(user):
    if user:
        print('ok')
