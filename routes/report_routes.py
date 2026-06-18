from fastapi import APIRouter ,HTTPException
from logs.logger_config import logger
from database.mission_db import MissionDB 
from database import utils ,agent_db

router = APIRouter(prefix="/reports")
m_db = MissionDB()
a_db = agent_db.AgentDB()


@router.get("summary")
def get_summary():
    summary = {}
    logger.info("GET /summary")
    try:
        logger.info("start get summary")
        summary["active_agents_count"] = a_db.count_active_agents()[0]["active_agents"]
        summary["total_missions"] = m_db.count_all_missions()[0]["count(*)"]
        return summary
    except Exception as e:
        logger.error(e)




