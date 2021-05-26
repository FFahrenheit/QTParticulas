from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

# Aplicación de Qt
app = QApplication()
# Se crea la vista
window = MainWindow()
# Se hace visible
window.show()
# Qt loop
sys.exit(app.exec_())