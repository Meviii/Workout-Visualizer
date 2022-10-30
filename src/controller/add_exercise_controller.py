import src.model.Exercise as Exercise
import src.model.Workout as Workout
import src.repository.workout_repository as workout_repo
import src.repository.exercise_repository as exercise_repo
import logging

def get_workouts() -> list:
    
    all_workouts = workout_repo.find_all()
    return [Workout.workout(x[1], x[2], x[0]) for x in all_workouts]
    
def add_new_exercise(exercise_name, exercise_sets, exercise_reps, exercise_workout_string) -> bool:

    workout_name, workout_day = _workout_string_tokeniser(exercise_workout_string)
    
    workout_id = workout_repo.find_id_by_name_and_day(workout_name = workout_name, workout_day = workout_day)

    exercise_to_add = Exercise.exercise(exercise_name, exercise_sets, exercise_reps, workout_id[0][0])
    
    try:
        exercise_repo.save(exercise_to_add)
        return True
    except Exception as e:
        print(e)
    
    return False

def _workout_string_tokeniser(string):
    mid = 0
    for i in string.split():
        if i.lower() == "on":
            break
        mid += 1
    
    string_builder = ""
    name = string.split()[:mid]
    day = (string.split()[mid+1:])
    for i,v in enumerate(name):
        if i == len(name) - 1:
            string_builder += v    
        else:
            string_builder += v + " "
    name = string_builder
    
    string_builder = ""
    for i,v in enumerate(day):
            string_builder += v
    day = string_builder
    
    return (name, day) 
