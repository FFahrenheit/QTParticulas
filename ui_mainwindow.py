# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(681, 604)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionGrafo = QAction(MainWindow)
        self.actionGrafo.setObjectName(u"actionGrafo")
        self.action_grafo = QAction(MainWindow)
        self.action_grafo.setObjectName(u"action_grafo")
        self.action_lista = QAction(MainWindow)
        self.action_lista.setObjectName(u"action_lista")
        self.action_recorridos = QAction(MainWindow)
        self.action_recorridos.setObjectName(u"action_recorridos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.plainTextSort = QComboBox(self.tab)
        self.plainTextSort.addItem("")
        self.plainTextSort.addItem("")
        self.plainTextSort.addItem("")
        self.plainTextSort.setObjectName(u"plainTextSort")

        self.gridLayout_5.addWidget(self.plainTextSort, 3, 1, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_5.addWidget(self.salida, 4, 1, 1, 1)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_5.addWidget(self.label_10, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.origin_y = QSpinBox(self.groupBox_3)
        self.origin_y.setObjectName(u"origin_y")
        self.origin_y.setMinimum(0)
        self.origin_y.setMaximum(500)
        self.origin_y.setValue(0)

        self.gridLayout_3.addWidget(self.origin_y, 2, 1, 1, 1)

        self.origin_x = QSpinBox(self.groupBox_3)
        self.origin_x.setObjectName(u"origin_x")
        self.origin_x.setMaximum(500)

        self.gridLayout_3.addWidget(self.origin_x, 0, 1, 2, 1)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 2, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.velocity = QSpinBox(self.groupBox)
        self.velocity.setObjectName(u"velocity")
        self.velocity.setMaximum(65535)

        self.gridLayout_4.addWidget(self.velocity, 3, 1, 1, 1)

        self.agregar_final_button = QPushButton(self.groupBox)
        self.agregar_final_button.setObjectName(u"agregar_final_button")

        self.gridLayout_4.addWidget(self.agregar_final_button, 6, 0, 1, 2)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.color_g = QSpinBox(self.groupBox_2)
        self.color_g.setObjectName(u"color_g")
        self.color_g.setMaximum(255)

        self.gridLayout.addWidget(self.color_g, 2, 1, 3, 1)

        self.color_r = QSpinBox(self.groupBox_2)
        self.color_r.setObjectName(u"color_r")
        self.color_r.setMaximum(255)

        self.gridLayout.addWidget(self.color_r, 0, 1, 2, 1)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.color_b = QSpinBox(self.groupBox_2)
        self.color_b.setObjectName(u"color_b")
        self.color_b.setMaximum(255)

        self.gridLayout.addWidget(self.color_b, 5, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 2, 1)


        self.gridLayout_4.addWidget(self.groupBox_2, 4, 0, 1, 2)

        self.agregar_inicio_button = QPushButton(self.groupBox)
        self.agregar_inicio_button.setObjectName(u"agregar_inicio_button")

        self.gridLayout_4.addWidget(self.agregar_inicio_button, 5, 0, 1, 2)

        self.id = QSpinBox(self.groupBox)
        self.id.setObjectName(u"id")
        self.id.setMaximum(65535)

        self.gridLayout_4.addWidget(self.id, 0, 1, 1, 1)

        self.mostrar_button = QPushButton(self.groupBox)
        self.mostrar_button.setObjectName(u"mostrar_button")

        self.gridLayout_4.addWidget(self.mostrar_button, 7, 0, 1, 2)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_2 = QGridLayout(self.groupBox_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.destination_y = QSpinBox(self.groupBox_4)
        self.destination_y.setObjectName(u"destination_y")
        self.destination_y.setMaximum(500)

        self.gridLayout_2.addWidget(self.destination_y, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.destination_x = QSpinBox(self.groupBox_4)
        self.destination_x.setObjectName(u"destination_x")
        self.destination_x.setMaximum(500)

        self.gridLayout_2.addWidget(self.destination_x, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_4, 2, 0, 1, 2)

        self.grafo_button = QPushButton(self.groupBox)
        self.grafo_button.setObjectName(u"grafo_button")

        self.gridLayout_4.addWidget(self.grafo_button, 8, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 4, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_7.addWidget(self.mostrar_tabla_pushButton, 1, 3, 1, 1)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_7.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_7.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_7.addWidget(self.tabla, 0, 0, 1, 4)

        self.tableSort = QComboBox(self.tab_2)
        self.tableSort.addItem("")
        self.tableSort.addItem("")
        self.tableSort.addItem("")
        self.tableSort.setObjectName(u"tableSort")

        self.gridLayout_7.addWidget(self.tableSort, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_8 = QGridLayout(self.tab_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")

        self.gridLayout_8.addWidget(self.graphicsView, 0, 0, 1, 2)

        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")

        self.gridLayout_8.addWidget(self.dibujar, 1, 0, 1, 1)

        self.borrar = QPushButton(self.tab_3)
        self.borrar.setObjectName(u"borrar")

        self.gridLayout_8.addWidget(self.borrar, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_6.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 681, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuVer = QMenu(self.menubar)
        self.menuVer.setObjectName(u"menuVer")
        self.menuAlgoritmos = QMenu(self.menubar)
        self.menuAlgoritmos.setObjectName(u"menuAlgoritmos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuVer.menuAction())
        self.menubar.addAction(self.menuAlgoritmos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuVer.addAction(self.action_grafo)
        self.menuVer.addAction(self.action_lista)
        self.menuAlgoritmos.addAction(self.action_recorridos)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
        self.actionGrafo.setText(QCoreApplication.translate("MainWindow", u"Convertir a Grafo", None))
#if QT_CONFIG(shortcut)
        self.actionGrafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.action_grafo.setText(QCoreApplication.translate("MainWindow", u"Ver como grafo", None))
#if QT_CONFIG(shortcut)
        self.action_grafo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.action_lista.setText(QCoreApplication.translate("MainWindow", u"Ver como lista", None))
#if QT_CONFIG(shortcut)
        self.action_lista.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+L", None))
#endif // QT_CONFIG(shortcut)
        self.action_recorridos.setText(QCoreApplication.translate("MainWindow", u"Recorridos (profundidad/anchura)", None))
#if QT_CONFIG(shortcut)
        self.action_recorridos.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.plainTextSort.setItemText(0, QCoreApplication.translate("MainWindow", u"Id ascendente", None))
        self.plainTextSort.setItemText(1, QCoreApplication.translate("MainWindow", u"Distancia descendente", None))
        self.plainTextSort.setItemText(2, QCoreApplication.translate("MainWindow", u"Velocidad ascendente", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.agregar_final_button.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.agregar_inicio_button.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.mostrar_button.setText(QCoreApplication.translate("MainWindow", u"Mostrar plano", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.grafo_button.setText(QCoreApplication.translate("MainWindow", u"Mostrar grafo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Id de la particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.tableSort.setItemText(0, QCoreApplication.translate("MainWindow", u"Id ascendente", None))
        self.tableSort.setItemText(1, QCoreApplication.translate("MainWindow", u"Distancia descendente", None))
        self.tableSort.setItemText(2, QCoreApplication.translate("MainWindow", u"Velocidad ascendente", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.borrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuVer.setTitle(QCoreApplication.translate("MainWindow", u"Ver", None))
        self.menuAlgoritmos.setTitle(QCoreApplication.translate("MainWindow", u"Algoritmos", None))
    # retranslateUi

