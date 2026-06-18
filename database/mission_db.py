from database.db_connection import DB_connection


class MissionDB:

    def __init__(self):
        self.db = DB_connection()
        self.connection = self.db.get_connection()
        self.cursor = self.connection.cursor(dictionary=True)

    def create_mission(self,data):
        try:
            self.cursor.execute("""
                                INSERT INTO missions(title,description,location,difficulty,importance)
                                VALUES(%s,%s,%s,%s,%s)""",
                                data["title"],data["description"],data["location"],
                                data["difficulty"],data["importance"])
            mission = self.get_mission_by_id(self.get_last_row_id())
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return mission
            return "error: somthing wrong"
        except Exception as e:
            print(e)
            return e
        
    def get_all_mission(self):
        self.cursor.execute("select * from missions")
        return self.cursor.fetchall()

    def get_mission_by_id(self,id):
        mission = None
        try:
            self.cursor.execute("select * from missions where id = %s",(id,))
            mission = self.cursor.fetchone()
        except Exception as e:
            print(e)
        return mission | None
    
    def assign_mission(self,m_id,a_id):
        self.cursor.execute("""UPDATE missions set assigned_agent_id = %s 
                            where id = %s
                            """,(a_id,m_id))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return True
        return
    
    def update_mission_status(self,id,status):
        self.cursor.execute("update missions set status = %s where id = %s"
                            ,(status,id))
        self.connection.commit()
        if self.cursor.rowcount > 0:
            return True
        return
    
    def get_open_missions_by_agent(self,id:int):
        self.cursor.execute("select * from missions wher status = ASSIGNED or status = IN_PROGRESS")
        return self.cursor.fetchall()
    
    def count_all_missions(self):
        self.cursor.execute("select count(*) from missions")
        return self.cursor.fetchall()
    
    def count_by_status(self,status):
        self.cursor.execute("select count(*) from missions where status = %s",(status,))
        return self.cursor.fetchall()
    
    def count_open_missions(self):
        self.cursor.execute("select count(*) from missions where status = IN_PROGRESS or status = ASSIGNED")
        return self.cursor.fetchall()
    
    def count_critical_missions(self):
        self.cursor.execute("select count(*) from missions where status = CRITICAL")
        return self.cursor.fetchall()
    
    def get_top_agent(self):
        self.cursor.execute("")
    



    def get_last_row_id(self):
        self.cursor.execute("select max(id) as id from missions")
        id = self.cursor.fetchone()[0]["id"]
        return id



