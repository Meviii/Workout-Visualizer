import string

class exercise:    
    def __init__(self, name, sets, reps, workout_id, id=None):
        
        self.id = id
        self.sets = sets
        self.name = name
        self.reps = reps
        self.workout_id = workout_id
    
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> string:
        return self.name
    
    def get_sets(self) -> int:
        return self.sets
    
    def get_reps(self) -> int:
        return self.reps
    
    def get_workout_id(self) -> int:
        return self.id
    
    def set_id(self, id):
        self.id = id
        
    def set_name(self, name) -> None:
        self.name = name
        
    def set_sets(self, sets) -> None:
        self.sets = sets
        
    def set_reps(self, reps) -> None:
        self.reps = reps
    