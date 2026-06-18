from fastapi import APIRouter ,HTTPException
from logs.logger_config import logger
from database.mission_db import MissionDB ,DB_connection

router = APIRouter(prefix="/missions")
# connect = DB_connection()
db = MissionDB()


@router.post("")
def create_missions(data:dict):
    logger.info("POST /create_mission")
    try:
        agent =  db.create_mission(data)
        logger.info("missions created successful")
        return agent
    except Exception as e:
        logger.error(e)

@router.get("")
def get_all_missions():
    logger.info("GET /all_missions")
    try:
        missions = db.get_all_mission()
        logger.info("You managed to get the list")
        return missions
    except Exception as e:
        logger.error(e)

@router.get("{id}")
def get_mission_by_id(id:int):
    logger.info("GET /mission")
    try:
        mission = db.get_mission_by_id(id)
        logger.info("id :%s exists",(id,))
        return mission
    except Exception as e:
        logger.error(e)

@router.put("{id}/assign/{agent_id}")
def assign_mission(m_id:int,a_id:int):
    pass






