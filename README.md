# Progetto Futuro 2026 - ITT E. Fermi Francavilla Fontana

1. creare un file chiamato `.gitignore`
2. modificare il file aggiungendo
   ```
   .env
   .venv/
   ```
3. Creare un **virtual environment**
    ```bash
    python -m venv .venv
    ```
    in questo modo creiamo un virtual environment chiamato `.venv` in cui installare le nostre librerie.
4. Attivare il virtual environment:
   In windows:
   
    ```bash
    .venv/Scripts/activate
    ```
    
    In MacOS/Linux:

    ```bash
    source .venv/bin/activate
    ```
5. Creare un file chiamato `.env`
# Installazione delle librerie

**Dopo** aver attivato l'environment, eseguire

```
pip install -U langchain langchain-google-genai langchain-mistralai langchain-cerebras langchain-openai pytelegrambotapi python-dotenv
```

# Registrazione su Cerebras

Andare sul sito di [https://cloud.cerebras.ai](https://cloud.cerebras.ai) e:
1. autenticarsi
2. riempire il form conoscitivo
3. scegliere il piano Free
4. copiare il token con il bottone arancione

Sul sito di Cerebras, per conoscere i modelli disponibili, andare sulla pagina **Limits**, presente nel menu della pagina.
