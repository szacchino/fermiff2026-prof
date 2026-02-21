from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from tools import apri_porta, get_stato_porta, chiudi_porta, richiesta_informazioni

userdata = dotenv_values()

llm = init_chat_model(userdata.get("MODEL")
    , temperature=userdata.get("TEMPERATURE")
    , base_url=userdata.get("BASE_URL")
    , api_key=userdata.get("CEREBRAS")
    )

istruzioni = """
Ti chiami Loopo e sei un agente scorbutico, in grado di gestire la domotica di casa. 

Dopo ogni azione eseguita (o anche se non ne hai eseguite), chiama SEMPRE il tool 
richiesta_informazioni per comunicare la risposta all'utente e raccogliere il prossimo input.
"""
messages = []


agent = create_agent(llm
                     , tools=[apri_porta, chiudi_porta, get_stato_porta, richiesta_informazioni]
                     , system_prompt=istruzioni
                     )

# oggi fa caldo in casa? c'è qualcosa che puoi fare?
risposta = agent.invoke({})

print(risposta)
