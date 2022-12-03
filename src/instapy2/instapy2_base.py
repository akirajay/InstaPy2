from .configuration import Configuration
import random
from urllib3.exceptions import HTTPError
from requests.exceptions import ProxyError
from instagrapi.exceptions import (
    GenericRequestError, ClientConnectionError,
    SentryBlock, RateLimitError, ClientThrottledError,
    ClientLoginRequired, PleaseWaitFewMinutes,
    ClientForbiddenError
)

from instagrapi import Client

import os

class InstaPy2Base:
    def login(self, username: str = None, password: str = None, verification_code: str = ''):
        
        self.session = Client()

        if not os.path.exists(path=os.getcwd() + f'{os.path.sep}/files'):
            os.mkdir(path=os.getcwd() + f'{os.path.sep}/files')

        if os.path.exists(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}{username}.json'):
            self.session.load_settings(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}{username}.json')
            logged_in = self.session.login(username=username, password=password, verification_code=verification_code)
        else:
            logged_in = self.session.login(username=username, password=password, verification_code=verification_code)
            self.session.dump_settings(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}{username}.json')

        print(f'[INFO]: Successfully logged in as: {self.session.username}.' if logged_in else f'[ERROR]: Failed to log in.')
        self.configuration = Configuration(session=self.session)
