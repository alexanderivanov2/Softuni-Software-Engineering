import re


class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


    @staticmethod
    def __is_username_valid(username):
        return 5 < len(username) < 15

    @staticmethod
    def __is_valid_password(password):
        return 8 <= len(password) and bool(re.search(r"\d", password)) and bool(re.search(r"[A-Z]", password))

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if self.__is_username_valid(username):
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if self.__is_valid_password(password):
            self.__password = password
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")


# profile_with_invalid_password = Profile('My_username', 'My-password')
#profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)