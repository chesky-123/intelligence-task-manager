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
            self.connection.commit()
            mission = self.cursor.fetchall()
            return mission

        except Exception as e:
            print(e)



a = MissionDB()

print(a.create_mission({"title":"title_1","description":"description","location":"TLV","difficulty":2,"importance":1}))


