import random

import pandas as pd

from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from tools.common import richiesta_informazioni

userdata = dotenv_values()

# 1. Carica il file CSV con pandas
try:
    df = pd.read_csv('video_games.csv')
    print("`video_games.csv` caricato con successo.")
except FileNotFoundError:
    print("ERRORE: Il file `video_games.csv` non è stato trovato. Assicurati che sia stato scaricato correttamente.")
    # Create an empty DataFrame to prevent errors in subsequent operations if the file is missing
    df = pd.DataFrame(columns=["id","name","released","rating","rating_top","ratings_count","platforms"])
    print("Creazione di un DataFrame vuoto. Il server MCP potrebbe non funzionare come previsto.")

def get_count(column_name: str) -> int:
    """Restituisce il conteggio dei valori distinti per la colonna specificata."""
    if df.empty:
        return "Il dataset non è stato caricato o è vuoto. Impossibile recuperare i valori distinti."
    print(" === get_count " + column_name)
    if column_name in df.columns:
        # Dropna to avoid including NaN in distinct list, then convert to list of strings
        distinct_list = df[column_name].dropna().astype(str).unique().tolist()
        if distinct_list:
            return len(distinct_list)
    return -1

def get_distinct_values(column_name: str) -> list:
    """Restituisce un elenco dei valori distinti per la colonna specificata."""
    if df.empty:
        return "Il dataset non è stato caricato o è vuoto. Impossibile recuperare i valori distinti."
    print(" === get_distinct_values " + column_name)
    if column_name in df.columns:        
        # Dropna to avoid including NaN in distinct list, then convert to list of strings
        distinct_list = df[column_name].dropna().astype(str).unique().tolist()
        if distinct_list:
            return distinct_list
    return []

def get_column_names():
    """Restituisce un elenco dei nomi delle colonne del dataset."""
    print(" === get_column_names ")
    return df.columns.tolist() if not df.empty else []

llm = init_chat_model(userdata.get("MODEL")
    , temperature=userdata.get("TEMPERATURE")
    , base_url=userdata.get("CEREBRAS_BASE_URL")
    , api_key=userdata.get("CEREBRAS_API_KEY")
    )

istruzioni = """
Ti chiami Loopo e sei un chatbot simpatico e gentile.
Puoi interrogare il dataset dei videogiochi tramite i tool di cui disponi.
Rispondi sempre nella stessa lingua dell'utente.
Non terminare le richieste di informazioni fino a quando l'utente non digita 'esci', 'exit' o 'quit'. 
Dopo ogni tua risposta chiama obbligatoriamente il tool richiesta_informazioni per ottenere il prossimo input. 
"""

agent = create_agent(
            model=llm
            , tools=[get_count, get_column_names, get_distinct_values, richiesta_informazioni]
            , system_prompt=istruzioni
        )

result = agent.invoke({})

print(result["structured_response"] if "structured_response" in result else result)
print(result["messages"][-1].content)