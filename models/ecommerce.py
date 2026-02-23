from pydantic import BaseModel, Field

# Definizione delle strutture dati
class Item(BaseModel):
  """Informazioni sull'articolo, rappresentano un articolo che un cliente desidera acquistare e la sua quantità”"""
  name: str = Field(description="Il nome dell'articolo")
  quantity: int = Field(description="La quantità dell'articolo; è necessario assicurarsi che l'utente specifichi una quantità precisa; evitare di interpretare richieste ambigue")

class Order(BaseModel):
    """Informazioni sull'ordine di un cliente."""
    name: str = Field(description="Il nome del cliente; è sufficiente il nome")
    email: str = Field(description="L'indirizzo e-mail del cliente")
    items: list[Item] = Field(description="Gli articoli che il cliente desidera acquistare")
    complete: bool = Field(description="Se l'ordine è completo o meno")
