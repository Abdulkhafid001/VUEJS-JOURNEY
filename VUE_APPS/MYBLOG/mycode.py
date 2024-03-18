# this file uses the secrets module to generate a random key to send to a user.
# if the key is correct allow user to reset password.
import secrets


class AppUtilities:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_secret_key(key_length):
        secret_key = secrets.token_urlsafe(key_length)
        return secret_key
