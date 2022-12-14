import string

class workout:
    
    def __init__(self, day, name, id=None, exercises=list([])):
        self.id = id
        self.day = day 
        self.name = name
        self.exercises = exercises
    
    def get_id(self) -> int:
        return self.id
    
    def get_name(self) -> string:
        return self.name
    
    def get_day(self) -> string:
        return self.day
    
    def get_exercises(self) -> list:
        return self.exercises
    
    def set_id(self, id):
        self.id = id
    
    def set_day(self, day):
        self.day = day
    
    def set_name(self, name) -> None:
        self.name = name
    
    def set_exercises(self, exercises) -> None:
        self.exercises = exercises
        
    def __str__(self) -> str:
        return f"ID: {self.id}, \nName: {self.name},\nDay: {self.day}"