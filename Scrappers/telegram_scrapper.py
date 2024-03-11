from dotenv import load_dotenv
from os import getenv
from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputMessagesFilterPhotos


load_dotenv()
# Remember to use your own values from my.telegram.org!
api_id = getenv("TELEGRAM_API_ID")
api_hash = getenv("TELEGRAM_API_HASH")
client = TelegramClient('anon', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())
    username = me.username
    print(username)

    # message = await client.send_message(
    #     'me',
    #     'This message has **bold**, `code`, __italics__ and '
    #     'a [nice website](https://example.com)!',
    #     link_preview=False
    # )
    prueba = await client.get_entity('t.me/publicidad_ventas_cuba')
    all_messages = await client.get_messages(prueba, 100)

    print(all_messages[0].stringify())

with client:
    client.loop.run_until_complete(main())