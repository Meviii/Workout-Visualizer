import src.model.Workout as Workout
import src.repository.workout_repository as workout_repo
import src.repository.exercise_repository as exercise_repo

def can_add_new_workout(workout_name, workout_day) -> bool:
    
    if workout_repo.find_by_name_and_day(workout_name, workout_day) != []:
        return False
    return True

def add_new_workout(workout_name, workout_day) -> bool:
    
    try: 
        workout_to_add = Workout.workout(workout_day, workout_name)
        workout_repo.save(workout_to_add)
        return True
    except Exception as e:
        return False

def add_exercises_for_workout(workout_id, exercises_of_workout):
    
    try:
        for exercise in exercises_of_workout:
            exercise.set_workout_id(workout_id)
            exercise_repo.save(exercise)
        
    except Exception as e:
        return False

def get_new_workout_id(workout_name, workout_day):
    try:
        result = workout_repo.find_id_by_name_and_day(workout_name, workout_day)
        workout_id = [i[0] for i in result if result != []]

    except Exception as e:
        return False
    
    if workout_id == []:
        return -1
    
    return workout_id[0]