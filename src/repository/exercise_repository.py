import src.database.sqlite_queries as db
import src.model.Workout as model

TABLE = "exercises"

def save(exercise):
    db.sql_add_query(table = TABLE, values = (exercise.name, str(exercise.sets), str(exercise.reps), str(exercise.workout_id)), columns = ("name", "sets", "reps", "workout_id"))

def delete_by_id():
    pass

def update_by_id():
    pass

def find_by_id():
    pass

def find_all() -> list():
    return db.sql_select_all_query(TABLE)

def delete_all():
    return db.sql_delete_all_query(TABLE)