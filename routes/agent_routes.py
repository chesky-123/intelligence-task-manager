from fastapi import APIRouter ,HTTPException
from logs.logger_config import logger
from database.agent_db import AgentDB ,DB_connection

router = APIRouter(prefix="/agents")
connect = DB_connection()
db = AgentDB()

@router.post("/database")
def create_database():
    logger.info("POST /create_database")
    try:
        db = connect.create_database()
        logger.info("database created successful")
        return db
    except Exception as e:
        logger.error(e)


@router.post("")
def create_agent(data:dict):
    logger.info("POST /create_agent")
    try:
        agent =  db.create_agent(data)
        logger.info("agent created successful")
        return agent
    except Exception as e:
        logger.error(e)

@router.get("")
def get_all_agents():
    logger.info("GET /all_agents")
    try:
        agents = db.get_all_agents()
        logger.info("You managed to get the list")
        return agents
    except Exception as e:
        logger.error(e)

@router.get("{id}")
def get_agent_by_id(id:int):
    logger.info("GET /agent")
    try:
        agent = db.get_agent_by_id(id)
        logger.info("id :%s exists",(id,))
        return agent
    except Exception as e:
        logger.error(e)

@router.put("(id)")
def update_agent(id:int,data:dict):
    logger.info("PUT /update agent")
    try:
        agent = db.update_agent(id,data)
        logger.info("agent %s update successful",(id,))
        return agent
    except Exception as e:
        logger.error(e)

@router.put("(id)/deactivate")
def deactivate_agent(id:int):
    logger.info("PUT /deactivate_agent")
    try:
        agent = db.deactivate_agent(id)
        logger.info("agent update successful")
        return agent
    except Exception as e:
        logger.error(e)

@router.get("{id}/performance")
def get_agent_performance(id:int):
    logger.info("GET /agent performance")
    try:
        agent_performance = db.get_agent_performance(id)
        logger.info("agent performance return successful")
        return agent_performance
    except Exception as e:
        logger.error(e)


