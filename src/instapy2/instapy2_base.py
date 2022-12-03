from .configuration import Configuration

from instagrapi import Client
from instagrapi.types import Media

from typing import List

import random, os
import random
import os
from urllib3.exceptions import HTTPError
from requests.exceptions import ProxyError
from instagrapi.exceptions import (
    GenericRequestError, ClientConnectionError,
    SentryBlock, RateLimitError, ClientThrottledError,
    ClientLoginRequired, PleaseWaitFewMinutes,
    ClientForbiddenError
)



class InstaPy2Base:
    def login(self, username: str = None, password: str = None, verification_code: str = '', proxy_lst: list = None):

        def next_proxy():
            return random.choices(proxy_lst)

        if len(proxy_lst) == 0:
            self.session = Client()
        else:
            print(next_proxy()[0])
            self.session = Client(proxy=next_proxy()[0])

        if not os.path.exists(path=os.getcwd() + f'{os.path.sep}/files'):
            os.mkdir(path=os.getcwd() + f'{os.path.sep}/files')

        if os.path.exists(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}{username}.json'):
            self.session.load_settings(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}{username}.json')
            logged_in = self.session.login(username=username, password=password, verification_code=verification_code)
        else:
            logged_in = self.session.login(username=username, password=password, verification_code=verification_code)
            self.session.dump_settings(path=os.getcwd() + f'{os.path.sep}files{os.path.sep}{username}.json')

        print(
            f'[INFO]: Successfully logged in as: {self.session.username}.' if logged_in else f'[ERROR]: Failed to log in.')
        self.configuration = Configuration(session=self.session)
