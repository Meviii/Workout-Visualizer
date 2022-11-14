import src.model.Exercise as Exercise
import src.model.Workout as Workout
import src.repository.workout_repository as workout_repo
import src.repository.exercise_repository as exercise_repo
from src.utility.convert_to_excel import MakeExcel
# from src.tests.TEST_convert_to_excel import MakeExcel

def clear_all():
    workout_repo.delete_all()
    exercise_repo.delete_all()

def get_workouts() -> list:
    
    all_workouts = workout_repo.find_all()

    return [Workout.workout(x[2], x[1], x[0]) for x in all_workouts]

def get_exercises() -> list:
    all_exercises = exercise_repo.find_all()
    
    return [Exercise.exercise(x[1], x[2], x[3], x[4]) for x in all_exercises]

def get_workout_id_by_name_and_day(workout_name, workout_day) -> int:
    try:
        result = workout_repo.find_id_by_name_and_day(workout_name, workout_day)
        workout_id = [i[0] for i in result if result != []]

    except Exception as e:
        return False
    
    if workout_id == []:
        return -1
    
    return workout_id[0]

def create_to_excel() -> bool:
    
    all_workouts = workout_repo.find_all()
    all_exercises = exercise_repo.find_all()
    
    # if workouts are empty
    if all_workouts == []:
        return False
    
    # if a workout has no exercises, return false
    for workout in all_workouts:
        cur_exercise_count = 0
        for exercise in all_exercises:
            if exercise[4] == workout[0]:
                cur_exercise_count += 1
        if cur_exercise_count == 0:
            return False
        
    mak = MakeExcel("output.xlsx", all_workouts, all_exercises, "green")
    mak.make_excel()
    
    return True

def delete_workout(workout_to_delete) -> bool:
    try:
        print(workout_to_delete.id)
        workout_repo.delete_by_id(workout_to_delete.id)
        return True
    except Exception as e:
        return False