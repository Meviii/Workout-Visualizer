# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_view - BACKUP.ui'
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
        home_view.setStyleSheet(u"border-color: rgb(255, 0, 127);\n"
"color: rgb(38, 255, 34);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(66, 52, 255);")
        self.home_title_label = QLabel(home_view)
        self.home_title_label.setObjectName(u"home_title_label")
        self.home_title_label.setGeometry(QRect(290, 40, 251, 61))
        self.home_create_button = QPushButton(home_view)
        self.home_create_button.setObjectName(u"home_create_button")
        self.home_create_button.setGeometry(QRect(670, 540, 91, 41))
        self.home_create_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.home_open_button = QPushButton(home_view)
        self.home_open_button.setObjectName(u"home_open_button")
        self.home_open_button.setGeometry(QRect(10, 10, 81, 31))
        self.home_open_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.home_clear_button = QPushButton(home_view)
        self.home_clear_button.setObjectName(u"home_clear_button")
        self.home_clear_button.setGeometry(QRect(570, 540, 91, 41))
        self.home_clear_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
        self.home_save_button = QPushButton(home_view)
        self.home_save_button.setObjectName(u"home_save_button")
        self.home_save_button.setGeometry(QRect(100, 10, 81, 31))
        self.home_save_button.setStyleSheet(u"font: 75 8pt \"MS Shell Dlg 2\";")
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
        self.scrollArea.setGeometry(QRect(40, 100, 721, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 719, 429))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        QWidget.setTabOrder(self.home_add_workout_button, self.home_create_button)
        QWidget.setTabOrder(self.home_create_button, self.home_clear_button)
        QWidget.setTabOrder(self.home_clear_button, self.home_save_button)
        QWidget.setTabOrder(self.home_save_button, self.home_open_button)

        self.retranslateUi(home_view)

        QMetaObject.connectSlotsByName(home_view)
    # setupUi

    def retranslateUi(self, home_view):
        home_view.setWindowTitle(QCoreApplication.translate("home_view", u"Workout Visualizer", None))
        self.home_title_label.setText(QCoreApplication.translate("home_view", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Workout Visualizer</span></p></body></html>", None))
        self.home_create_button.setText(QCoreApplication.translate("home_view", u"Create", None))
        self.home_open_button.setText(QCoreApplication.translate("home_view", u"Open ", None))
        self.home_clear_button.setText(QCoreApplication.translate("home_view", u"Clear All", None))
        self.home_save_button.setText(QCoreApplication.translate("home_view", u"Save", None))
        self.home_add_workout_button.setText(QCoreApplication.translate("home_view", u"Add Workout", None))
        self.home_status_label.setText("")
    # retranslateUi
