## A simple telegram client based on [Telepot](https://github.com/nickoala/telepot) ( Telepot upgraded version )


# Example 💡

```
from TelegramApiClient import Client, Filters

client = Client("123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
bot = client.Bot()

@client.message(Filters.private)
def MessageHandler(message):
    message.reply(message.text)
    
client.run()
```


# Guide 📙


## Client
> Client.Bot() #*[Telepot basic bot](https://telepot.readthedocs.io/en/latest/reference.html#basic-bot)*

> client.run()

## Decorators
> Client.message(Filters or None)

> Client.edited_message(Filters or None)

> Client.callback_query(Filters or None)

> Client.inline_query(Filters or None)

## Filters
- Filter by message content

> Filters.text

> Filters.photo

> Filters.video

> Filters.document

> Filters.audio

> Filters.voice

> Filters.video_note

> Filters.sticker

> Filters.command(regular expression)

- Filter by chat

> Filters.private

> Filters.supergroup

> Filters.group

> Filters.channel

> Filters.chat_id(chat_id) #*chat id can be int or list*

> Filters.chat_name(chat_name) #*chat name can be str or list*

> Filters.chat_username(username) #*username can be str or list*

## Message object
- Variables

> message.text #*str*

> message.sender #*int*

> message.chat #*int*

> message.message_id #*int*

- Functions

> message.reply([ text or caption ], parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_markup=None, MEDIA)

> message.respond([ text or caption ], reply_to_message_id=None, parse_mode=None, disable_web_page_preview=None, disable_notification=None, reply_markup=None, MEDIA)

*MEDIA can be ( photo=None, sticker=None, document=None, voice=None, audio=None, video=None, video_note=None )*

> message.forward(to_chat_id, disable_notification=None)

> message.delete()

> message.edit([ text or caption ], parse_mode=None, disable_web_page_preview=None, reply_markup=None)

> message.edit_reply_markup(reply_markup)

> message.answer(text, alert=None)

# Reply markup
> Keyboard([['Plain text'],
           [dict(text='Phone', request_contact=True), dict(text='Location', request_location=True)]], resize_keyboard=None)

> RemoveKeyboard()

> InlineKeyboard([[dict(text='URL', url='https://core.telegram.org/')], [InlineKeyboardButton(text='Callback', callback_data='Callback data')], [dict(text='Switch to using bot inline', switch_inline_query='initial query')]])
