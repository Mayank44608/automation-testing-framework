class LoginPage:
    def __init__(self):
        self.username_field = "username"
        self.password_field = "password"
        self.login_button = "login"

    def login(self, username, password):
        return f"Logging in with {username}"
