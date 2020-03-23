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
from PyQt5 import Qt, QtWidgets, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.Qt import QDesktopServices, QUrl
from PyQt5.Qt import QTextDocument, QPrinter

from variables import HOME_QMENU_PATH, DATABASE_PATH, WORKING_FOLDER

class Ctrl():
	menu = grl = ""
	edit = False
	idEdit = fechaEdit = ""
	def __init__(self):
		# Controlador
		pass

	def generarPDF(self):
		selected = self.tableWidget.currentIndex()
		if not selected.isValid() or len(self.tableWidget.selectedItems()) < 1:
			QtWidgets.QMessageBox.information(self, '¡Por Favor!', 'Se debe selecionar un Menú', QtWidgets.QMessageBox.Ok)
			return
			
		ids = self.tableWidget.selectedItems()[3]
		query = QSqlQuery()
		query.exec_("select * from qmenu where id = " + ids.text())
		query.first()

		_id = query.value(0)
		_fecha = query.value(1)
		_menu = json.loads(query.value(2)) 
		_grl = json.loads(query.value(3))

		i = 0
		semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

		rowsHtml = social = free = ''

		while i < len(_menu):
			dia = semana[i].lower()

			if _menu[dia][0] != "" or _menu[dia][1] != "":
				rowsHtml += """
						<br>
						<tr><td></td></tr>
						<tr height="10" color="#000000" style=" background-color: #f5f5f5;">
							<td align="center"><span tyle="font-family: Calibri ;font-style: normal;">"""+semana[i].upper()+"""</span></td>
						</tr>
                        <tr height="50" >
                        	<td width="20%" align="center" style="background-color: #f5f5f5;">
                        		<br>
                        		<IMG SRC="bkp/cheff.png" width="80" height="80">                                
                            </td>
                            <td align="center" width="80%" style="background-color: #f5f5f5; font-family: Bradley Hand ITC; font-size: 10pt;">
                            	<br>
                            	 """+ _menu[dia][0] + """
                            	<br><br>
                            	 """+ _menu[dia][1] + """
                            </td>
                        </tr>
                        """		
			i += 1

		if _grl['face'] != '':
			social += """<IMG SRC="bkp/icons8-facebook-100.png" width="15" height="15"> <span style="color:#4169E1">"""+ _grl['face'] + """ </span><br>"""
		if _grl['inst'] != '':
			social += """<IMG SRC="bkp/icons8-instagram-100.png" width="15" height="15"> <span style="color:#4169E1">"""+ _grl['inst'] + """ </span><br>"""
		if _grl['twit'] != '':
			social += """<IMG SRC="bkp/icons8-twitter-100.png" width="15" height="15"> <span style="color:#4169E1">"""+ _grl['twit'] + """ </span><br>"""
		if _grl['wsp'] != '':
			social += """<IMG SRC="bkp/icons8-whatsapp-100.png" width="15" height="15"> <span style="color:#4169E1">"""+ _grl['wsp'] + """ </span><br>"""   

		if _grl['free'] != False:
			free += """<IMG SRC="bkp/free.png" width="60" height="60">"""  

		html = """
                     <table width="600">
                        <tr width="600" color="#000000">
                        	<td width="20%" align="left">
                                <IMG SRC="""+ _grl['foto'] + """ width="100" height="100">                                
                            </td>
                            <td width="60%" align="center">
                               <h1 style="color: #FF8C00;font-family: Ink Free; font-style: italic;">"""+ _grl['nombre']+ """ </h1>
                               <h2 style="font-family: Bradley Hand ITC;">"""+ _grl['description'] + """ </h2><br>
                            </td>
                            <td width="20%" align="right">
                                <IMG SRC="""+ _grl['foto'] + """ width="100" height="100">
                            </td>
                        </tr>

                    </table>
                    _____________________________________________________________________________________________________

                    <table width="600">
                    	""" +rowsHtml+"""
                    	<br>
                    </table>
                    <br>

                    _____________________________________________________________________________________________________

                    <table width="600">
                    <br>
                    	<tr>
                    		<td align="left" width="50%">
                    			""" +social+"""
                    		</td>
                    		<td align="center" width="30%">
                    			<span style="color:#FF4500;"> Pedido hasta las """+_grl['pedido']+"""</span><br>
                    			</td>
                    		<td align="right" width="20%">                    			
                    			"""+free+"""
                    		</td>
                    	</tr>
                    </table>
                    _____________________________________________________________________________________________________
                    <table width="600">
                    <br>
                        <tr>
                            <td align="left" width="80%">
                            FECHA/HORA : """+ _fecha + """
                            </td>
                            <td align="right">
                            N° : """+ str(_id) +"""
                            </td>
                        </tr>
                    </table>
                    _____________________________________________________________________________________________________
                    <table width="600">
                        <tr>
                            <td align="left" width="80%" style=" font-size: 4; color: #C0C0C0; ">
                            Generado por QMenú 0.1
                            </td>
                        </tr>
                    </table>

                """

        # Nombre del PDF
		self.nombrePdf = 'menu_{0}.pdf'.format(query.value(0))
		doc = QTextDocument()
		doc.setHtml(html)
		printer = QPrinter()
		printer.setOutputFileName(self.nombrePdf)

		printer.setOutputFormat(QPrinter.PdfFormat)
		doc.print(printer)
		printer.newPage()
		# Abrir archivo
		url = QUrl
		url = QUrl(self.nombrePdf)
		QDesktopServices.openUrl(url)

	def editarMenu(self):
		selected = self.tableWidget.currentIndex()
		if not selected.isValid() or len(self.tableWidget.selectedItems()) < 1:
			QtWidgets.QMessageBox.information(self, '¡Por Favor!', 'Se debe selecionar un Menú', QtWidgets.QMessageBox.Ok)
			return
		ids = self.tableWidget.selectedItems()[3]
		query = QSqlQuery()
		query.exec_("select * from qmenu where id = " + ids.text())
		query.first()

		reply = QtWidgets.QMessageBox.question(self,
									'Editar',
									"Realmente desea editar Menú: '{0}'".format(ids.text()),
									QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if reply == QtWidgets.QMessageBox.Yes:
			_id = query.value(0)
			_fecha = query.value(1)
			_menu = json.loads(query.value(2)) 
			_grl = json.loads(query.value(3))

			self.edit = True
			self.idEdit = _id
			self.fechaEdit = _fecha

			if _menu['lunes'][2] != '':
				self.groupBox.setChecked(_menu['lunes'][2])
				self.primerPlatoLineEdit.setText(_menu['lunes'][0])
				self.segundoPlatoLineEdit.setText(_menu['lunes'][1])
			if _menu['martes'][2] != '':
				self.groupBox_2.setChecked(_menu['martes'][2])
				self.primerPlatoLineEdit_2.setText(_menu['martes'][0])
				self.segundoPlatoLineEdit_2.setText(_menu['martes'][1])
			if _menu['miercoles'][2] != '':
				self.groupBox_3.setChecked(_menu['miercoles'][2])
				self.primerPlatoLineEdit_3.setText(_menu['miercoles'][0])
				self.segundoPlatoLineEdit_3.setText(_menu['miercoles'][1])
			if _menu['jueves'][2] != '':
				self.groupBox_4.setChecked(_menu['jueves'][2])
				self.primerPlatoLineEdit_4.setText(_menu['jueves'][0])
				self.segundoPlatoLineEdit_4.setText(_menu['jueves'][1])
			if _menu['viernes'][2] != '':
				self.groupBox_5.setChecked(_menu['viernes'][2])
				self.primerPlatoLineEdit_5.setText(_menu['viernes'][0])
				self.segundoPlatoLineEdit_5.setText(_menu['viernes'][1])

			# General 
			self.imagen = _grl["foto"]

			self.nombreLineEdit.setText(_grl["nombre"])
			self.descripciNLineEdit.setText(_grl["description"])
			t = _grl["pedido"].split(':')
			self.pedidoHastaTimeEdit.setTime(QTime(int(t[0]), int(t[1]))) #HH : MM 
			self.envioGratisCheckBox.setChecked(_grl["free"])
			self.facebookLineEdit.setText(_grl["face"])
			self.instagramLineEdit.setText(_grl["inst"])
			self.twitterLineEdit.setText(_grl["twit"])
			self.whatsappLineEdit.setText(_grl["wsp"]) 
			self.imgLogo.setPixmap(QPixmap(_grl["foto"]))


	def insertarDatos(self):
		if self.groupBox.isChecked():
			lpc = self.primerPlatoLineEdit.text()
			lsc = self.segundoPlatoLineEdit.text()
			lc = self.groupBox.isChecked()
		else:
			lpc = lsc = lc = ""
		if self.groupBox_2.isChecked():
			mpc = self.primerPlatoLineEdit_2.text()
			msc = self.segundoPlatoLineEdit_2.text()
			mc = self.groupBox_2.isChecked()
		else:
			mpc = msc = mc = ""
		if self.groupBox_3.isChecked():
			mxpc = self.primerPlatoLineEdit_3.text()
			mxsc = self.segundoPlatoLineEdit_3.text()
			mxc = self.groupBox_3.isChecked()
		else:
			mxpc = mxsc = mxc =""
		if self.groupBox_4.isChecked():
			jpc = self.primerPlatoLineEdit_4.text()
			jsc = self.segundoPlatoLineEdit_4.text()
			jc = self.groupBox_4.isChecked()
		else:
			jpc = jsc = jc =""
		if self.groupBox_5.isChecked():
			vpc = self.primerPlatoLineEdit_5.text()
			vsc = self.segundoPlatoLineEdit_5.text()
			vc = self.groupBox_5.isChecked()
		else:
			vpc = vsc =  vc = ""

		self.grl = json.dumps({
			"nombre" : self.nombreLineEdit.text(),
			"description" : self.descripciNLineEdit.text(),
			"pedido" : self.pedidoHastaTimeEdit.text(), #HH : MM : SS
			"free" : self.envioGratisCheckBox.isChecked(),
			"face" : self.facebookLineEdit.text(),
			"inst" : self.instagramLineEdit.text(),
			"twit" : self.twitterLineEdit.text(),
			"wsp" : self.whatsappLineEdit.text(), 
			"foto" : self.imagen,            
		})

		self.menu = json.dumps({
			'lunes': [lpc, lsc, lc], 
			'martes': [mpc, msc, mc], 
			'miercoles': [mxpc, mxsc, mxc], 
			'jueves': [jpc, jsc, jc], 
			'viernes':[vpc, vsc, vc]})

		created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

		msg = "Realmente desea guardar Menú \n en la Base de Datos" if not self.edit else "Realmente desea editar Menu: '{0}'".format(str(self.idEdit))

		reply = QtWidgets.QMessageBox.question(self,
									'Guardar',
									msg,
									QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if reply == QtWidgets.QMessageBox.Yes:
			query = QSqlQuery()
			if not self.edit:
				query.exec_("insert into qmenu(created, menu, grl) values('{0}', '{1}', '{2}')".format(created, self.menu, self.grl))
			else:
				print(self.idEdit, self.fechaEdit)
				query.prepare("update qmenu set created = :created, menu = :menu , grl = :grl WHERE id="""+str(self.idEdit)+"")
				query.bindValue(":created", self.fechaEdit)
				query.bindValue(":menu",self.menu)
				query.bindValue(":grl",self.grl)
				status = query.exec_()

				if status is not True:
					errorText = query.lastError().text()
					QtWidgets.QMessageBox.critical(self, 'Query error', errorText)
				self.edit = False
				self.fechaEdit = self.idEdit = ""

		self.limpiarMenu()
		self.cargarDatos()

	def limpiarMenu(self):
		# Lunes
		self.groupBox.setChecked(False)
		self.primerPlatoLineEdit.setText("")
		self.segundoPlatoLineEdit.setText("")
		# Martes
		self.groupBox_2.setChecked(False)
		self.primerPlatoLineEdit_2.setText("")
		self.segundoPlatoLineEdit_2.setText("")
		# Miercoles
		self.groupBox_3.setChecked(False)
		self.primerPlatoLineEdit_3.setText("")
		self.segundoPlatoLineEdit_3.setText("")
		# Jueves
		self.groupBox_4.setChecked(False)
		self.primerPlatoLineEdit_4.setText("")
		self.segundoPlatoLineEdit_4.setText("")
		# Viernes
		self.groupBox_5.setChecked(False)
		self.primerPlatoLineEdit_5.setText("")
		self.segundoPlatoLineEdit_5.setText("")

		self.menu = self.grl = ""

	def cargarLogo(self):
		self.imagen, self.extension = QtWidgets.QFileDialog.getOpenFileName(self, "Seleccionar imagen", os.getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QtWidgets.QFileDialog.Options())

		if self.imagen:
			self.pixmapImagen = QPixmap(self.imagen).scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
			self.imgLogo.setPixmap(self.pixmapImagen)

	def cargarGeneral(self):
		with open(os.sep.join([WORKING_FOLDER,'bkp','datos_general.cfg']),'r') as f:
			_grl = json.load(f)

		self.imagen = _grl["foto"]

		self.nombreLineEdit.setText(_grl["nombre"])
		self.descripciNLineEdit.setText(_grl["description"])
		t = _grl["pedido"].split(':')
		self.pedidoHastaTimeEdit.setTime(QTime(int(t[0]), int(t[1]))) #HH : MM 
		self.envioGratisCheckBox.setChecked(_grl["free"])
		self.facebookLineEdit.setText(_grl["face"])
		self.instagramLineEdit.setText(_grl["inst"])
		self.twitterLineEdit.setText(_grl["twit"])
		self.whatsappLineEdit.setText(_grl["wsp"]) 
		self.imgLogo.setPixmap(QPixmap(_grl["foto"]))

	def guardarGeneral(self):
		foto = self.imagen
		photo = self.imgLogo.pixmap()
		photo.save("imagen/{0}.png".format('new_logo'), quality = 100)

		grl = {
			"nombre" : self.nombreLineEdit.text(),
			"description" : self.descripciNLineEdit.text(),
			"pedido" : self.pedidoHastaTimeEdit.text(), #HH : MM : SS
			"free" : self.envioGratisCheckBox.isChecked(),
			"face" : self.facebookLineEdit.text(),
			"inst" : self.instagramLineEdit.text(),
			"twit" : self.twitterLineEdit.text(),
			"wsp" : self.whatsappLineEdit.text(), 
			"foto" : foto,            
		}

		reply = QtWidgets.QMessageBox.question(self,
									'Guardar',
									"Realmente desea guardar Datos General",
									QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if reply == QtWidgets.QMessageBox.Yes:
			with open(os.sep.join([WORKING_FOLDER,'bkp','datos_general.cfg']), 'w') as salida:
				a = json.dump(grl, salida)

	def cargarDatos(self):
		index = 0
		query = QSqlQuery()
		query.exec_("select * from qmenu")

		while query.next():
			ids = query.value(0)
			fecha = query.value(1)
			menu = query.value(2)
			grl = query.value(3)

			self.tableWidget.setRowCount(index + 1)
			self.tableWidget.setItem(index, 0, QtWidgets.QTableWidgetItem(str(fecha)))
			self.tableWidget.setItem(index, 1, QtWidgets.QTableWidgetItem(menu))
			self.tableWidget.setItem(index, 2, QtWidgets.QTableWidgetItem(grl))
			self.tableWidget.setItem(index, 3, QtWidgets.QTableWidgetItem(str(ids)))

			index += 1

	def eliminarDatos(self, event):
		selected = self.tableWidget.currentIndex()
		if not selected.isValid() or len(self.tableWidget.selectedItems()) < 1:
			QtWidgets.QMessageBox.information(self, '¡Por Favor!', 'Se debe selecionar un Menú', QtWidgets.QMessageBox.Ok)
			return

		ids = self.tableWidget.selectedItems()[3]
		reply = QtWidgets.QMessageBox.question(self,
									'Eliminar',
									"Realmente desea eliminar\n\n - Menú: '{0}'".format(ids.text()),
									QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if reply == QtWidgets.QMessageBox.Yes:			
			query = QSqlQuery()
			query.exec_("delete from qmenu where id = " + ids.text())		

			self.tableWidget.removeRow(selected.row())
			self.tableWidget.setCurrentIndex(QModelIndex())

			return True
		else:
			return

	def db_create(self):
		query = QSqlQuery()
		query.exec_("create table qmenu(id INTEGER PRIMARY KEY AUTOINCREMENT, "
				"created DATE, menu longtext, grl longtext)")
		#query.exec_("insert into qmenu values(1, '2020-01-01', 'Wehaa Portal Soft.', 'Eliminar este Ejemplo!')")

	def db_connect(self, filename, server):
		db = QSqlDatabase.addDatabase(server)
		db.setDatabaseName(filename)
		if not db.open():
			QMessageBox.critical(None, "No se puede abrir Base de Datos",
					"No se puede establecer conección.\n\n"
					"Click Cancelar para salir.", QMessageBox.Cancel)
			return False
		return True

	def initDB(self, filename, server):
		filename = "{0}/{1}".format(DATABASE_PATH, filename)
		if not os.path.exists(filename):
			self.db_connect(filename, server)
			self.db_create()
		else:
			self.db_connect(filename, server)

		self.cargarDatos()
		self.cargarGeneral()