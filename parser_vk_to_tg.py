import vk
from constant import *
import telebot

bot = telebot.TeleBot(TG_TOKEN)
CHANNEL_NAME = ''

session = vk.AuthSession(app_id=APP_ID, user_login=USER_LOGIN, user_password=USER_PASSWORD)
api = vk.API(session)
photo = api.photos.get(owner_id=-1, album_id='wall', count=1)


for k in range(0, len(photo)):
     try:
         url = photo[k]['src_xxbig']
         bot.send_photo(CHANNEL_NAME, url)

         continue
     except KeyError:
         url = photo[k]['src_big']
         bot.send_photo(CHANNEL_NAME, url)

# if __name__ == '__main__':
#     bot.polling(none_stop=True)