import string
import src.database.sqlite_queries as db
import src.model.Workout as model

TABLE = "workouts"
connection = db.create_connection()
cur = connection.cursor()

def save(workout):
    db.sql_add_query(table = TABLE, values = (workout.name, workout.day), columns = ("name", "day"))

def delete_by_id():
    db.sql_delete_query(table = TABLE)

def update_by_id():
    pass

def find_by_name(workout_name):
    results = []
    
    try:
        cur.execute(f"SELECT * FROM {TABLE} WHERE name = ?", (str(workout_name),))
        results = cur.fetchall()
        
    except Exception as e:
        print(f"Error: {e}")

    return results

def find_id_by_name_and_day(workout_name, workout_day) -> string:
    results = []
    
    try:
        cur.execute(f"SELECT ID FROM {TABLE} WHERE name = ? and day = ?", (str(workout_name), str(workout_day)))
        results = cur.fetchall()
        
    except Exception as e:
        print(f"Error: {e}")

    return results

def find_by_id():
    pass

def find_all() -> list():
    return db.sql_select_all_query(TABLE)

def delete_all() -> list():
    return db.sql_delete_all_query(TABLE)