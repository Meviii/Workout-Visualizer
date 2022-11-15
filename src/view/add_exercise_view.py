from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QLabel
from PyQt5.uic import loadUi
import src.view.view_loader as view_loader
import src.controller.add_exercise_controller as aec
import src.utility.path as util_path

FILENAME = 'add_exercise_view.ui'
PATH = util_path.get_correct_path_of_designer_files(FILENAME)

class Ui_AddExerciseWindow(QDialog):
    def __init__(self, widget):
        super(Ui_AddExerciseWindow, self).__init__()
        loadUi(PATH, self)
        
        self.widget = widget

        widget.setFixedHeight(326)
        widget.setFixedWidth(326)

        self.get_and_list_workouts()
        
        self._buttons()
        
    def _buttons(self):
        self.back_to_main_view.clicked.connect(self.back_button_clicked)
        self.add_exercise_button.clicked.connect(self.add_exercise_button_clicked)
    
    def get_and_list_workouts(self):
        all_workouts = aec.get_workouts()
        
        if all_workouts == []:
            return
        
        for workout in all_workouts:
            self.workout_combo_box.addItem(f"{workout.name} on {workout.day}")
    
    def add_exercise_button_clicked(self):
        exercise_name = self.exercise_name_text.text()
        exercise_reps = self.exercise_reps_text.text()
        exercise_sets = self.exercise_sets_text.text()
        exercise_workouts = self.workout_combo_box.currentText()
        
        # if empty fields
        if exercise_name == "" or exercise_reps == "" or exercise_sets == "" or exercise_workouts == "":
                self.exercise_add_status.setText("Empty fields")
                return
        
        # if incorrect data types
        worker = exercise_reps
        if "-" in exercise_reps:
            worker = str(exercise_reps).replace("-", "")
        
        if str(worker).isdigit() == False or str(exercise_sets).isdigit() == False:
            self.exercise_add_status.setText("Incorrect fields")
            return
        
        # if failed to add exercise
        if not aec.add_new_exercise(exercise_name, exercise_sets, exercise_reps, exercise_workouts):
            self.exercise_add_status.setText("Failed to add")
            return
            
        self.exercise_add_status.setText("Added")
        
    def back_button_clicked(self):
        view_loader.load_home_view(self)