stato_casa = {
    "porta": "CHIUSA"
}

def apri_porta():
    """Apre la porta di casa ed imposta lo stato della porta ad APERTA"""
    stato_casa["porta"] = "APERTA"

    print("CHIAMATO apri_porta")

    return "la porta è ora aperta"

def chiudi_porta():
    """Chiude la porta di casa ed imposta lo stato della porta a CHIUSA"""
    stato_casa["porta"] = "CHIUSA"

    print("CHIAMATO chiudi_porta")
    
    return "la porta è ora chiusa"

def get_stato_porta():
    """restituisce lo stato in cui si trova la porta di casa che può essere APERTA o CHIUSA"""
    print("CHIAMATO get_stato_porta")
    return stato_casa["porta"]