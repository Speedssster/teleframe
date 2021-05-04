from requests import post


class Connection():
    '''Simple one-time lazy Connection Model for requests'''

    url: str = ""

    def __init__(self, url: str, bot_token: str) -> None:
        '''instantiate a `Connection` object with `url`(telegram server) and
        `Bot Token`'''

        self.url = f'{url}/bot{bot_token}/'

    def send(self, method: str, **kwargs) -> tuple:
        '''Wrap & send new POST request by given `method` and `kwargs`.

        :param method: case-insensitive str from telegram bot api available methods.
        :param \*\*kwargs: Optional arguments that `method` takes.
        
        :return: `tuple(state <bool>, response <JSON-object>)`
        '''

        try:
            response = post(self.url + method, json=kwargs)
        except Exception as error:
            print(error)
            return (False, {'error': error})
        else:
            return (response.ok, response.json())
