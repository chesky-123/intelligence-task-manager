from fastapi import FastAPI
from routes import agent_routes,mission_routes
app = FastAPI()

app.include_router(agent_routes.router)
app.include_router(mission_routes.router)







