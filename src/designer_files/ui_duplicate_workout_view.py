# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'duplicate_workout_view.ui'
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
        self.title_label.setGeometry(QRect(58, 46, 231, 51))
        self.add_workout_button = QPushButton(add_workout_view)
        self.add_workout_button.setObjectName(u"add_workout_button")
        self.add_workout_button.setGeometry(QRect(180, 180, 61, 23))
        self.workout_name_field = QLineEdit(add_workout_view)
        self.workout_name_field.setObjectName(u"workout_name_field")
        self.workout_name_field.setGeometry(QRect(100, 120, 141, 20))
        self.workout_label = QLabel(add_workout_view)
        self.workout_label.setObjectName(u"workout_label")
        self.workout_label.setGeometry(QRect(60, 87, 231, 21))
        self.workout_label.setAlignment(Qt.AlignCenter)
        self.workout_add_status_label = QLabel(add_workout_view)
        self.workout_add_status_label.setObjectName(u"workout_add_status_label")
        self.workout_add_status_label.setGeometry(QRect(102, 180, 71, 21))
        self.workout_day_combo_box = QComboBox(add_workout_view)
        self.workout_day_combo_box.setObjectName(u"workout_day_combo_box")
        self.workout_day_combo_box.setGeometry(QRect(100, 150, 141, 21))
        QWidget.setTabOrder(self.workout_name_field, self.add_workout_button)
        QWidget.setTabOrder(self.add_workout_button, self.back_to_main_view)

        self.retranslateUi(add_workout_view)

        QMetaObject.connectSlotsByName(add_workout_view)
    # setupUi

    def retranslateUi(self, add_workout_view):
        add_workout_view.setWindowTitle(QCoreApplication.translate("add_workout_view", u"Exercise - Workout Tracker", None))
        self.back_to_main_view.setText(QCoreApplication.translate("add_workout_view", u"Back", None))
        self.title_label.setText(QCoreApplication.translate("add_workout_view", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Duplicate Workout</span></p></body></html>", None))
        self.add_workout_button.setText(QCoreApplication.translate("add_workout_view", u"Add", None))
        self.workout_name_field.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Workout name", None))
        self.workout_label.setText("")
        self.workout_add_status_label.setText("")
        self.workout_day_combo_box.setCurrentText("")
        self.workout_day_combo_box.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Choose a workout", None))
    # retranslateUi

