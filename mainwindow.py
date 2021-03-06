from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtCore import SignalInstance, Slot
from PySide2.QtGui import QPen, QColor
from ui_mainwindow import Ui_MainWindow
from lib.cern import CERN
from lib.particula import Particula
from pprint import pformat

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.cern = CERN()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.agregar_inicio_button.clicked.connect(self.agregar_inicio)
        self.ui.agregar_final_button.clicked.connect(self.agregar_fin)
        self.ui.mostrar_button.clicked.connect(self.mostrar_plano)
        self.ui.grafo_button.clicked.connect(self.mostrar_grafo)

        self.ui.salida.setReadOnly(True)
        self.grafo = False

        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)
        self.ui.action_grafo.triggered.connect(self.mostrar_grafo)
        self.ui.action_lista.triggered.connect(self.mostrar_plano)
        
        self.ui.action_recorridos.triggered.connect(self.mostrar_recorridos)
        self.ui.action_prim.triggered.connect(self.dibujar_prim)
        self.ui.action_kruskal.triggered.connect(self.dibujar_kruskal)
        self.ui.action_dijkstra.triggered.connect(self.dibujar_dijkstra)

        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.borrar.clicked.connect(self.limpiar)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        self.ui.plainTextSort.currentIndexChanged.connect(self.sort_plain)
        self.ui.tableSort.currentIndexChanged.connect(self.sort_plain)

    @Slot()
    def dibujar_dijkstra(self):
        self.mostrar()
        if not self.grafo or len(self.cern) == 0:
            QMessageBox.critical(
                self,
                "No se pudo leer",
                "Convierta a grafo no vac??o antes"
            )
        else:
            origen_x = int(self.ui.origin_x.text())
            origen_y = int(self.ui.origin_y.text()) 
            origen = (origen_x, origen_y)

            destino_x = int(self.ui.destination_x.text())
            destino_y = int(self.ui.destination_y.text())
            destino = (destino_x, destino_y)

            grafo = self.cern.to_dict()

            if origen not in grafo or destino not in grafo:
                QMessageBox.information(
                    self,
                    "Origen o destino inv??lidos",
                    "Escriba un origen y destino v??lidos en los campos"
                )
                return
            
            distancias, camino = self.cern.dijkstra(origen)

            print('')
            formated = pformat(distancias, width=40, indent=1)
            print(formated)
            print('')
            formated = pformat(camino, width=40, indent=1)
            print(formated)
            
            if camino[origen] not in grafo or camino[destino] not in grafo:
                QMessageBox.critical(
                self,
                "Sin camino",
                "No se encontr?? el camino"
                )
                return

            self.ui.tabWidget.setCurrentIndex(2)
            self.scene.clear()
            pen = QPen()
            pen.setColor(QColor(105, 207, 193))
            dimension = 5
            pen.setWidth(dimension)

            siguiente = destino

            while siguiente != origen:
                actual = camino[siguiente]
                
                self.scene.addLine(actual[0]+3, actual[1]+3, siguiente[0], siguiente[1], pen) 
                self.scene.addEllipse(actual[0], actual[1], dimension, dimension, pen)
                self.scene.addEllipse(siguiente[0], siguiente[1], dimension, dimension, pen)
                
                siguiente = camino[siguiente]
                

    @Slot()
    def dibujar_kruskal(self):
        self.mostrar()
        if not self.grafo or len(self.cern) == 0:
            QMessageBox.critical(
                self,
                "No se pudo leer",
                "Convierta a grafo no vac??o antes"
            )
        else:
            arbol = self.cern.kruskal()
            print("Arbol de expansion minima: ")
            print(arbol)

            self.ui.tabWidget.setCurrentIndex(2)
            
            pen = QPen()
            pen.setDashPattern([1,3])
            color  = QColor(255,255,255)
            pen.setColor(color)
            pen.setWidth(4)
            
            for arista in arbol:

                origen = arista[1]
                destino = arista[2]

                self.scene.addLine(origen[0]+3, origen[1]+3, destino[0], destino[1], pen)

    @Slot()
    def dibujar_prim(self):
        self.mostrar()
        if not self.grafo or len(self.cern) == 0:
            QMessageBox.critical(
                self,
                "No se pudo leer",
                "Convierta a grafo no vac??o antes"
            )
        else:
            origen_x = int(self.ui.origin_x.text())
            origen_y = int(self.ui.origin_y.text()) 
            origen = (origen_x, origen_y)
            
            if origen not in self.cern.to_dict():
                QMessageBox.information(
                    self,
                    "Sin origen v??lido",
                    "Se usar?? el primer elemento en el grafo como origen"
                )
                origen = next(iter(self.cern.to_dict()))

            arbol = self.cern.prim(origen)
            print(arbol)

            self.ui.tabWidget.setCurrentIndex(2)
            
            pen = QPen()
            pen.setDashPattern([1,3])
            color  = QColor(255,255,255)
            pen.setColor(color)
            pen.setWidth(4)
            
            for arista in arbol:

                origen = arista[1]
                destino = arista[2]

                self.scene.addLine(origen[0]+3, origen[1]+3, destino[0], destino[1], pen)

    @Slot()
    def mostrar_recorridos(self):
        self.mostrar()
        if not self.grafo or len(self.cern) == 0:
            QMessageBox.critical(
                self,
                "No se pudo leer",
                "Convierta a grafo no vac??o antes"
            )
        else:
            origen_x = int(self.ui.origin_x.text())
            origen_y = int(self.ui.origin_y.text()) 
            origen = (origen_x, origen_y)
            
            if origen not in self.cern.to_dict():
                QMessageBox.information(
                    self,
                    "Sin origen v??lido",
                    "Se usar?? el primer elemento en el grafo como origen"
                )
                origen = next(iter(self.cern.to_dict()))

            anchura = self.cern.recorrido_anchura(origen)
            profundidad = self.cern.recorrido_profundidad(origen)
            
            print(f"Origen = {str(origen)}")

            print("Recorrido en anchura:")
            print(anchura)
            self.ui.salida.insertPlainText('\n\nRecorrido en anchura:\n')
            self.ui.salida.insertPlainText(anchura)

            print("Recorrido en profundidad:")
            print(profundidad)
            self.ui.salida.insertPlainText('\nRecorrido en profundidad:\n')
            self.ui.salida.insertPlainText(profundidad)

            self.ui.salida.ensureCursorVisible()
    
    @Slot()
    def sort_plain(self,index):
        self.ui.plainTextSort.setCurrentIndex(index)
        self.ui.tableSort.setCurrentIndex(index)
        self.mostrar()

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def dibujar(self):
        self.scene.clear()
        if len(self.cern) > 0:
            pen = QPen()
            # maxValue = max( [p.velocidad for p in self.cern] )

            for particula in self.cern:

                color  = QColor(int(particula.red), int(particula.green), int(particula.blue))
                pen.setColor(color)

                # dimension = round(6 - 3 * particula.velocidad / (maxValue+0.1)) 
                dimension = 5
                pen.setWidth(dimension)

                self.scene.addLine(particula.origen_x+3, particula.origen_y+3, particula.destino_x, particula.destino_y, pen) 
                self.scene.addEllipse(particula.origen_x, particula.origen_y, dimension, dimension, pen)
                self.scene.addEllipse(particula.destino_x, particula.destino_y, dimension, dimension, pen)

    @Slot()
    def limpiar(self):
        self.scene.clear()

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
            'Atenci??n',
            f"La particula con id {id} no pudo ser encontrada"
        )

        self.ui.buscar_lineEdit.clear()

    @Slot()
    def abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir archivo',
            './examples',
            'JSON (*.json)'
        )[0]

        if self.cern.abrir(ubicacion):
            QMessageBox.information(
                self,
                "??xito",
                "Se abri?? el archivo " + ubicacion
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
            './examples',
            'JSON (*.json)'
        )[0]

        print("Archivo: " + ubicacion)

        if self.cern.guardar(ubicacion):
            QMessageBox.information(
                self,
                "??xito",
                "Se guard?? en el archivo " + ubicacion
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
    def mostrar_grafo(self):
        self.grafo = True
        self.mostrar()

    @Slot()
    def mostrar_plano(self):
        self.grafo = False
        self.mostrar()

    @Slot()
    def mostrar(self):
        self.ui.salida.clear()
        index = self.ui.tableSort.currentIndex()

        if index == 0:
            self.cern.sort_by_id()
        elif index == 1:
            self.cern.sort_by_distancia()
        elif index == 2:
            self.cern.sort_by_velocidad()

        if self.grafo:
            grafo = self.cern.to_dict()

            formated = pformat(grafo, width=40, indent=1)
            print(formated)
            self.ui.salida.insertPlainText(formated)

        else:
            self.ui.salida.insertPlainText(str(self.cern))            
        
        self.mostrar_tabla()
        self.dibujar()

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