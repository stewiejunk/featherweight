from fastapi import FastAPI
from endpoints import home, ping, search
import uvicorn

app = FastAPI()

app.include_router(home.router)
app.include_router(ping.router)
app.include_router(search.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
