from db_connection import DB_connection


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
                                data["title"],data["description",data["location"],
                                data["difficulty"],data["importance"]])
            mission = self.get_mission_by_id(self.get_last_row_id())
            self.connection.commit()
            if self.cursor.rowcount > 0:
                return mission
            return "error: somthing wrong"
        except Exception as e:
            print(e)
            return e

    def get_mission_by_id(self,id):
        self.mission = None
        try:
            self.cursor.execute("select * from mission where id = %s",(id,))
            self.mission = self.cursor.fetchall()
        except Exception as e:
            print(e)
        return self.mission

    def get_last_row_id(self):
        self.cursor.execute("select max(id) as id from missions")
        id = self.cursor.fetchall()[0]["id"]
        return id


a = MissionDB()

print(a.create_mission({"title":"title_1","description":"description","location":"TLV","difficulty":2,"importance":1}))


