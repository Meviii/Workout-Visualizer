import src.model.Exercise as Exercise
import src.model.Workout as Workout
import src.repository.workout_repository as workout_repo

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
    
    