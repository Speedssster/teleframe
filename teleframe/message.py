from json import loads


class Message():
    '''implements Model Class to decode message from incoming update 
    requests.
    '''

    def __init__(self) -> None:
        # required
        self.id: int = 0
        self.sender_id: int = 0
        # optional
        self.text: str = ""
        self.mime_type: str = ""
        self.file_id: str = ""
        self.reply: object = None
        # state
        self._bool: bool = False
        self.has_text: bool = False
        self.has_file: bool = False
        self.has_replied: bool = False
        # exeption
        self.error: str = ""

    def load(self, body: bytes or dict) -> None:
        '''instantiate an `Message` object from update response body'''

        try:
            if not isinstance(body, dict):
                body = loads(body)
            if 'message' in body:
                body = body['message']
            self.id = int(body['message_id'])
            self.sender_id = int(body['from']['id'])
            if 'text' in body:
                self.text = str(body['text'])
                self.has_text = True
            if 'document' in body:
                self.file_id = body['document']['file_id']
                self.mime_type = body['document']['mime_type']
                self.has_file = True
            if 'reply_to_message' in body:
                self.reply = Message()
                self.reply.load(body['reply_to_message'])
                self.has_replied = True
        except KeyError as key:
            self.error = f'Key {key} not found in given body.'
        except Exception as error:
            self.error = error
        else:
            self._bool = True

    def __bool__(self) -> bool:
        '''Return `True` if object successfully loaded without error.'''

        return self._bool

    def __str__(self) -> str:
        if self:
            _ = f'\n- Message ID: {self.id}\n- Sender ID: {self.sender_id}'
            if self.has_text:
                _ += f'\n- Text: {self.text}'
            if self.has_file:
                _ += f'\n- File Type: {self.mime_type}\n- File ID: {self.file_id}'
            if self.has_replied:
                _ += f'\nReplied:{self.reply}'
            return _
        else:
            return f'Following error happends:\n{self.error}'
