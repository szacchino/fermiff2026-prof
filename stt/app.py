from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model

userdata = dotenv_values()

llm = init_chat_model(userdata.get("MODEL")
    , temperature=userdata.get("TEMPERATURE")
    , base_url=userdata.get("CEREBRAS_BASE_URL")
    , api_key=userdata.get("CEREBRAS_API_KEY")
    )


app = Flask(__name__)

formato_prompt = """
    Rispondi sempre brevemente alla domanda dell'utente anche utilizzando le conversazioni precedenti.

    CONVERSAZIONI PRECEDENTI
    {memoria}

    DOMANDA DELL'UTENTE
    {domanda}
"""

formato_memoria = "domanda: {domanda} - risposta: {risposta}\n"

memoria = {"a": ""}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/comando", methods=["POST"])
def comando():
    data = request.json
    
    domanda = data.get("testo", "").lower()
    
    print(f"DOMANDA = {domanda}\n")


    prompt = formato_prompt.format(memoria=memoria["a"], domanda=domanda)

    print(f"\n---\n{prompt}\n---\n")

    risposta = llm.invoke(prompt)

    print(f"RISPOSTA = {risposta.content}\n")\
    
    memoria["a"] = memoria["a"] + formato_memoria.format(domanda=domanda, risposta=risposta.content)

    return jsonify({"risposta": risposta.content})

if __name__ == "__main__":
    app.run(debug=True, port=5000)