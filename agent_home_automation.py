from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from tools.home_automation import apri_porta, get_stato_porta, chiudi_porta
from tools.common import richiesta_informazioni

userdata = dotenv_values()

llm = init_chat_model(userdata.get("MODEL")
    , temperature=userdata.get("TEMPERATURE")
    , base_url=userdata.get("CEREBRAS_BASE_URL")
    , api_key=userdata.get("CEREBRAS_API_KEY")
    )

istruzioni = """
Ti chiami Loopo e sei un agente scorbutico in grado di gestire la domotica di casa. 

Dopo ogni azione eseguita (o anche se non ne hai eseguite), chiama SEMPRE il tool 
richiesta_informazioni per comunicare la risposta all'utente e raccogliere il prossimo input.
"""

agent = create_agent(model=llm
                     , tools=[apri_porta, chiudi_porta, get_stato_porta, richiesta_informazioni]
                     , system_prompt=istruzioni
                     )


risposta = agent.invoke({})

print(risposta)
