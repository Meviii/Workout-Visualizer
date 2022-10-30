# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_workout_view - Copy.ui'
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
        self.add_status_label = QLabel(add_workout_view)
        self.add_status_label.setObjectName(u"add_status_label")
        self.add_status_label.setGeometry(QRect(100, 190, 91, 21))
        self.title_label = QLabel(add_workout_view)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(90, 50, 171, 51))
        self.workout_name_text = QLineEdit(add_workout_view)
        self.workout_name_text.setObjectName(u"workout_name_text")
        self.workout_name_text.setGeometry(QRect(100, 120, 141, 20))
        self.statusLabel = QLabel(add_workout_view)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(190, 320, 71, 16))
        self.configDateLabel_2 = QLabel(add_workout_view)
        self.configDateLabel_2.setObjectName(u"configDateLabel_2")
        self.configDateLabel_2.setGeometry(QRect(219, 330, 91, 21))
        self.add_workout_button = QPushButton(add_workout_view)
        self.add_workout_button.setObjectName(u"add_workout_button")
        self.add_workout_button.setGeometry(QRect(180, 190, 61, 23))
        self.workout_day_text = QLineEdit(add_workout_view)
        self.workout_day_text.setObjectName(u"workout_day_text")
        self.workout_day_text.setGeometry(QRect(100, 160, 141, 20))

        self.retranslateUi(add_workout_view)

        QMetaObject.connectSlotsByName(add_workout_view)
    # setupUi

    def retranslateUi(self, add_workout_view):
        add_workout_view.setWindowTitle(QCoreApplication.translate("add_workout_view", u"Workouts - Workout Tracker", None))
        self.back_to_main_view.setText(QCoreApplication.translate("add_workout_view", u"Back", None))
        self.add_status_label.setText("")
        self.title_label.setText(QCoreApplication.translate("add_workout_view", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Add Workout</span></p></body></html>", None))
        self.workout_name_text.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Workout Name", None))
        self.statusLabel.setText("")
        self.configDateLabel_2.setText("")
        self.add_workout_button.setText(QCoreApplication.translate("add_workout_view", u"Add", None))
        self.workout_day_text.setPlaceholderText(QCoreApplication.translate("add_workout_view", u"Workout Day", None))
    # retranslateUi

