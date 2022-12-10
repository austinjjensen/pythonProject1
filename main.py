from gui import *
from controller import *
def main():
    # import sys
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()

if __name__ == "__main__":
    main()