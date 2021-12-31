import telegram 

bot = telegram.Bot(token='5057469943:AAEnqLxtpV5s3YcNdxcx0AfZ9dJ2RWuAoms')

# for i in bot.getUpdates():
#     print(i.message)

bot.sendMessage(chat_id= 5015230730, text="메세지 테스트!! ")