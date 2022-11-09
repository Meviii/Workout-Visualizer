from PyQt5 import QtWidgets
import sys
import src.view.home_view as home_view

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = home_view.Ui_HomeWindow(widget)
    widget.addWidget(main)
    widget.show()
    sys.exit(app.exec_())