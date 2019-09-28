# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow  # 这个是这样的
import a_layout, formWindow, setbuddy

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    # ui = a_layout.Ui_MainWindow()
    # ui = formWindow.Ui_MainWindow()
    ui = setbuddy.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())




