# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_exercise_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_workout_view(object):
    def setupUi(self, add_workout_view):
        if not add_workout_view.objectName():
            add_workout_view.setObjectName(u"add_workout_view")
        add_workout_view.resize(326, 326)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_workout_view.sizePolicy().hasHeightForWidth())
        add_workout_view.setSizePolicy(sizePolicy)
        self.back_to_main_view = QPushButton(add_workout_view)
        self.back_to_main_view.setObjectName(u"back_to_main_view")
        self.back_to_main_view.setGeometry(QRect(250, 10, 61, 21))
        self.title_label = QLabel(add_workout_view)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(90, 46, 171, 51))
        self.exercise_name_text = QLineEdit(add_workout_view)
        self.exercise_name_text.setObjectName(u"exercise_name_text")
        self.exercise_name_text.setGeometry(QRect(100, 150, 141, 20))
        self.add_exercise_button = QPushButton(add_workout_view)
        self.add_exercise_button.setObjectName(u"add_exercise_button")
        self.add_exercise_button.setGeometry(QRect(180, 260, 61, 23))
        self.exercise_sets_text = QLineEdit(add_workout_view)
        self.exercise_sets_text.setObjectName(u"exercise_sets_text")
        self.exercise_sets_text.setGeometry(QRect(100, 190, 141, 20))
        self.exercise_reps_text = QLineEdit(add_workout_view)
        self.exercise_reps_text.setObjectName(u"exercise_reps_text")
        self.exercise_reps_text.setGeometry(QRect(100, 230, 141, 20))
        self.exercise_workout_label = QLabel(add_workout_view)
        self.exercise_workout_label.setObjectName(u"exercise_workout_label")
        self.exercise_workout_label.setGeometry(QRect(60, 87, 231, 21))
        self.exercise_add_status = QLabel(add_workout_view)
        self.exercise_add_status.setObjectName(u"exercise_add_status")
        self.exercise_add_status.setGeometry(QRect(102, 260, 71, 21))
        self.workout_combo_box = QComboBox(add_workout_view)
        self.workout_combo_box.setObjectName(u"workout_combo_box")
        self.workout_combo_box.setGeometry(QRect(100, 120, 141, 21))
        QWidget.setTabOrder(self.exercise_name_text, self.exercise_sets_text)
        QWidget.setTabOrder(self.exercise_sets_text, self.exercise_reps_text)
        QWidget.setTabOrder(self.exercise_reps_text, self.add_exercise_button)
        QWidget.setTabOrder(self.add_exercise_button, self.back_to_main_view)

        self.retranslateUi(add_workout_view)

        QMetaObject.connectSlotsByName(add_workout_view)
    # setupUi

    def retranslateUi(self, add_workout_view):
        add_workout_view.setWindowTitle(QCoreApplication.translate("add_workout_view", u"Exercise - Workout Tracker", None))
        self.back_to_main_view.setText(QCoreApplication.translate("add_workout_view", u"Back", None))
        self.title_label.setText(QCoreApplication.translate("add_workout_view", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Add Exercise</span></p></body></html>", None))
        self.exercise_name_text.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Exercise Name", None))
        self.add_exercise_button.setText(QCoreApplication.translate("add_workout_view", u"Add", None))
        self.exercise_sets_text.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Exercise Sets", None))
        self.exercise_reps_text.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Exercise Reps (eg. 4, 4-6)", None))
        self.exercise_workout_label.setText(QCoreApplication.translate("add_workout_view", u"Adding for Workout: Back & Biceps on Tuesday", None))
        self.exercise_add_status.setText("")
        self.workout_combo_box.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Choose a workout", None))
    # retranslateUi

