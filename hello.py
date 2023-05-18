import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

# Create instance of Qapp (passing an empty list as app won't be handling command line arguements)
app = QApplication([])

# instance, title, size/screen position, message and said message reference
window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

# show the gui, and run the gui, respectively
window.show()
sys.exit(app.exec())