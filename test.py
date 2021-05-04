from tele_frame import Message, Connection

if __name__ == "__main__":

    data = {
        'update_id': 977246057,
        'message':     {
            "message_id": 80,
            "from": {
                "id": 11111111,
                "is_bot": False,
                "first_name": "\\u26a1",
                "language_code": "en"
            },
            "chat": {
                "id": 11111111,
                "first_name": "\\u26a1",
                "type": "private"
            },
            "text": "this is test",
            "date": 1618958614,
            "document": {
                "file_name": "file.json",
                "mime_type": "application/json",
                "file_id": "BQACAgQAAxkBAANQYH9ZFE7sAHkL7Uu7A5ecI664AAhoLAALFv_hTduBxHABbb0eBA",
                "file_unique_id": "AgADgsAsW_-FM",
                "file_size": 98
            },
            "reply_to_message":
            {
                "message_id": 79,
                "from": {
                    "id": 11111111,
                    "is_bot": False,
                    "first_name": "\\u26a1",
                    "language_code": "en"
                },
                "chat": {
                    "id": 11111111,
                    "first_name": "\\u26a1",
                    "type": "private"
                },
                "text": "this is test2",
                "date": 1618958613,
                "document": {
                    "file_name": "file.json",
                    "mime_type": "application/json",
                    "file_id": "BQACAgQAAxkBAANQYH9ZFE7sAHkL7Uu7A5ecI664AAhoLAALFv_hTduBxHABbb0eBA",
                    "file_unique_id": "AgADgsAsW_-FM",
                    "file_size": 98
                }
            }
        }
    }

    payam = Message()
    payam.load(data)
    print(payam)

    a = Connection('https://api.telegram.org',
        '1715241206:AAF8u4qrITgwE_JgapV5XvyFDotLvD8Q5YM')
    state,data = a.send('sendMessage',
        chat_id=10000000,
        text='test'
    )
    print(state, data)
