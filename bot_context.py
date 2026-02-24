import telebot
from dotenv import dotenv_values
from langchain.chat_models import init_chat_model

userdata = dotenv_values()

contesto = ""

with open("context.txt", "r") as file:
    contesto = file.read()

llm = init_chat_model(
    model = userdata["MODEL"]
    , api_key = userdata["CEREBRAS_API_KEY"]
    , base_url = userdata["CEREBRAS_BASE_URL"]
    , temperature = userdata["TEMPERATURE"]
)

bot = telebot.TeleBot(userdata["TELEGRAM"])

formato_prompt = """
    Rispondi usando il seguente contesto altrimenti rispondi che non lo sai.

    CONTESTO:
    {contesto}

    DOMANDA DELL'UTENTE:
    {domanda}
    """

@bot.message_handler(func=lambda message:True)
def risponditore(message):
    print(message)
    domanda = message.text
    user_id=message.from_user.id

    prompt = formato_prompt.format(domanda=domanda, contesto=contesto)

    risposta = llm.invoke(prompt)

    bot.reply_to(message, risposta.content)

bot.polling()