from database.mission_db import MissionDB
from database.agent_db import AgentDB
from fastapi import HTTPException

missions = MissionDB()
agents = AgentDB()


def check_location_and_difficulty(location:int,difficulty:int):
    if 0 < location < 10 and 0 < location < 10:
        return True
    return

def check_assign(id,agent_id):
    all_missions = missions.get_all_mission()
    all_agents = agents.get_all_agents()
    is_mission = False
    is_agent = False
    is_new = False
    is_active = False
    is_thri_open = True
    is_CRITICAL = False
    is_comender = False
    for mission in all_missions:
        if mission["id"] == id:
            is_mission = True
            if mission["status"] == "NEW":
                is_new = True
            if mission["is_active"] == True:
                is_active = True
            if mission["status"] == "CRITICAL":
                is_CRITICAL = True

    for agent in all_agents:
        if agent["assigned_agent_id"] == agent_id:
            is_agent = True
            if missions.get_open_missions_by_agent(agent_id) < 3:
                is_thri_open = False
            if is_CRITICAL:
                if agent["agent_rank"] == "Commander":
                    is_comender = True

    if not is_mission:
        raise HTTPException(status_code=404 ,detail="Mission not found")
    if not is_agent:
        raise HTTPException(status_code=404 ,detail="Agent not found")
    if not is_new:
        raise HTTPException(status_code=400 ,detail="Mission not available")
    if not is_active:
        raise HTTPException(status_code=400 ,detail="Agent is not active")
    if is_thri_open:
        raise HTTPException(status_code=400 ,detail="Agent has reached maximum missions")
    if not is_comender:
        raise HTTPException(status_code=400 ,detail="Only Commander can handle critical missions")
    return True

def is_not_new(id):
    mission = missions.get_mission_by_id(id)
    if mission["status"]:
        return True
    raise HTTPException(status_code=400 ,detail="Mission not available")

def is_in_progress(id):
    mission = missions.get_mission_by_id(id)
    if mission["status"] == "PROGRESS_IN":
        return True
    raise HTTPException(status_code=400 ,detail="Mission not available")






