
    רקע:
        יצירת מערכת לניהול סוכנים ומשימות
        המערכת תדע להוסיף סוכנים ומשימות ולהוריד 
        לחשב רמת סיכון למשימה ולפי זה לשייך משימות 
        לסוכנים ולבדוק התקדמות 

    מבנה תיקיות:

        intelligence-task-manager/
        ├── database/
        │ ├── db_connection.py
        │ ├── agent_db.py
        │ └── mission_db.py
        | |-- utils.py
        ├── README.md
        ├── requirements.txt
        └── .gitignore

    :agents מבנה טבלת

        |שדה | סוג | הערות
        |--- |--- |---
        | מזהה ייחודי |INT, AUTO_INCREMENT,PK | id 
        | שם הסוכן |VARCHAR | name
        |תחום התמחות | VARCHAR |specialty
        | TRUE :מחדל ברירת | BOOLEAN | is_active
        | 0 :מחדל ברירת | INT| completed_missions
        | 0 :מחדל ברירת |INT | failed_missions
        | בלבד Junior / Senior / Commander | ENUM / VARCHAR | agent_rank

   :missions מבנה טבלת 

        |שדה | סוג | הערות
        |--- |--- |---
        | מזהה ייחודי |INT, AUTO_INCREMENT,PK | id 
        | כותרת המשימה | VARCHAR | title
        | תיאור מפורט | TEXT | description
        | מיקום |VARCHAR | location
        | בלבד 10–1  | INT | difficulty
        | בלבד 10–1 | INT | importance
        | NEW :מחדל ברירת | VARCHAR | status
        | מחושב אוטומטית — לא מגיע מהמשתמש |VARCHAR | level_risk
        | שיוך עד NULL | INT | assigned_agent_id

   :connection_db מחלקת

   * אחראית לחיבור הפרויקט ל database
   * מתודת connect  מתחברת ל satabase 
   * מתודת create_database מייצרת database אם לא קיים
   * מתודת create_agents_table מייצרת טבלת agents אם לא קיים
   * מתודת create+missions_table מייצרת טבלת missions אם לא קיים

   מחלקת AgentDB:

        מתודה | תפקיד
        | :--- | :--- 
        create_agent(data) | יוצרת סוכן חדש ומחזירה את האובייקט של הסוכן 
        agents_all_get() | מחזירה רשימת כל הסוכנים
        get_agent_by_id(id) | None או ,ID לפי אחד סוכן מחזירה
        update_agent(id ,data) | )id לשנות אפשרות אין )השורה לכל UPDATE
        agent_deactivate(id) | מגדירה מצב סוכן ללא פעיל
        completed_increment(id) | מעדכן את כמות המשימות שהושלמו
        failed_increment(id) | מעדכן את כמות המשימות שנכשלו
        get_agent_performance(id) |  completed, failed, total, האלו המפתחות עם מילון מחזירה
        success_rate
        )שימו לב לחשב את הערך הזה rate_success - כמה באחוזים משימות
        הסתיימו בהצלחה מתוך הסך הכולל(
        agents_active_count() | מחזירה את מספר הסוכנים הפעילים

    מחלקת nissions:

        תפקיד |מתןדה
        |:--- |:---
        mission_create(data) | יצירת משימה חדשה ומחזירה את כל האובייקט
        missions_all_get() | מחזירה את כל המשימות
        get_mission_by_id(id) | None או ,ID לפי אחת משימה מחזירה
        assign_mission(m_id ,a_id) | מייכת משימה לסוכן
        assign_mission_statu(id ,status) | סטטוס שינוי לכל משמשת
        get_open_missions_by_agent(id) | סוכן של ASSIGNED/IN_PROGRESS משימות מחזירה
        missions_all_count() | סה"כ משימות
        status_by_count(status) | סופרת לפי סטטוס מסוים
        missions_open_count() | סופרת משימות פתוחות
        count_critical_missions() | משימות סופרת CRITICAL
        get_top_agent() | ביותר הגבוה completed_missions עם הסוכן




    חוקי המערכת:

        1 rank חייב להיות Commander / Senior / Junior — כל ערך אחר זורק שגיאה

        2 difficulty ו-importance חייבים להיות בין 1 ל10- — אחרת שגיאה.

        3 level_risk מחושב אוטומטית בעת יצירת משימה — המשתמש לא שולח אותו.

        4 סוכן עם False=active_is לא יכול לקבל משימות.

        5 סוכן לא יכול להחזיק יותר מ3- משימות פתוחות )PROGRESS_IN / ASSIGNED )במקביל.

        6 אם CRITICAL=level_risk — רק סוכן בדרגת Commander יכול לקבל את המשימה.

        7 ניתן לשייך רק משימה בסטטוס NEW. לאחר שיוך: ASSIGNED=status.

        8 ניתן להתחיל רק משימה בסטטוס ASSIGNED. לאחר: PROGRESS_IN=status.

        9 ניתן לסיים רק משימה. PROGRESS_IN ולשנות לסטטוס completed or failed

        10 ניתן לבטל רק משימה בסטטוס NEW או ASSIGNED — אחרת שגיאה.

    הוראות הרצה:

    להרצת ה Docker :
                    docker run -d --name intelligence-mysql -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=Intelligence_db -p 3306:3306 mysql:8.0

    להרצת שכבת ה DB:
            להרצת agents:
                py .\agent_db.py
            להרצת missions:
                py .\mission_db.py


    רשימת Endpoints:

       Agents endpoints: 

           Method |  Endpoint |   תיאור   
        [ POST] | agents/ | יצירת סוכן חדש 
        [ GET] | agents/ |כל הסוכנים 
        ]GET[ /agents/{id} ID לפי סוכן
        ]PUT[ /agents/{id} סוכן עדכון
        ]PUT[ /agents/{id}/deactivate סוכן השבתת
        ]GET[ /agents/{id}/performance סוכן ביצועי

    Missions endpoints:

        [ POST] |  missions/ | משימה יצירת
        [ GET] | missions/ | כל המשימות 
        ]GET[ | /missions/{id} | ID לפי משימה
        ]PUT[ | /missions/{id}/assign/{agent_id} | לסוכן שיוך
        ]PUT[ | /missions/{id}/start | משימה התחלת
        ]PUT[ | /missions/{id}/complete | בהצלחה סיום
        ]PUT[ | /missions/{id}/fail | בכישלון סיום
        ]PUT[ | /missions/{id}/cancel | משימה ביטול

    Reports endpoints:

        [ GET] | summary/reports/ | דוח כללי של המערכת 
        ]GET[ | /reports/missions-by-status | סטטוס לפי משימות
        ]GET[ | /reports/top-agent )get_top_agent( | המצטיין הסוכן








