import mysql.connector

class DB_connection:

    def __init__(self):
        self.config = {"host":"localhost",
                       "user":"root",
                       "password":"1234",
                       "database":"Intelligence_db"}
        self._connect = None

    def get_connection(self):
        if self._connect:
            return self._connect
        try:
            self._connect = mysql.connector.connect(**self.config)
            return self._connect
        except Exception as e:
            print(e)

    def create_database(self):
        self.connector = self.get_connection()
        self.cursor = self.connector.cursor(dictionary=True)
        self.cursor.execute("create database if not exists Intelligence_db")
        self.connector.commit()
        if self.cursor.rowcount > 0:
            return "database created successful"
        return "c'ant create database"
    
    def create_tablse(self):
        connector = self.get_connection()
        cursor = connector.cursor(dictionary=True)        
        cursor.execute("""
                            CREATE TABLE if not exists agents(id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(50) NOT NULL,
                            specialty VARCHAR(50) NOT NULL,
                            is_active BOOLEAN DEFAULT True,
                            completed_missions INT DEFAULT 0,
                            failed_missions int DEFAULT 0,
                            agent_rank ENUM ('Junior' ,'Senior' ,'Commander'))
                            """)
        
        cursor.execute("""
                    CREATE TABLE if NOT exists missions(id INT AUTO_INCREMENT PRIMARY KEY,
                    title VARCHAR(100),
                    description TEXT,
                    location VARCHAR(50),
                    difficulty INT ,
                    importance INT,
                    status VARCHAR(100) DEFAULT "NEW",
                    level_risk VARCHAR(100),
                    assigned_agent_id INT DEFAULT NULL)
                       """)
        
        connector.commit()
        return "two tables created successful"

       
         






