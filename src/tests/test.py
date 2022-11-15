def _sort_workout_by_day(workouts_to_sort, sorted_workouts = [], current_day = 0):
        
        MAX_DAY_COUNT = 7
        DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        
        # break
        if current_day == MAX_DAY_COUNT:
            return sorted_workouts
        
        # add to final list for current day
        for workout in workouts_to_sort:
            if str(workout[2]).lower() == DAYS[current_day]:
                sorted_workouts.append(workout)
        
        return _sort_workout_by_day(workouts_to_sort, sorted_workouts, current_day + 1)

print(_sort_workout_by_day([(12, 'Chest', 'Monday'), (13, 'Back', 'Tuesday')]))