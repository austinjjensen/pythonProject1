from PyQt5.QtWidgets import *
from gui import *
from _csv import writer

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pushCalculate.clicked.connect(lambda: self.calculate())
        self.pushClear.clicked.connect(lambda: self.clear())

    def calculate(self):

        name = self.nameInput.text()
        numClasses = self.numClassInput.text()
        courseName = self.classInput_1.text()
        letterGrade = self.gradeInput_1.text()
        numCredits = self.creditInput_1.text()



        with open('studentRecords.csv', 'a', newline='') as file:
            Writer = writer(file)
            Writer.writerow([name, numClasses, courseName, letterGrade, numCredits])

        # self.labelGpa.setText(f'Your GPA is: {name}')

        # self.nameInput.setText('')
        # self.numClassInput.setText('')
        # self.classInput_1.setText('')
        # self.classInput_2.setText('')
        # self.classInput_3.setText('')
        # self.classInput_4.setText('')
        # self.classInput_5.setText('')
        # self.classInput_6.setText('')
        # self.gradeInput_1.setText('')
        # self.gradeInput_2.setText('')
        # self.gradeInput_3.setText('')
        # self.gradeInput_4.setText('')
        # self.gradeInput_5.setText('')
        # self.gradeInput_6.setText('')
        # self.creditInput_1.setText('')
        # self.creditInput_2.setText('')
        # self.creditInput_3.setText('')
        # self.creditInput_4.setText('')
        # self.creditInput_5.setText('')
        # self.creditInput_6.setText('')


    def clear(self):
        self.nameInput.setText('')
        self.numClassInput.setText('')
        self.classInput_1.setText('')
        self.classInput_2.setText('')
        self.classInput_3.setText('')
        self.classInput_4.setText('')
        self.classInput_5.setText('')
        self.classInput_6.setText('')
        self.gradeInput_1.setText('')
        self.gradeInput_2.setText('')
        self.gradeInput_3.setText('')
        self.gradeInput_4.setText('')
        self.gradeInput_5.setText('')
        self.gradeInput_6.setText('')
        self.creditInput_1.setText('')
        self.creditInput_2.setText('')
        self.creditInput_3.setText('')
        self.creditInput_4.setText('')
        self.creditInput_5.setText('')
        self.creditInput_6.setText('')