from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QLabel
from PyQt5.uic import loadUi
import src.view.view_loader as view_loader
import src.controller.add_exercise_controller as aec

class Ui_AddExerciseWindow(QDialog):
    def __init__(self, widget):
        super(Ui_AddExerciseWindow, self).__init__()
        loadUi("src/designer_files/add_exercise_view.ui", self)
        
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
        
        if exercise_name == "" or exercise_reps == "" or exercise_sets == "":
            self.exercise_add_status.setText("Empty fields")
        else:
            aec.add_new_exercise(exercise_name, exercise_sets, exercise_reps, exercise_workouts)
            self.exercise_add_status.setText("Added")
        
    def back_button_clicked(self):
        view_loader.load_home_view(self)