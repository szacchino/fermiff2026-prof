import telebot
from dotenv import dotenv_values
from langchain.chat_models import init_chat_model


userdata = dotenv_values()

llm = init_chat_model(
    model = userdata["MODEL"]
    , api_key = userdata["CEREBRAS_API_KEY"]
    , base_url = userdata["CEREBRAS_BASE_URL"]
    , temperature = userdata["TEMPERATURE"]
)

bot = telebot.TeleBot(userdata["TELEGRAM"])

@bot.message_handler(func=lambda message:True)
def risponditore(message):
    print(message)
    domanda = message.text
    user_id=message.from_user.id

    risposta = llm.invoke(domanda)

    bot.reply_to(message, risposta.content)

bot.polling()