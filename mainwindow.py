from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from lib.cern import CERN
from lib.particula import Particula

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.cern = CERN()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_inicio_button.clicked.connect(self.agregar_inicio)
        self.ui.agregar_final_button.clicked.connect(self.agregar_fin)
        self.ui.mostrar_button.clicked.connect(self.mostrar)

        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)

    @Slot()
    def abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]

        if self.cern.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
            self.mostrar()
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

    @Slot()
    def guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(
            self,
            'Abrir archivo',
            '.',
            'JSON (*.json)'
        )[0]

        print("Archivo: " + ubicacion)

        if self.cern.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se guardó en el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al guardar el archivo " + ubicacion
            )

    @Slot()
    def agregar_inicio(self):
        self.cern.agregar_inicio(self.get_particula())
        self.mostrar()

    @Slot()
    def agregar_fin(self):
        self.cern.agregar_final(self.get_particula())
        self.mostrar()
    
    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        self.ui.salida.insertPlainText(str(self.cern))

    def get_particula(self):
        id = int(self.ui.id.text())
        orig_x = int(self.ui.origin_x.text())
        orig_y = int(self.ui.origin_y.text())
        dest_x = int(self.ui.destination_x.text())
        dest_y = int(self.ui.destination_y.text())
        velocidad = int(self.ui.velocity.text())
        color_r = int(self.ui.color_r.text())
        color_g = int(self.ui.color_g.text())
        color_b = int(self.ui.color_b.text())
        return Particula(id,orig_x,orig_y,dest_x,dest_y,velocidad,color_r,color_g,color_b)