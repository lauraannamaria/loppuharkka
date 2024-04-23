from fastapi import FastAPI

app = FastAPI()

players = {
    0: {"id": 0, "name": "Laura"},
    1: {"id": 1, "name": "Emmi"},
    2: {"id": 2, "name": "Kikke"},
    3: {"id": 3, "name": "Kati"}
}


# Haetaan kaikki pelaajat
@app.get("/players")
def get_players():
    return [players[p] for p in players]

#Haetaan tietty pelaaja id:n perusteella
@app.get("/players/{id}")
def get_player(id: int):
    return players[id]