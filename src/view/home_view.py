from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
import src.controller.home_controller as hc
import src.view.view_loader as view_loader

class Ui_HomeWindow(QDialog):
    def __init__(self, widget):
        super(Ui_HomeWindow, self).__init__()
        loadUi("src/designer_files/home_view.ui", self)
        self.widget = widget
        widget.setFixedHeight(600)
        widget.setFixedWidth(800)
        
        self.get_and_print_workouts()
        
        if self.can_add_exercise_button():
            cur_button = QPushButton("Add Exercise", self)
            cur_button.setObjectName("home_add_exercise_button")
            cur_button.setGeometry(40, 540, 140, 40)
            cur_button.clicked.connect(self.add_exercise_clicked)

        self._buttons()
        
    def _buttons(self):
        self.home_add_workout_button.clicked.connect(self.add_workout_clicked)
        self.home_clear_button.clicked.connect(self.clear_all_clicked)
        self.home_create_button.clicked.connect(self.create_clicked)
        
    def add_exercise_clicked(self):
        view_loader.load_add_exercise_view(self)
    
    def create_clicked(self):
        if not (hc.create_to_excel()):
            self.home_status_label.setText("Failed to create")
        else:
            self.home_status_label.setText("Created to Excel")
    
    def clear_all_clicked(self):
        hc.clear_all()
        view_loader.load_home_view(self)
    
    def add_workout_clicked(self):
        view_loader.load_add_workout_view(self)
    
    def can_add_exercise_button(self) -> bool:
        all_workouts = hc.get_workouts()
        
        if all_workouts != []:
            return True
        return False
    
    def get_and_print_workouts(self):
        all_workouts = hc.get_workouts()
        all_exercises = hc.get_exercises()
        
        if all_workouts == []:
            return
        
        x = 1
        for workout in all_workouts:
            string_builder = str("")
            
            cur_label = QLabel(parent=self)
            cur_label.setStyleSheet("border: 1px solid black;")
            cur_label.setMinimumSize(120,40)
            cur_label.setMaximumSize(180,130)
            cur_label.setObjectName(("new_workout_" + str(x)))
            
            string_builder += str(f"{workout.name} on {workout.day}\n")
            string_builder += str("\n")
            
            for exercise in all_exercises:
                if exercise.workout_id == hc.get_workout_id_by_name(workout.name, workout.day):
                    string_builder += (f"{exercise.name}, {exercise.sets} sets, {exercise.reps} reps\n")
            
            cur_label.setText(string_builder)

            self.home_grid_layout.addWidget(cur_label)
            x += 1
            