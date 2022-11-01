from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMainWindow, QDialog, QLabel
from PyQt5.uic import loadUi
import src.view.view_loader as view_loader
import src.controller.add_workout_controller as awc
import src.utility.path as util_path

FILENAME = 'add_workout_view.ui'
PATH = util_path.get_correct_path_of_designer_files(FILENAME)

class Ui_AddWorkoutWindow(QDialog):
    def __init__(self, widget):
        super(Ui_AddWorkoutWindow, self).__init__()
        loadUi(PATH, self)
        
        self.widget = widget
        
        self._load_days_combo_box()
        
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
    
    def add_workout_button_clicked(self):
        workout_name = self.workout_name_text.text()
        workout_day = self.workout_day_combo_box.currentText()

        # if fields are empty
        if workout_name == "" or workout_day == "":
            self.add_status_label.setText("Empty fields")
            return
        
        # if not correcty datatype
        if str(workout_name).isdigit() == False:
            self.add_status_label.setText("Incorrect fields")
            return
        
        # if workout_name is not unique
        if not awc.can_add_new_workout(workout_name):
            self.add_status_label.setText("Duplicate")
        
        # if adding new workout failed
        if not (awc.add_new_workout(workout_name, workout_day)):
            self.add_status_label.setText("Failed to add")
            return
        
        self.add_status_label.setText("Added")
        
    def back_button_clicked(self):
        view_loader.load_home_view(self)