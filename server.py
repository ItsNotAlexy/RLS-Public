import fastapi
import uvicorn
from src.api.oauth import Oauth

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/whitelist/{player}/{id}")
async def whitelist(player:str, id:int):
    auth = Oauth(player, id)

    if auth.is_whitelisted():
        return {"message": f"{player} Is Whitelisted ✅", "id": id}
    else:
        return {"message": f"{player} Is Not Whitelisted ❌", "error_code": 404}
    
@app.get("/api/whitelist/add/{player}/{id}")
async def add_whitelist(player:str, id:int):
    auth = Oauth(player, id)

    if auth.is_whitelisted():
        return {"message": f"{player} Is Already Whitelisted ✅", "id": id}
    else:
        auth.add_whitelisted()
        return {"message": f"{player} Has Been Whitelisted ✅", "id": id}
    
@app.get("/api/whitelist/remove/{player}/{id}")
async def remove_whitelist(player:str, id:int):
    auth = Oauth(player, id)

    if auth.is_whitelisted():
        auth.remove_whitelisted()
        return {"message": f"{player} Has Been Removed From The Whitelist ✅", "id": id}
    else:
        return {"message": f"{player} Is Not Whitelisted ❌", "error_code": 404}
    
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
