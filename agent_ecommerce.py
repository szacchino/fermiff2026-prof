from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

from models.ecommerce import Order,Item
from tools.common import richiesta_informazioni

userdata = dotenv_values()

llm = init_chat_model(userdata.get("GEMINI_MODEL")
    , temperature=userdata.get("TEMPERATURE")
    , api_key=userdata.get("GEMINI_API_KEY")
    , thinking_budget=0
    )


istruzioni = """
Ti chiami Loopo e sei un agente simpatico e gentile, esperto nell'estrarre informazioni dal prompt dell'utente.
Utilizza le informazioni disponibili nei messaggi dell'utente per 
inserire i dati nel data object col formato specificato.
Sii molto conciso e diretto. Chiedi all'utente le informazioni mancanti nel data object
ma prima di terminare richiedi all'utente una conferma.
Rispondi sempre nella stessa lingua dell'utente.
"""

agent = create_agent(
            model=llm
            , tools=[richiesta_informazioni]
            , system_prompt=istruzioni
            , response_format=Order
        )

# Starting agent

result = agent.invoke({
    "messages": [
        {
            "role": "user"
            , "content": "Saluta l'utente, quindi avvia la raccolta dei dati"
        }
    ]
})

print(result["structured_response"])