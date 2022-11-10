import src.model.Exercise as Exercise
import src.model.Workout as Workout
import src.repository.workout_repository as workout_repo
import src.repository.exercise_repository as exercise_repo
from src.utility.convert_to_excel import MakeExcel

def clear_all():
    workout_repo.delete_all()
    exercise_repo.delete_all()

def get_workouts() -> list:
    
    all_workouts = workout_repo.find_all()

    return [Workout.workout(x[2], x[1], x[0]) for x in all_workouts]

def get_exercises() -> list:
    all_exercises = exercise_repo.find_all()
    
    return [Exercise.exercise(x[1], x[2], x[3], x[4]) for x in all_exercises]

def get_workout_id_by_name(workout_name, workout_day) -> int:
    result = workout_repo.find_id_by_name_and_day(workout_name, workout_day)[0][0]
    
    if result == []:
        return -1
    
    return result

def create_to_excel() -> bool:
    
    all_workouts = workout_repo.find_all()
    all_exercises = exercise_repo.find_all()
    
    if all_workouts == []:
        return False
    
    mak = MakeExcel("output.xlsx", all_workouts, all_exercises, "green")
    mak.make_excel()
    
    return True