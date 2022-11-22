# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_view - WORKING ON.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_home_view(object):
    def setupUi(self, home_view):
        if not home_view.objectName():
            home_view.setObjectName(u"home_view")
        home_view.resize(800, 600)
        home_view.setAutoFillBackground(False)
        home_view.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color:transparent;\n"
"	background:none;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"\n"
"#home_view{\n"
"	background-color:#1f232a;\n"
"}\n"
"\n"
"#verticalLayout{\n"
"	background-color:#16191d;\n"
"}\n"
"\n"
"#verticalLayout QPushButton{\n"
"	text-align:left;\n"
"	padding:5px 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"\n"
"")
        self.home_title_label = QLabel(home_view)
        self.home_title_label.setObjectName(u"home_title_label")
        self.home_title_label.setGeometry(QRect(290, 40, 251, 61))
        self.home_create_button = QPushButton(home_view)
        self.home_create_button.setObjectName(u"home_create_button")
        self.home_create_button.setGeometry(QRect(670, 540, 91, 41))
        self.home_create_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.home_clear_button = QPushButton(home_view)
        self.home_clear_button.setObjectName(u"home_clear_button")
        self.home_clear_button.setGeometry(QRect(570, 540, 91, 41))
        self.home_clear_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.home_add_workout_button = QPushButton(home_view)
        self.home_add_workout_button.setObjectName(u"home_add_workout_button")
        self.home_add_workout_button.setGeometry(QRect(620, 53, 141, 41))
        self.home_add_workout_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.home_status_label = QLabel(home_view)
        self.home_status_label.setObjectName(u"home_status_label")
        self.home_status_label.setGeometry(QRect(481, 550, 81, 21))
        self.home_status_label.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(home_view)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(130, 100, 630, 430))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(630, 430))
        self.scrollArea.setMaximumSize(QSize(630, 430))
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 630, 430))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget = QWidget(home_view)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 100, 111, 431))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_add_workout_button_3 = QPushButton(self.verticalLayoutWidget)
        self.home_add_workout_button_3.setObjectName(u"home_add_workout_button_3")
        self.home_add_workout_button_3.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.home_add_workout_button_3)

        self.home_add_workout_button_2 = QPushButton(self.verticalLayoutWidget)
        self.home_add_workout_button_2.setObjectName(u"home_add_workout_button_2")
        self.home_add_workout_button_2.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.home_add_workout_button_2)

        self.home_add_workout_button_4 = QPushButton(self.verticalLayoutWidget)
        self.home_add_workout_button_4.setObjectName(u"home_add_workout_button_4")
        self.home_add_workout_button_4.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.home_add_workout_button_4)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.home_save_button = QPushButton(self.verticalLayoutWidget)
        self.home_save_button.setObjectName(u"home_save_button")
        self.home_save_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.home_save_button)

        self.home_open_button = QPushButton(self.verticalLayoutWidget)
        self.home_open_button.setObjectName(u"home_open_button")
        self.home_open_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.home_open_button)

        QWidget.setTabOrder(self.home_add_workout_button, self.home_create_button)
        QWidget.setTabOrder(self.home_create_button, self.home_clear_button)
        QWidget.setTabOrder(self.home_clear_button, self.home_open_button)

        self.retranslateUi(home_view)

        QMetaObject.connectSlotsByName(home_view)
    # setupUi

    def retranslateUi(self, home_view):
        home_view.setWindowTitle(QCoreApplication.translate("home_view", u"Workout Visualizer", None))
        self.home_title_label.setText(QCoreApplication.translate("home_view", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Workout Visualizer</span></p></body></html>", None))
        self.home_create_button.setText(QCoreApplication.translate("home_view", u"Create", None))
        self.home_clear_button.setText(QCoreApplication.translate("home_view", u"Clear All", None))
        self.home_add_workout_button.setText(QCoreApplication.translate("home_view", u"Add Workout", None))
        self.home_status_label.setText("")
        self.home_add_workout_button_3.setText(QCoreApplication.translate("home_view", u"Personal Details", None))
        self.home_add_workout_button_2.setText(QCoreApplication.translate("home_view", u"Workouts", None))
        self.home_add_workout_button_4.setText(QCoreApplication.translate("home_view", u"Goals", None))
        self.home_save_button.setText(QCoreApplication.translate("home_view", u"Save", None))
        self.home_open_button.setText(QCoreApplication.translate("home_view", u"Open ", None))
    # retranslateUi

