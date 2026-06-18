from database.db_connection import DB_connection


class AgentDB:

    def __init__(self):
        self.db = DB_connection()
        self.connection = self.db.get_connection()
        self.cursor = self.connection.cursor(dictionary=True)

    def create_agent(self,data):
        try:
            self.cursor.execute("""
                                insert INTO agents(name ,specialty,agent_rank) VALUES(%s,%s,%s)
                                """,(data["name"],data["specialty"],data["agent_rank"]))
            agent = self.get_agent_by_id(self.get_last_row_id())
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return agent
            return "error: somthing wrong"
        except Exception as e:
            print(e)
            return(e)
    
    def get_all_agents(self):
        self.agents = []
        try:
            self.cursor.execute("select * from agents")
            self.agents = self.cursor.fetchall()
        except Exception as e:
            raise e
        return self.agents
    
    def get_agent_by_id(self,id):
        self.agent = None
        try:
            self.cursor.execute("select * from agents where id = %s",(id,))
            self.agent = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return self.agent

    def update_agent(self,id,data):
        if id != data["id"]:
            return "wronge id"
        try:
            self.cursor.execute("UPDATE agents SET name = %s ,specialty = %s where id = %s",(data["name"] ,data["specialty"],id))
            self.connection.commit()
        except Exception as e:
            print(e)
        if self.cursor.rowcount > 0:
            return "agent update successful"
        return "c'ant update agent"
    
    def deactivate_agent(self,id):
        try:
            self.cursor.execute("UPDATE agents SET is_active = %s WHERE id = %s",(False,id))
            self.connection.commit()
        except Exception as e:
            print(e)

        if self.cursor.rowcount > 0:
            return "agent deactivate successful"
        return "somthing wronge"
    
    def increment_completed(self,id):
        try:
            self.cursor.execute("update agents set completed_missions = completed_missions + %s where id = %s",(1,id))
            self.connection.commit()
        except Exception as e:
            print(e)
        
        if self.cursor.rowcount > 0:
            return "increment completed successful"
        return "somthing wronge"
    
    def increment_failed(self,id):
        try:
            self.cursor.execute("update agents set failed_missions = failed_missions + 1 where id = %s",(id,))
            self.connection.commit()
        except Exception as e:
            print(e)
        if self.cursor.rowcount > 0:
            return "increment failed completed successful"
        return "somthing wronge"

    def get_agent_performance(self,id):
        self.agent_performance = {}
        try:
            self.cursor.execute("""
                            SELECT completed_missions as completed ,failed_missions as failed
                            FROM agents WHERE id = %s
                                """,(id,))
            self.agent_performance = self.cursor.fetchall()[0]
            self.cursor.execute("""
                                SELECT COUNT(status) as total FROM missions as total 
                                WHERE assigned_agent_id = %s AND status != "NEW"
                                """,(id,))
            self.total = self.cursor.fetchall()[0]["total"]
            self.agent_performance["total"] = self.total
            self.agent_performance["success_rate"] = round((self.agent_performance["completed"] / self.total) * 100 ,2)
        except Exception as e:
            print(e)
        return self.agent_performance

    def count_active_agents(self):
        try:
            self.cursor.execute("select count(*) as active_agents from agents where is_active = True")
            return self.cursor.fetchall()
        except Exception as e:
            print(e)

    def get_last_row_id(self):
        self.cursor.execute("select max(id) as id from agents")
        id = self.cursor.fetchall()[0]["id"]
        return id



