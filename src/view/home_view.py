from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import src.controller.home_controller as hc
import src.view.view_loader as view_loader
import src.utility.path as util_path

FILENAME = 'home_view.ui'
PATH = util_path.get_correct_path_of_designer_files(FILENAME)

class Ui_HomeWindow(QDialog):
    def __init__(self, widget):
        super(Ui_HomeWindow, self).__init__()
        loadUi(PATH, self)
        self.widget = widget
        widget.setFixedHeight(600)
        widget.setFixedWidth(800)

        if hc.get_workouts() != []:
            self.get_and_print_workouts()

        if self.can_add_exercise_button():
            exercise_button = QPushButton("Add Exercise", self)
            exercise_button.setObjectName("home_add_exercise_button")
            exercise_button.setGeometry(40, 540, 140, 40)
            exercise_button.clicked.connect(self.add_exercise_clicked)

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
        COLUMN_MAX = 3
        all_workouts = hc.get_workouts()
        all_exercises = hc.get_exercises()
        
        # Add each Workout
        row = 0
        col = 0
        for w_idx in range(len(all_workouts)):
            current_workout = all_workouts[w_idx]
            current_exercises = [e for e in all_exercises if e.workout_id == current_workout.id]
            
            if col == COLUMN_MAX:
                row += 1
                col = 0
                self._create_per_workout(row, col, all_workouts[w_idx], current_exercises, w_idx)
                col += 1
            else:
                self._create_per_workout(row, col, all_workouts[w_idx], current_exercises, w_idx)
                col += 1
        
    def _duplicate_workout(self, current_workout, current_exercises):
        view_loader.load_duplicate_workout_view(self, current_workout, current_exercises)
    
    def _create_per_workout(self, row, col, curr_workout, curr_exercises, current_idx):
        
        # Frame Per Workout
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(f"frame_{current_idx}")
        self.frame.setMinimumSize(QSize(180, 180))
        self.frame.setMaximumSize(QSize(180, 180))
        # self.frame.setStyleSheet(u"background-color: rgb(150, 255, 64);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        # self.frame.setFrameShadow(QFrame.Raised)
        
        # Label Per Workout
        self.label = QLabel(self.frame)
        self.label.setObjectName(f"label_{current_idx}")
        self.label.setGeometry(QRect(50, 10, 130, 30))
        self.label.setText(f"{curr_workout.name} on {curr_workout.day}\n")
        
        # Exercise List Per Workout
        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(f"listWidget_{current_idx}")
        self.listWidget.setGeometry(QRect(10, 30, 160, 120))
        
        for exercise in curr_exercises:
            self.listWidget.addItem((f"{exercise.name}, {exercise.sets} sets, {exercise.reps} reps\n"))
        
        duplicate_button = QPushButton("Duplicate", self.frame)
        duplicate_button.setObjectName(f"workout_dup_button_{current_idx}")
        duplicate_button.setGeometry(QRect(10, 155, 50, 20))
        duplicate_button.clicked.connect(lambda: self._duplicate_workout(curr_workout, curr_exercises))
        
        delete_button = QPushButton("Delete", self.frame)
        delete_button.setObjectName(f"workout_dup_button_{current_idx}")
        delete_button.setGeometry(QRect(70, 155, 50, 20))
        delete_button.clicked.connect(lambda: self._delete_workout(curr_workout))
        
        # Add frame to Grid Layout
        self.gridLayout.addWidget(self.frame, row, col, 1, 1, Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

    def _delete_workout(self, workout_to_delete):
        if not hc.delete_workout(workout_to_delete):
            self.home_status_label.setText("Couldn't delete")
            return False
        
        view_loader.load_home_view(self)