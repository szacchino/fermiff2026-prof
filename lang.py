from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model

userdata = dotenv_values()

llm = init_chat_model(userdata.get("MODEL")
    , temperature=userdata.get("TEMPERATURE")
    , base_url=userdata.get("CEREBRAS_BASE_URL")
    , api_key=userdata.get("CEREBRAS_API_KEY")
    )

risposta = llm.invoke("Chi è Anders Hejlsberg e perché è importante per l'AI? Rispondi brevemente")

print (risposta.content)
