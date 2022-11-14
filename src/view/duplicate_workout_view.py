from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QLabel
from PyQt5.uic import loadUi
import src.utility.path as util_path
import src.view.view_loader as view_loader
import src.controller.duplicate_workout_controller as dwc

FILENAME = 'duplicate_workout_view.ui'
PATH = util_path.get_correct_path_of_designer_files(FILENAME)

class Ui_DuplicateWorkoutWindow(QDialog):
    def __init__(self, widget, workout_to_add, exercises_of_workout):
        super(Ui_DuplicateWorkoutWindow, self).__init__()
        loadUi(PATH, self)
        print(workout_to_add)
        print(exercises_of_workout)
        self.widget = widget
        self.workout_to_add = workout_to_add
        self.exercises_of_workout = exercises_of_workout
        
        self._load_days_combo_box()
        
        self.workout_label.setText(f"Duplicating Workout: {workout_to_add.name} on {workout_to_add.day}")
        
        widget.setFixedHeight(326)
        widget.setFixedWidth(326)
        
        self._buttons()
        
    def _load_days_combo_box(self):
        DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(len(DAYS)):
            self.workout_day_combo_box.addItem(DAYS[i])
    
    def _buttons(self):
        self.back_to_main_view.clicked.connect(self.back_button_clicked)
        self.add_workout_button.clicked.connect(self.add_workout_button_clicked)
    
    def add_workout_button_clicked(self) -> bool:
        workout_name = self.workout_name_field.text()
        workout_day = self.workout_day_combo_box.currentText()

        # if fields are empty
        if workout_name == "" or workout_day == "":
            self.workout_add_status_label.setText("Empty fields")
            return False
        
        # if workout_name is not unique
        if not dwc.can_add_new_workout(workout_name, workout_day):
            self.workout_add_status_label.setText("Already Added")
            return False
        
        # add new workout if can
        if not (dwc.add_new_workout(workout_name, workout_day)):
            self.workout_add_status_label.setText("Failed to add")
            return False
        
        new_workout_id = dwc.get_new_workout_id(workout_name, workout_day)
        
        # add exercises to workout
        if self.exercises_of_workout != []:
            if not (dwc.add_exercises_for_workout(new_workout_id, self.exercises_of_workout)):
                self.workout_add_status_label.setText("Failed to add")
                return False
        
        self.workout_add_status_label.setText("Added")
        
    def back_button_clicked(self):
        view_loader.load_home_view(self)