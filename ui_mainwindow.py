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
        MainWindow.resize(331, 511)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

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

        self.id = QSpinBox(self.groupBox)
        self.id.setObjectName(u"id")
        self.id.setMaximum(65535)

        self.gridLayout_4.addWidget(self.id, 0, 1, 1, 1)

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

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 3, 0, 1, 1)

        self.velocity = QSpinBox(self.groupBox)
        self.velocity.setObjectName(u"velocity")
        self.velocity.setMaximum(65535)

        self.gridLayout_4.addWidget(self.velocity, 3, 1, 1, 1)

        self.agregar_final_button = QPushButton(self.groupBox)
        self.agregar_final_button.setObjectName(u"agregar_final_button")

        self.gridLayout_4.addWidget(self.agregar_final_button, 6, 0, 1, 2)

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

        self.agregar_inicio_button = QPushButton(self.groupBox)
        self.agregar_inicio_button.setObjectName(u"agregar_inicio_button")

        self.gridLayout_4.addWidget(self.agregar_inicio_button, 5, 0, 1, 2)

        self.mostrar_button = QPushButton(self.groupBox)
        self.mostrar_button.setObjectName(u"mostrar_button")

        self.gridLayout_4.addWidget(self.mostrar_button, 7, 0, 1, 2)


        self.gridLayout_5.addWidget(self.groupBox, 1, 0, 1, 1)

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout_5.addWidget(self.salida, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 331, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Part\u00edcula", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Id", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Destino", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Color", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Green", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Red", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Blue", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Velocidad", None))
        self.agregar_final_button.setText(QCoreApplication.translate("MainWindow", u"Agregar al final", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"y", None))
        self.agregar_inicio_button.setText(QCoreApplication.translate("MainWindow", u"Agregar al inicio", None))
        self.mostrar_button.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

