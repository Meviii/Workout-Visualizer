import src.view.home_view as hv
import src.view.add_workout_view as awv
import src.view.add_exercise_view as aev

def load_home_view(self):
    home_view = hv.Ui_HomeWindow(self.widget)
    self.widget.addWidget(home_view)
    self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

def load_add_workout_view(self):
    add_workout_window = awv.Ui_AddWorkoutWindow(self.widget)
    self.widget.addWidget(add_workout_window)
    self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

def load_add_exercise_view(self):
    add_exercise_window = aev.Ui_AddExerciseWindow(self.widget)
    self.widget.addWidget(add_exercise_window)
    self.widget.setCurrentIndex(self.widget.currentIndex() + 1)