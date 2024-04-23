from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

players = {
    0: {"id": 0, "name": "Laura"},
    1: {"id": 1, "name": "Emmi"},
    2: {"id": 2, "name": "Kikke"},
    3: {"id": 3, "name": "Kati"}
}

class PlayerBase(BaseModel):
    name: str

class PlayerDB(PlayerBase):
    id: int

#Luodaan uusi pelaaja
@app.post("/players", status_code=status.HTTP_201_CREATED)
def create_player(player_in: PlayerBase):
    new_id = max(players.keys()) + 1
    player = PlayerDB(**player_in.model_dump(), id= new_id)
    players[new_id] = player.model_dump()
    return player


# Haetaan kaikki pelaajat
@app.get("/players", response_model=list[PlayerDB])
def get_players():
    return [players[p] for p in players]

#Haetaan tietty pelaaja id:n perusteella
@app.get("/players/{id}", response_model=PlayerDB)
def get_player(id: int):
    return players[id]

# Voidaan poistaa pelaaja
@app.delete("/players/{id}")
def delete_player(id: int):
    if id not in players:
        raise HTTPException(status_code=404, detail='Id not found')
    del players[id]
    return {'message': f'Player with id: {id} deleted'}
