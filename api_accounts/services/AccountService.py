import os

import jwt
from dotenv import load_dotenv

from api_accounts.models import Account
from api_users.models import User

load_dotenv()


class AccountService:
    @classmethod
    def get_token(cls, data):
        return data[7:len(data) - 1]

    @classmethod
    def get_account_by_token(cls, token):
        jwt_options = {
            'verify_signature': False,
            'verify_exp': True,
            'verify_nbf': False,
            'verify_iat': True,
            'verify_aud': False
        }
        # payload = jwt.decode(
        #     jwt_options,
        #     token,
        #     "secret",
        # )
        payload = jwt.decode(jwt=token, options=jwt_options, key=os.getenv('SECRET_KEY'), algorithms=['HS256'])
        account = Account.objects.get(username=payload['user_id'])
        return account

    @classmethod
    def get_user_id(cls, account):
        user = User.objects.get(account=account)
        return user.id
