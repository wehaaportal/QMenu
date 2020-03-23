# -*- coding: utf-8 -*-
#=============================================
#
#	QMenú 0.1
#	(c) Wehaa Portal Soft.
#
#=============================================
from __future__ import unicode_literals
from datetime import date, datetime
import os, sys, json

''' PyQt5 '''
from PyQt5 import Qt, QtWidgets, QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

''' PyQt5 Gui '''
from views.Ui_main import Ui_windows

from variables import HOME_QMENU_PATH, DATABASE_PATH
from controlador import Ctrl

class WQMenu(QtWidgets.QMainWindow, Ui_windows, Ctrl):
	imagen = ok = ""
	def __init__(self):
		# Cargar Controlador		
		Ctrl.__init__(self)

		# Iniciando QMenú
		super(WQMenu, self).__init__()
		self.setupUi(self)

		# Pantalla Completa
		self.showFullScreen()

		# Configuración de Tablas
		self.tableWidget.setColumnCount(4)
		self.tableWidget.setHorizontalHeaderLabels(['FECHA', 'MENÚ', 'GENERAL', 'N°'])
		
		self.tableWidget.setAlternatingRowColors(True)
		self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
		self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
		self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
		self.tableWidget.setColumnWidth(0, 150)
		self.tableWidget.setColumnWidth(1, 520)
		self.tableWidget.setColumnWidth(2, 520)
		self.tableWidget.setColumnWidth(3, 50)
		self.tableWidget.setShowGrid(True)

		# Funciones de los botones
		self.btnClose.clicked.connect(self.close)
		self.btnPDF.clicked.connect(self.generarPDF)
		self.btnEdit.clicked.connect(self.editarMenu)	
		self.btnClean.clicked.connect(self.eliminarDatos)

		self.btnDB.clicked.connect(self.insertarDatos)
		self.btnSave.clicked.connect(self.guardarGeneral)		

		self.btnADDLOGO.clicked.connect(self.cargarLogo)

	def closeEvent(self, event):
		reply = QMessageBox.question(self,
									'Salir',
									"Realmente desea salir de QMenú",
									QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def _firstRun(self):
		# Iniciar por primera vez QMenú
		# Directorio
		for directory in (HOME_QMENU_PATH, DATABASE_PATH):
			if not os.path.isdir(directory):
				os.mkdir(directory, 0o777)

		# Iniciar Data Base
		self.initDB('base_de_datos.db', 'QSQLITE')


if __name__ == '__main__':
	app = QApplication(sys.argv)
	qm = WQMenu()

	# Comprobar primer arranque
	if not os.path.exists(HOME_QMENU_PATH):
		qm._firstRun()
	else:
		qm.initDB('base_de_datos.db', 'QSQLITE')

	# Mostrar QMenú
	qm.show()

	sys.exit(app.exec_())

