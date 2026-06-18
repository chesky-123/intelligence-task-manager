from fastapi import APIRouter ,HTTPException
from logs.logger_config import logger
from database.mission_db import MissionDB ,DB_connection
from database import utils

router = APIRouter(prefix="/missions")
# connect = DB_connection()
db = MissionDB()


@router.post("")
def create_missions(data:dict):
    logger.info("POST /create_mission")
    try:
        if utils.check_location_and_difficulty(data["location"], data["difficulty"]):
            logger.info("start create missions")
            agent =  db.create_mission(data)
            logger.info("missions created successful")
            return agent
        raise HTTPException(status_code=400 , detail="difficulty and location must be betwin 0-10")
    except Exception as e:
        logger.error(e)

@router.get("")
def get_all_missions():
    logger.info("GET /all_missions")
    try:
        logger.info("starting")
        missions = db.get_all_mission()
        logger.info("You managed to get the list")
        return missions
    except Exception as e:
        logger.error(e)

@router.get("{id}")
def get_mission_by_id(id:int):
    logger.info("GET /mission")
    try:
        logger.info("starting...")
        mission = db.get_mission_by_id(id)
        logger.info("id :%s exists",(id,))
        return mission
    except Exception as e:
        logger.error(e)

@router.put("{id}/assign/{agent_id}")
def assign_mission(m_id:int,a_id:int):
    logger.info("PUT /assign_mission")
    try:
        if utils.check_assign:
            logger.info("assign_mission")
            assign = db.assign_mission(m_id ,a_id)
            logger.info("assign_mission successful")
            return assign
    except Exception as e:
        logger.error(e)

@router.put("{id}/start")
def start_mission(id:int):
    logger.info("PUT /start_mission")
    try:
        if utils.is_not_new:
            logger.info("start connect")
            mission = db.update_mission_status(id,"NEW")
            logger.info("mission started")
            return mission
    except Exception as e:
        logger.error(e)

@router.put("{id}/complete")
def complete_mission(id):
    logger.info("PUT /complete_mission")
    try:
        if utils.is_in_progress():
            logger.info("start to complete")
            mission = db.update_mission_status(id,"COMPLETED")
            logger.info("missio completed")
            return mission
    except Exception as e:
        logger.error(e)

@router.put("{id}/fail")
def fail_mission(id):
    logger.info("PUT /fail_mission")
    try:
        if utils.is_in_progress():
            logger.info("start to fail")
            mission = db.update_mission_status(id,"FAILED")
            logger.info("mission fail")
            return mission
    except Exception as e:
        logger.error(e)

@router.put("/{id}/cancel")
def cancel_mission(id):
    logger.info("PUT /cancel_mission")
    try:
        if utils.is_not_new(id):
            logger.info("start cancel mission")
            mission = db.update_mission_status(id,"CANCELLED")
            logger.info("miission canceled")
            return mission
    except Exception as e:
        logger.error(e)




