import random
from fastmcp import FastMCP
import pandas as pd

# 1. Carica il file CSV con pandas
try:
    df = pd.read_csv('video_games.csv')
    print("`video_games.csv` caricato con successo.")
except FileNotFoundError:
    print("ERRORE: Il file `video_games.csv` non è stato trovato. Assicurati che sia stato scaricato correttamente.")
    # Create an empty DataFrame to prevent errors in subsequent operations if the file is missing
    df = pd.DataFrame(columns=['Name', 'Platform'])
    print("Creazione di un DataFrame vuoto. Il server MCP potrebbe non funzionare come previsto.")

# Create an MCP server
mcp = FastMCP(
    name="HelpfulAssistant",
    instructions=""" Questo server ha accesso a un dataset di videogiochi e può rispondere a domande sui nomi dei giochi e le piattaforme disponibili, oppure averne un count. """
    )


# Add an addition tool
@mcp.tool()
def get_count(column_name: str) -> int:
    """Restituisce il conteggio dei valori distinti per la colonna specificata.
    """
    if df.empty:
        return "Il dataset non è stato caricato o è vuoto. Impossibile recuperare i valori distinti."
    print(df.columns)
    if column_name in df.columns:
        # Dropna to avoid including NaN in distinct list, then convert to list of strings
        distinct_list = df[column_name].dropna().astype(str).unique().tolist()
        if distinct_list:
            return len(distinct_list)
    return -1

@mcp.tool()
def get_distinct_values(column_name: str) -> list:
    """Restituisce un elenco dei valori distinti per la colonna specificata.
    """
    if df.empty:
        return "Il dataset non è stato caricato o è vuoto. Impossibile recuperare i valori distinti."
    print(df.columns)
    if column_name in df.columns:        
        # Dropna to avoid including NaN in distinct list, then convert to list of strings
        distinct_list = df[column_name].dropna().astype(str).unique().tolist()
        if distinct_list:
            return distinct_list
    return []

@mcp.tool()
def get_column_names():
    """Restituisce un elenco dei nomi delle colonne del dataset."""
    return df.columns.tolist() if not df.empty else []

@mcp.tool()
def get_rows(filter: str) -> list:
    """ Filtra e restituisce le righe del dataset in base a una Espressione di filtro in sintassi Pandas query(). """
    if not df.empty and filter != []:
        filter = filter.replace("\n", " ").replace("\r", " ").replace("'AND", "' AND").replace("'OR", "' OR").replace("'and", "' and").replace("'or", "' or")
        # Filter the DataFrame based on the provided filter (case-insensitive)
        risultato = df.query(filter)
        print(risultato[['name', 'platforms', 'released']])
        return risultato.values.tolist()
    return []

# Run with streamable HTTP transport
if __name__ == "__main__":
    print(f"Il server MCP è in esecuzione all'indirizzo: http://127.0.0.1:8000/mcp/")
    # input("Premi Invio per avviare il server MCP...")
    # mcp.run(transport="streamable-http")
    mcp.run(
        transport="http",
        host="0.0.0.0",           # Bind to all interfaces
        port=8000
    )
