from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from PySide2.QtCore import Qt, SLOT, Slot
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

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

    @Slot()
    def mostrar_tabla(self):
        headers = ['Id','Origen','Destino','Velocidad','Color','Distancia']
        self.ui.tabla.setColumnCount(len(headers))
        self.ui.tabla.setHorizontalHeaderLabels(headers)

        self.ui.tabla.setRowCount(len(self.cern))

        for index, part in enumerate(self.cern):

            id_widget = QTableWidgetItem(str(part.id))
            origen_widget = QTableWidgetItem(f"({part.origen_x},{part.origen_y})")
            destino_widget = QTableWidgetItem(f"({part.destino_x},{part.destino_y})")
            velocidad_widget = QTableWidgetItem(str(part.velocidad))
            color_widget = QTableWidgetItem(f"rgb({part.red},{part.green},{part.blue})")
            distancia_widget = QTableWidgetItem(f"{part.distancia:.4f}")

            self.ui.tabla.setItem(index,0,id_widget)
            self.ui.tabla.setItem(index,1,origen_widget)
            self.ui.tabla.setItem(index,2,destino_widget)
            self.ui.tabla.setItem(index,3,velocidad_widget)
            self.ui.tabla.setItem(index,4,color_widget)
            self.ui.tabla.setItem(index,5,distancia_widget)

    @Slot()
    def buscar_id(self):
        id = self.ui.buscar_lineEdit.text().strip()

        for part in self.cern:
            
            current_id = str(part.id)

            if current_id == id:
                self.ui.tabla.clearContents()
                self.ui.tabla.setRowCount(1)

                id_widget = QTableWidgetItem(str(part.id))
                origen_widget = QTableWidgetItem(f"({part.origen_x},{part.origen_y})")
                destino_widget = QTableWidgetItem(f"({part.destino_x},{part.destino_y})")
                velocidad_widget = QTableWidgetItem(str(part.velocidad))
                color_widget = QTableWidgetItem(f"rgb({part.red},{part.green},{part.blue})")
                distancia_widget = QTableWidgetItem(f"{part.distancia:.4f}")

                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_widget)
                self.ui.tabla.setItem(0, 2, destino_widget)
                self.ui.tabla.setItem(0, 3, velocidad_widget)
                self.ui.tabla.setItem(0, 4, color_widget)
                self.ui.tabla.setItem(0, 5, distancia_widget)

                return
        
        QMessageBox.warning(
            self,
            'Atención',
            f"La particula con id {id} no pudo ser encontrada"
        )

        self.ui.buscar_lineEdit.clear()

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
        self.mostrar_tabla()

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