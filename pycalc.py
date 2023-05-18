import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

WINDOW_SIZE = 235

# create the class and the parameters surrounding the calculator GUI
class PyCalcWindow(QMainWindow):
    """PyCalc's main window (GUI or view)."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyCalc")
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)

# create the instance to run, event loop
def main():
    """PyCalc's main function."""
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    sys.exit(pycalcApp.exec())

# execute 
if __name__ == "__main__":
    main()