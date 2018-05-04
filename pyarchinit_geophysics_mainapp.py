#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***************************************************************************
        pyArchInit Plugin  - A QGIS plugin to manage archaeological dataset
        					 stored in Postgres
                             -------------------
    begin                : 2007-12-01
    copyright            : (C) 2008 by Luca Mandolesi
    email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import csv_writer
from csv_writer import *
import sys, os

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *


try:
	from qgis.core import *
	from qgis.gui import *
except:
	pass

from datetime import date
from psycopg2 import *

# from  pyarchinit_exp_Geophysics_pdf import *

# --import pyArchInit modules--#
from  pyarchinit_geophysics_ui import Ui_DialogGeo
from  pyarchinit_geophysics_ui import *
from  pyarchinit_utility import *
from  pyarchinit_error_check import *

try:
	from  pyarchinit_db_manager import *
except:
	pass
from  sortpanelmain import SortPanelMain

##from  pyarchinit_exp_Findssheet_pdf import *

import numpy as np
from numpy import *

from delegateComboBox import *


class pyarchinit_Geophysics(QDialog, Ui_DialogGeo):
	MSG_BOX_TITLE = "PyArchInit - Scheda Geofisica"
	DATA_LIST = []
	DATA_LIST_REC_CORR = []
	DATA_LIST_REC_TEMP = []
	REC_CORR = 0
	REC_TOT = 0
	BROWSE_STATUS = "b"
	STATUS_ITEMS = {"b": "Usa", "f": "Trova", "n": "Nuovo Record"}
	SORT_MODE = 'asc'
	SORTED_ITEMS = {"n": "Non ordinati", "o": "Ordinati"}
	SORT_STATUS = "n"
	UTILITY = Utility()
	DB_MANAGER = ""
	TABLE_NAME = 'geophysics_table'
	MAPPER_TABLE_CLASS = "GEOFISICA"
	NOME_SCHEDA = "Scheda Geofisica"
	ID_TABLE = "id_grid"
	
	CONVERSION_DICT = {ID_TABLE: ID_TABLE, "Sito": "sito", "Progetto": "progetto", "Metodo": "metodo", "Anno": "anno",
		"Settore": "settore", "Area": "area", "Griglia": "griglia", "Piano di Campagna": "pdc",
		"Quota assoluta": "quota", "Descrizione": "descrizione", "Interpretazione": "interpretazione",
		"Schedatore": 'schedatore', "Data schedatura": 'data_schedatura', "Modello": 'modello', "Velocita'": 'velocita',
		"X": 'x', "Y": 'y', "Data": "date", "Frequenza": "frequenza", "Risoluzione": "risoluzione",
		"Massima Profondita'": "max_prof", "Range(ns)": "range", "Bibliografia": "bibliografia"}
	
	SORT_ITEMS = [ID_TABLE, "Sito", "Progetto", "Metodo", "Anno", "Settore", "Area", "Griglia", "Piano di Campagna",
		"Quota assoluta", "Descrizione", "Interpretazione", "Schedatore", "Data schedatura", "Modello", "Velocita'",
		"X", "Y", "Data", "Frequenza", "Risoluzione", "Massima Profondita'", "Range(ns)", "Bibliografia"]
	
	TABLE_FIELDS = ["sito", "progetto", "metodo", "anno", "settore", "area", "griglia", "pdc", "quota", "descrizione",
		"interpretazione", "schedatore", "data_schedatura", "modello", "velocita", "x", "y", "date", "frequenza",
		"risoluzione", "max_prof", "range", "bibliografia"]
	
	TABLE_FIELDS_UPDATE = ["sito", "progetto", "metodo", "anno", "settore", "area", "griglia", "pdc", "quota",
	                       "descrizione", "interpretazione", "schedatore", "data_schedatura", "modello", "velocita",
	                       "x", "y", "date", "frequenza", "risoluzione", "max_prof", "range", "bibliografia"]
	
	SEARCH_DICT_TEMP = ""
	
	if os.name == 'posix':
		HOME = os.environ['HOME']
	elif os.name == 'nt':
		HOME = os.environ['HOMEPATH']
	
	# QUANT_PATH = ('%s%s%s') % (HOME, os.sep, "pyarchinit_Quantificazioni_folder")
	
	DB_SERVER = 'not defined'
	
	def __init__(self, iface):
		self.iface = iface
		
		QDialog.__init__(self)
		self.setupUi(self)
		self.currentLayerId = None
		try:
			self.on_pushButton_connect_pressed()
		except Exception, e:
			QMessageBox.warning(self, "Sistema di connessione", str(e), QMessageBox.Ok)
	
	def enable_button(self, n):
		# self.pushButton_connect.setEnabled(n)
		
		self.pushButton_new_rec.setEnabled(n)
		
		# self.pushButton_view_all_2.setEnabled(n)
		
		self.pushButton_first_rec.setEnabled(n)
		
		self.pushButton_last_rec.setEnabled(n)
		
		self.pushButton_prev_rec.setEnabled(n)
		
		self.pushButton_next_rec.setEnabled(n)
		
		self.pushButton_delete.setEnabled(n)
		
		self.pushButton_new_search.setEnabled(n)
		
		self.pushButton_search_go.setEnabled(n)
		
		self.pushButton_sort.setEnabled(n)
	
	def enable_button_search(self, n):
		self.pushButton_connect.setEnabled(n)
		
		self.pushButton_new_rec.setEnabled(n)
		
		self.pushButton_view_all_2.setEnabled(n)
		
		self.pushButton_first_rec.setEnabled(n)
		
		self.pushButton_last_rec.setEnabled(n)
		
		self.pushButton_prev_rec.setEnabled(n)
		
		self.pushButton_next_rec.setEnabled(n)
		
		self.pushButton_delete.setEnabled(n)
		
		self.pushButton_save.setEnabled(n)
		
		self.pushButton_sort.setEnabled(n)
	
	def on_pushButton_connect_pressed(self):
		from pyarchinit_conn_strings import *
		# self.setComboBoxEditable(["self.comboBox_sito"],1)
		conn = Connection()
		conn_str = conn.conn_str()
		
		test_conn = conn_str.find('sqlite')
		
		if test_conn == 0:
			self.DB_SERVER = "sqlite"
		
		try:
			self.DB_MANAGER = Pyarchinit_db_management(conn_str)
			self.DB_MANAGER.connection()
			self.charge_records()
			# check if DB is empty
			if bool(self.DATA_LIST) == True:
				self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), 0
				self.DATA_LIST_REC_TEMP = self.DATA_LIST_REC_CORR = self.DATA_LIST[0]
				self.BROWSE_STATUS = "b"
				self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
				self.label_sort.setText(self.SORTED_ITEMS["n"])
				self.set_rec_counter(len(self.DATA_LIST), self.REC_CORR + 1)
				self.charge_list()
				self.fill_fields()
			else:
				QMessageBox.warning(self, "BENVENUTO",
				                    "Benvenuto in pyArchInit" + self.NOME_SCHEDA + ". Il database e' vuoto. Premi 'Ok' e buon lavoro!",
				                    QMessageBox.Ok)
				
				self.charge_list()
				self.BROWSE_STATUS = 'x'
				self.on_pushButton_new_rec_pressed()
		except Exception, e:
			e = str(e)
			if e.find("no such table"):
				QMessageBox.warning(self, "Alert",
				                    "La connessione e' fallita <br><br> E' NECESSARIO RIAVVIARE QGIS " + e,
				                    QMessageBox.Ok)
			else:
				QMessageBox.warning(self, "Alert",
				                    "Attenzione rilevato bug! Segnalarlo allo sviluppatore<br> Errore: <br>" + str(e),
				                    QMessageBox.Ok)
	
	def customize_gui(self):
		# media prevew system
		self.iconListWidget = QtGui.QListWidget(self)
		self.iconListWidget.setFrameShape(QtGui.QFrame.StyledPanel)
		self.iconListWidget.setFrameShadow(QtGui.QFrame.Sunken)
		self.iconListWidget.setLineWidth(2)
		self.iconListWidget.setMidLineWidth(2)
		self.iconListWidget.setProperty("showDropIndicator", False)
		self.iconListWidget.setIconSize(QtCore.QSize(150, 150))
		self.iconListWidget.setMovement(QtGui.QListView.Snap)
		self.iconListWidget.setResizeMode(QtGui.QListView.Adjust)
		self.iconListWidget.setLayoutMode(QtGui.QListView.Batched)
		self.iconListWidget.setGridSize(QtCore.QSize(160, 160))
		self.iconListWidget.setViewMode(QtGui.QListView.IconMode)
		self.iconListWidget.setUniformItemSizes(True)
		self.iconListWidget.setBatchSize(1000)
		self.iconListWidget.setObjectName("iconListWidget")
		self.iconListWidget.SelectionMode()
		self.iconListWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
		self.connect(self.iconListWidget, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.openWide_image)
		self.tabWidget.addTab(self.iconListWidget, "Media")
		
		"""
        # delegate combobox

        #		valuesTE = ["frammento", "frammenti", "intero", "integro"]
        #		self.delegateTE = ComboBoxDelegate()
        #		self.delegateTE.def_values(valuesTE)
        #		self.delegateTE.def_editable('False')
        #		self.tableWidget_elementi_reperto.setItemDelegateForColumn(1,self.delegateTE)


        #	def loadMediaPreview(self, mode = 0):
        self.iconListWidget.clear()
        if mode == 0:
            # if has geometry column load to map canvas

            rec_list = self.ID_TABLE + " = " + str(eval("self.DATA_LIST[int(self.REC_CORR)]." + self.ID_TABLE))
            search_dict = {'id_entity': "'" + str(eval("self.DATA_LIST[int(self.REC_CORR)]." + self.ID_TABLE)) + "'",
                           'entity_type': "'REPERTO'"}
            record_us_list = self.DB_MANAGER.query_bool(search_dict, 'MEDIATOENTITY')
            for i in record_us_list:
                search_dict = {'id_media': "'" + str(i.id_media) + "'"}

                u = Utility()
                search_dict = u.remove_empty_items_fr_dict(search_dict)
                mediathumb_data = self.DB_MANAGER.query_bool(search_dict, "MEDIA_THUMB")
                thumb_path = str(mediathumb_data[0].filepath)

                item = QListWidgetItem(str(i.id_media))

                item.setData(QtCore.Qt.UserRole, str(i.id_media))
                icon = QIcon(thumb_path)
                item.setIcon(icon)
                self.iconListWidget.addItem(item)
        elif mode == 1:
            self.iconListWidget.clear()
        """
	
	"""
    def openWide_image(self):
        items = self.iconListWidget.selectedItems()
        for item in items:
            dlg = ImageViewer(self)
            id_orig_item = item.text()  # return the name of original file

            search_dict = {'id_media': "'" + str(id_orig_item) + "'"}

            u = Utility()
            search_dict = u.remove_empty_items_fr_dict(search_dict)

            try:
                res = self.DB_MANAGER.query_bool(search_dict, "MEDIA")
                file_path = str(res[0].filepath)
            except Exception, e:
                QMessageBox.warning(self, "Errore", "Attenzione 1 file: " + str(e), QMessageBox.Ok)

            dlg.show_image(unicode(file_path))  # item.data(QtCore.Qt.UserRole).toString()))
            dlg.exec_()
    """

	def insert_new_rec(self):
		##bibliografia
		bibliografia = self.table2dict("self.tableWidget_bibliografia")
		
		try:
			if self.lineEdit_pdc.text() == "":
				pdc = None
			else:
				pdc = float(self.lineEdit_pdc.text())
			
			if self.lineEdit_quota.text() == "":
				quota = None
			else:
				quota = float(self.lineEdit_quota.text())
			
			if self.lineEdit_risoluzione.text() == "":
				risoluzione = None
			else:
				risoluzione = float(self.lineEdit_risoluzione.text())
				
			data = self.DB_MANAGER.insert_geophysics_values(
				self.DB_MANAGER.max_num_id(self.MAPPER_TABLE_CLASS, self.ID_TABLE) + 1,  # 0 - IDsito
				unicode(self.comboBox_sito.currentText()),  # 1 - Sito
				unicode(self.lineEdit_progetto.text()),  # 2 - progetto
				unicode(self.comboBox_metodo.currentText()),  # 3 - metodo
				unicode(self.lineEdit_anno.text()),  # 4 - definizione
				unicode(self.lineEdit_settore.text()),  # 5 settore
				unicode(self.comboBox_area.currentText()),  # 6 - descrizione
				unicode(self.lineEdit_griglia.text()),  # 7 - griglia
				pdc,  # 8 - piano di campagna
				quota,  # 9 - quota
				unicode(self.textEdit_descrizione.toPlainText()),  # 10 - descrizione
				unicode(self.textEdit_interpretazione.toPlainText),  # 11 - interpretazione
				unicode(self.comboBox_schedatore.currentText()),  # 12 - schedatore
				unicode(self.lineEdit_data_schedatura.text()),  # 13 - data schedatura
				unicode(self.comboBox_modello.currentText()),  # 14 - modello
				unicode(self.comboBox_velocita.currentText()),  # 15 - velocita'
				unicode(self.comboBox_frequenza.currentText()),  # 16 - frequenza
				risoluzione,  # 17 - risoluzione
				unicode(self.lineEdit_max_prof.text()),  # 18 - max_prof
				unicode(self.lineEdit_range.text()),  # 19 - range
				unicode(self.lineEdit_x.text()),  # 20
				unicode (self.lineEdit_y.text()),  # 21
				unicode (self.lineEdit_date.text()),  # 22 - risoluzione
				str(bibliografia)) #23
			
			try:
				self.DB_MANAGER.insert_data_session(data)
				return 1
			except Exception, e:
				e_str = str(e)
				if e_str.__contains__("Integrity"):
					msg = self.ID_TABLE + " gia' presente nel database"
				else:
					msg = e
				QMessageBox.warning(self, "Errore", "immissione 1 \n" + str(msg), QMessageBox.Ok)
				return 0
			
			finally:
				pass
		
		except Exception, e:
			QMessageBox.warning(self, "Attenzione", "Errore di immissione 2 \n" + str(e), QMessageBox.Ok)
			return 0
	
	def charge_list(self):
		sito_vl = self.UTILITY.tup_2_list_III(self.DB_MANAGER.group_by('site_table', 'sito', 'SITE'))
		try:
			sito_vl.remove('')
		except Exception, e:
			if str(e) == "list.remove(x): x not in list":
				pass
			else:
				QMessageBox.warning(self, "Messaggio", "Sistema di aggiornamento lista Sito: " + str(e), QMessageBox.Ok)
		
		self.comboBox_sito.clear()
		sito_vl.sort()
		self.comboBox_sito.addItems(sito_vl)
	
	# buttons functions
	def on_pushButton_sort_pressed(self):
		if self.check_record_state() == 1:
			pass
		else:
			dlg = SortPanelMain(self)
			dlg.insertItems(self.SORT_ITEMS)
			dlg.exec_()
			
			items, order_type = dlg.ITEMS, dlg.TYPE_ORDER
			
			self.SORT_ITEMS_CONVERTED = []
			for i in items:
				self.SORT_ITEMS_CONVERTED.append(self.CONVERSION_DICT[unicode(i)])
			
			self.SORT_MODE = order_type
			self.empty_fields()
			
			id_list = []
			for i in self.DATA_LIST:
				id_list.append(eval("i." + self.ID_TABLE))
			self.DATA_LIST = []
			
			temp_data_list = self.DB_MANAGER.query_sort(id_list, self.SORT_ITEMS_CONVERTED, self.SORT_MODE,
			                                            self.MAPPER_TABLE_CLASS, self.ID_TABLE)
			
			for i in temp_data_list:
				self.DATA_LIST.append(i)
			self.BROWSE_STATUS = "b"
			self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
			if type(self.REC_CORR) == "<type 'str'>":
				corr = 0
			else:
				corr = self.REC_CORR
			
			self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), 0
			self.DATA_LIST_REC_TEMP = self.DATA_LIST_REC_CORR = self.DATA_LIST[0]
			self.SORT_STATUS = "o"
			self.label_sort.setText(self.SORTED_ITEMS[self.SORT_STATUS])
			self.set_rec_counter(len(self.DATA_LIST), self.REC_CORR + 1)
			self.fill_fields()
		
		##	def on_toolButtonPreviewMedia_toggled(self):
		##		if self.toolButtonPreviewMedia.isChecked() == True:
		##			QMessageBox.warning(self, "Messaggio", "Modalita' Preview Media Reperti attivata. Le immagini dei Reperti saranno visualizzate nella sezione Media", QMessageBox.Ok)
		##			self.loadMediaPreview()
		##		else:
		##			self.loadMediaPreview(1)
	
	def on_pushButton_new_rec_pressed(self):
		if bool(self.DATA_LIST) == True:
			if self.data_error_check() == 1:
				pass
			else:
				if self.BROWSE_STATUS == "b":
					if bool(self.DATA_LIST) == True:
						if self.records_equal_check() == 1:
							msg = self.update_if(QMessageBox.warning(self, 'Errore',
							                                         "Il record e' stato modificato. Vuoi salvare le modifiche?",
							                                         QMessageBox.Cancel, 1))
		
		if self.BROWSE_STATUS != "n":
			self.BROWSE_STATUS = "n"
			self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
			self.empty_fields()
			
			self.setComboBoxEditable(['self.comboBox_sito'], 0)
			self.setComboBoxEnable(['self.comboBox_sito'], 'True')
			self.setComboBoxEnable(['self.lineEdit_griglia'], 'True')
			
			self.label_sort.setText(self.SORTED_ITEMS[self.SORT_STATUS])
			
			self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
			self.set_rec_counter('', '')
			self.label_sort.setText(self.SORTED_ITEMS["n"])
			self.empty_fields()
			
			self.enable_button(0)
	
	def on_pushButton_save_pressed(self):
		# save record
		if self.BROWSE_STATUS == "b":
			if self.data_error_check() == 0:
				if self.records_equal_check() == 1:
					self.update_if(QMessageBox.warning(self, 'ATTENZIONE',
					                                   "Il record e' stato modificato. Vuoi salvare le modifiche?",
					                                   QMessageBox.Cancel, 1))
					self.SORT_STATUS = "n"
					self.label_sort.setText(self.SORTED_ITEMS[self.SORT_STATUS])
					self.enable_button(1)
					self.fill_fields(self.REC_CORR)
				else:
					QMessageBox.warning(self, "ATTENZIONE", "Non e' stata realizzata alcuna modifica.", QMessageBox.Ok)
		else:
			if self.data_error_check() == 0:
				test_insert = self.insert_new_rec()
				if test_insert == 1:
					self.empty_fields()
					self.SORT_STATUS = "n"
					self.label_sort.setText(self.SORTED_ITEMS[self.SORT_STATUS])
					self.charge_records()
					self.charge_list()
					self.BROWSE_STATUS = "b"
					self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
					self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), len(self.DATA_LIST) - 1
					self.set_rec_counter(self.REC_TOT, self.REC_CORR + 1)
					
					self.setComboBoxEditable(['self.comboBox_sito'], 1)
					self.setComboBoxEnable(['self.comboBox_sito'], 'False')
					self.setComboBoxEnable(['self.lineEdit_griglia'], 'False')
					
					self.fill_fields(self.REC_CORR)
					self.enable_button(1)
	
	def generate_list_pdf(self):
		data_list = []
		for i in range(len(self.DATA_LIST)):
			data_list.append({str(self.DATA_LIST[i].id_grid),  # 0 - id_invlap
			                  unicode(self.DATA_LIST[i].sito),  # 1- sito
			                  unicode(self.DATA_LIST[i].progetto),  # 2- progetto
			                  unicode(self.DATA_LIST[i].metodo),  # 3 - metodo
			                  unicode(self.DATA_LIST[i].anno),  # 4 - anno
			                  unicode(self.DATA_LIST[i].settore),  # 5 - settore
			                  unicode(self.DATA_LIST[i].area),  # 6 - area
			                  unicode(self.DATA_LIST[i].griglia),  # 7 - griglia
			                  unicode(self.DATA_LIST[i].pdc),  # 8 - pdc
			                  unicode(self.DATA_LIST[i].quota),  # 9 - quota
			                  unicode(self.DATA_LIST[i].descrizione),  # 10 - descrizione
			                  unicode(self.DATA_LIST[i].interpretazione),  # 11 - interpretazione
			                  unicode(self.DATA_LIST[i].schedatore),  # 12 - schedatore
			                  unicode(self.DATA_LIST[i].data_schedatura),  # 13 - data_schedatura
			                  unicode(self.DATA_LIST[i].modello),  # 14 - modello
			                  unicode(self.DATA_LIST[i].velocita),  # 15 - velocita
			                  unicode(self.DATA_LIST[i].x),  # 16 - x
			                  unicode(self.DATA_LIST[i].x),  # 17 - y
			                  #unicode(self.DATA_LIST[i].date),  # 18 - date
			                  unicode(self.DATA_LIST[i].frequenza),  # 19 - frequenza
			                  unicode(self.DATA_LIST[i].risoluzione),  # 20- risoluzione
			                  unicode(self.DATA_LIST[i].max_prof),  # 21 - massima profondità
			                  unicode(self.DATA_LIST[i].range),  # 22 - range
			                  unicode(self.DATA_LIST[i].bibliografia),  #23
			                  })
		return data_list
	
	"""
    def on_pushButton_exp_pdf_sheet_pressed(self):
        if self.records_equal_check() == 1:
            self.update_if(
                QMessageBox.warning(self, 'Errore', u"Il record e' stato modificato. Vuoi salvare le modifiche?",
                                    QMessageBox.Cancel, 1))

        Geophysics_pdf_sheet = generate_geophysics_pdf()
        data_list = self.generate_list_pdf()
        Geophysics_pdf_sheet.build_Geophysics_sheets(data_list)
    """
	
	# ********************************************************************************
	##			###cerca le singole area/us presenti in quella cassa
	##			res_tip_reperto = self.DB_MANAGER.query_distinct('INVENTARIO_MATERIALI',[['sito','"Sito archeologico"'], ['nr_cassa',cassa]], ['tipo_reperto'])
	##
	##			tip_rep_res_list = ""
	##			for i in res_tip_reperto:
	##				tip_rep_res_list += str(i.tipo_reperto) +"<br/>"
	##
	##			#inserisce l'elenco degli inventari
	##			single_cassa.append(tip_rep_res_list)
	##
	##		#QMessageBox.warning(self,'tk',str(data_for_pdf), QMessageBox.Ok)
	##		return data_for_pdf vediamo che succede
	
	####################################################
	# ********************************************************************************
	
	def data_error_check(self):
		test = 0
		EC = Error_check()
		
		nr_griglia = self.lineEdit_griglia.text()
		#		d_letto_posa = self.lineEdit_d_letto_posa.text()
		#		d_letto_attesa = self.lineEdit_d_letto_attesa.text()
		#		toro = self.lineEdit_toro.text()
		#		spessore = self.lineEdit_spessore.text()
		#		larghezza = self.lineEdit_larghezza.text()
		#		lunghezza = self.lineEdit_lunghezza.text()
		#		h = self.lineEdit_h.text()
		
		
		
		if EC.data_is_empty(unicode(self.comboBox_sito.currentText())) == 0:
			QMessageBox.warning(self, "ATTENZIONE", "Campo Sito. \n Il campo non deve essere vuoto", QMessageBox.Ok)
			test = 1
		
		if EC.data_is_empty(unicode(self.lineEdit_griglia.text())) == 0:
			QMessageBox.warning(self, "ATTENZIONE", "Campo Griglia. \n Il campo non deve essere vuoto", QMessageBox.Ok)
			test = 1
		
		if EC.data_is_empty(unicode(self.lineEdit_progetto.text())) == 0:
			QMessageBox.warning(self, "ATTENZIONE", "Campo Progetto. \n Il campo non deve essere vuoto", QMessageBox.Ok)
			test = 1
		
		if EC.data_is_empty(unicode(self.lineEdit_settore.text())) == 0:
			QMessageBox.warning(self, "ATTENZIONE", "Campo Settore. \n Il campo non deve essere vuoto", QMessageBox.Ok)
			test = 1
		
		if EC.data_is_empty(unicode(self.comboBox_area.currentText())) == 0:
			QMessageBox.warning(self, "ATTENZIONE", "Campo Area. \n Il campo non deve essere vuoto", QMessageBox.Ok)
			test = 1
		
		return test
	
	# insert new row into tableWidget
	# bibliografia
	def on_pushButton_insert_row_bibliografia_pressed(self):
		self.insert_new_row('self.tableWidget_bibliografia')
	
	def on_pushButton_remove_row_bibliografia_pressed(self):
		self.remove_row('self.tableWidget_bibliografia')
	
	def check_record_state(self):
		ec = self.data_error_check()
		if ec == 1:
			return 1  # ci sono errori di immissione
		elif self.records_equal_check() == 1 and ec == 0:
			self.update_if(
				QMessageBox.warning(self, 'Errore', "Il record e' stato modificato. Vuoi salvare le modifiche?",
				                    QMessageBox.Cancel, 1))
			# self.charge_records() incasina lo stato trova
			return 0  # non ci sono errori di immissione
	
	def on_pushButton_view_all_2_pressed(self):
		if self.check_record_state() == 1:
			pass
		else:
			self.empty_fields()
			self.charge_records()
			self.fill_fields()
			self.BROWSE_STATUS = "b"
			self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
			if type(self.REC_CORR) == "<type 'str'>":
				corr = 0
			else:
				corr = self.REC_CORR
			self.set_rec_counter(len(self.DATA_LIST), self.REC_CORR + 1)
			self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), 0
			self.DATA_LIST_REC_TEMP = self.DATA_LIST_REC_CORR = self.DATA_LIST[0]
			self.label_sort.setText(self.SORTED_ITEMS["n"])
		##			if self.toolButtonPreviewMedia.isChecked() == True:
		##				self.loadMediaPreview(1)
	
	# records surf functions
	def on_pushButton_first_rec_pressed(self):
		if self.check_record_state() == 1:
			##			if self.toolButtonPreviewMedia.isChecked() == True:
			self.loadMediaPreview(1)
		else:
			try:
				self.empty_fields()
				self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), 0
				self.fill_fields(0)
				self.set_rec_counter(self.REC_TOT, self.REC_CORR + 1)
			except Exception, e:
				QMessageBox.warning(self, "Errore", str(e), QMessageBox.Ok)
			##				if self.toolButtonPreviewMedia.isChecked() == True:
			##					self.loadMediaPreview(0)
			# se si decidesse di aggiungere if self toolButtonPreviewMedia si metterà prima di except
	
	def on_pushButton_last_rec_pressed(self):
		if self.check_record_state() == 1:
			##			if self.toolButtonPreviewMedia.isChecked() == True:
			self.loadMediaPreview(0)
		else:
			
			try:
				self.empty_fields()
				self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), len(self.DATA_LIST) - 1
				self.fill_fields(self.REC_CORR)
				self.set_rec_counter(self.REC_TOT, self.REC_CORR + 1)
			except Exception, e:
				QMessageBox.warning(self, "Errore", str(e), QMessageBox.Ok)
			##				if self.toolButtonPreviewMedia.isChecked() == True:
			##					self.loadMediaPreview(0)
	
	def on_pushButton_prev_rec_pressed(self):
		if self.check_record_state() == 1:
			pass
		else:
			self.REC_CORR = self.REC_CORR - 1
			if self.REC_CORR == -1:
				self.REC_CORR = 0
				QMessageBox.warning(self, "Errore", "Sei al primo record!", QMessageBox.Ok)
			else:
				try:
					self.empty_fields()
					self.fill_fields(self.REC_CORR)
					self.set_rec_counter(self.REC_TOT, self.REC_CORR + 1)
				except Exception, e:
					QMessageBox.warning(self, "Errore", str(e), QMessageBox.Ok)
				##					if self.toolButtonPreviewMedia.isChecked() == True:
				##						self.loadMediaPreview(0)
	
	def on_pushButton_next_rec_pressed(self):
		if self.check_record_state() == 1:
			pass
		else:
			self.REC_CORR = self.REC_CORR + 1
			if self.REC_CORR >= self.REC_TOT:
				self.REC_CORR = self.REC_CORR - 1
				QMessageBox.warning(self, "Errore", "Sei all'ultimo record!", QMessageBox.Ok)
			else:
				try:
					self.empty_fields()
					self.fill_fields(self.REC_CORR)
					self.set_rec_counter(self.REC_TOT, self.REC_CORR + 1)
				except Exception, e:
					QMessageBox.warning(self, "Errore", str(e), QMessageBox.Ok)
				##					if self.toolButtonPreviewMedia.isChecked() == True:
				##						self.loadMediaPreview(0)
	
	def on_pushButton_delete_pressed(self):
		msg = QMessageBox.warning(self, "Attenzione!!!",
		                          u"Vuoi veramente eliminare il record? \n L'azione e' irreversibile",
		                          QMessageBox.Cancel, 1)
		if msg != 1:
			QMessageBox.warning(self, "Messagio!!!", "Azione Annullata!")
		else:
			try:
				id_to_delete = eval("self.DATA_LIST[self.REC_CORR]." + self.ID_TABLE)
				self.DB_MANAGER.delete_one_record(self.TABLE_NAME, self.ID_TABLE, id_to_delete)
				self.charge_records()  # charge records from DB
				QMessageBox.warning(self, "Messaggio!!!", "Record eliminato!")
			except Exception, e:
				QMessageBox.warning(self, "Messaggio!!!", "Tipo di errore: " + str(e))
			if bool(self.DATA_LIST) == False:
				QMessageBox.warning(self, "Attenzione", u"Il database e' vuoto!", QMessageBox.Ok)
				self.DATA_LIST = []
				self.DATA_LIST_REC_CORR = []
				self.DATA_LIST_REC_TEMP = []
				self.REC_CORR = 0
				self.REC_TOT = 0
				self.empty_fields()
				self.set_rec_counter(0, 0)
			# check if DB is empty
			if bool(self.DATA_LIST) == True:
				self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), 0
				self.DATA_LIST_REC_TEMP = self.DATA_LIST_REC_CORR = self.DATA_LIST[0]
				
				self.BROWSE_STATUS = "b"
				self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
				self.set_rec_counter(len(self.DATA_LIST), self.REC_CORR + 1)
				self.charge_list()
				self.fill_fields()
		self.SORT_STATUS = "n"
		self.label_sort.setText(self.SORTED_ITEMS[self.SORT_STATUS])
	
	def on_pushButton_new_search_pressed(self):
		if self.check_record_state() == 1:
			pass
		else:
			self.enable_button_search(0)
			
			# set the GUI for a new search
			
			
			if self.BROWSE_STATUS != "f":
				self.BROWSE_STATUS = "f"
				###
				self.setComboBoxEditable(['self.comboBox_sito'], 1)
				self.setComboBoxEnable(['self.comboBox_sito'], 'True')
				self.setLineEditEnable(['self.lineEdit_griglia'], 'True')
				self.setTextEditEnable(["self.textEdit_descrizione"], "False")
				self.setTableEnable(["self.tableWidget_bibliografia"], "False")
				###
				self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
				self.set_rec_counter('', '')
				self.label_sort.setText(self.SORTED_ITEMS["n"])
				self.charge_list()
				self.empty_fields()
	
	def on_pushButton_search_go_pressed(self):
		check_for_buttons = 0
		if self.BROWSE_STATUS != "f":
			QMessageBox.warning(self, "ATTENZIONE", "Per eseguire una nuova ricerca clicca sul pulsante 'new search' ",
			                    QMessageBox.Ok)
		else:
			##
			if self.lineEdit_quota.text() != "":
				quota = int(self.lineEdit_quota.text())
			else:
				quota = ""
				
			if self.lineEdit_pdc.text() != "":
				pdc = int(self.lineEdit_pdc.text())
			else:
				pdc = ""
			
			if self.lineEdit_x.text() != "":
				x = int(self.lineEdit_x.text())
			else:
				x = ""
			
			if self.lineEdit_y.text() != "":
				y = int(self.lineEdit_y.text())
			else:
				y = ""
			
			if self.lineEdit_risoluzione.text() != "":
				risoluzione = int(self.lineEdit_risoluzione.text())
			else:
				risoluzione = ""
			
			search_dict = {self.TABLE_FIELDS[0]: "'" + unicode(self.comboBox_sito.currentText()) + "'",
			               self.TABLE_FIELDS[1]: "'" + unicode(self.lineEdit_progetto.text()) + "'",
			               self.TABLE_FIELDS[2]: "'" + unicode(self.comboBox_metodo.currenttext()) + "'",
			               self.TABLE_FIELDS[3]: "'" + unicode(self.lineEdit_anno.text()) + "'",
			               self.TABLE_FIELDS[4]: "'" + unicode(self.lineEdit_settore.text()) + "'",
			               self.TABLE_FIELDS[5]: "'" + unicode(self.comboBox_area.currentText()) + "'",
			               self.TABLE_FIELDS[6]: "'" + unicode(self.lineEdit_griglia.text()) + "'",
			               self.TABLE_FIELDS[7]: pdc,
			               self.TABLE_FIELDS[8]: quota,
			               self.TABLE_FIELDS[9]: "'" + unicode(self.textEdit_descrizione.toPlainText()) + "'",
			               self.TABLE_FIELDS[10]: "'" + unicode(self.textEdit_interpretazione.toPlainText()) + "'",
			               self.TABLE_FIELDS[11]: "'" + unicode(self.comboBox_schedatore.currentText()) + "'",
			               self.TABLE_FIELDS[12]: "'" + unicode(self.lineEdit_data_schedatura.text()) + "'",
			               self.TABLE_FIELDS[13]: "'" + unicode(self.comboBox_modello.text()) + "'",
			               self.TABLE_FIELDS[14]: "'" + unicode(self.comboBox_velocita.text()) + "'",
			               self.TABLE_FIELDS[15]: x,
			               self.TABLE_FIELDS[16]: y,
			               self.TABLE_FIELDS[17]: "'" + unicode(self.lineEdit_data.text()) + "'",
			               self.TABLE_FIELDS[18]: "'" + unicode(self.comboBox_frequenza.text()) + "'",
			               self.TABLE_FIELDS[19]: risoluzione,
			               self.TABLE_FIELDS[20]: "'" + unicode(self.lineEdit_max_prof.text()) + "'",
			               self.TABLE_FIELDS[21]: "'" + unicode(self.lineEdit_range.currentText()) + "'",
			               }
			
			u = Utility()
			search_dict = u.remove_empty_items_fr_dict(search_dict)
			
			if bool(search_dict) == False:
				QMessageBox.warning(self, "ATTENZIONE", "Non e' stata impostata alcuna ricerca!!!", QMessageBox.Ok)
			
			else:
				self.SEARCH_DICT_TEMP = search_dict
				res = self.DB_MANAGER.query_bool(search_dict, self.MAPPER_TABLE_CLASS)
				if bool(res) == False:
					QMessageBox.warning(self, "ATTENZIONE", "Non e' stato trovato alcun record!", QMessageBox.Ok)
					
					self.set_rec_counter(len(self.DATA_LIST), self.REC_CORR + 1)
					self.DATA_LIST_REC_TEMP = self.DATA_LIST_REC_CORR = self.DATA_LIST[0]
					
					self.fill_fields(self.REC_CORR)
					
					self.BROWSE_STATUS = "b"
					self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
					
					self.setComboBoxEditable(["self.comboBox_sito"], 1)
					self.setComboBoxEnable(["self.comboBox_sito"], "False")
					self.setlineEditEnable(["self.lineEdit_griglia"], "False")
					self.settextEditEnable(["self.textEdit_descrizione"], "True")
					self.setTableEnable(["self.tableWidget_bibliografia"], "True")
					check_for_buttons = 1
				
				else:
					
					self.DATA_LIST = []
					
					for i in res:
						self.DATA_LIST.append(i)
					
					self.REC_TOT, self.REC_CORR = len(self.DATA_LIST), 0
					self.DATA_LIST_REC_TEMP = self.DATA_LIST_REC_CORR = self.DATA_LIST[0]
					
					self.fill_fields()
					
					self.BROWSE_STATUS = "b"
					self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
					self.set_rec_counter(len(self.DATA_LIST), self.REC_CORR + 1)
					
					if self.REC_TOT == 1:
						strings = ("E' stato trovato", self.REC_TOT, "record")
					else:
						strings = ("Sono stati trovati", self.REC_TOT, "records")
					
					self.setComboBoxEditable(["self.comboBox_sito"], 1)
					self.setComboBoxEnable(['self.comboBox_sito'], "False")
					self.setlineEditEnable(['self.lineEdit_griglia'], "False")
					self.setTableEnable(["self.tableWidget_descrizione"], "True")  #
					self.setTableEnable(["self.tableWidget_bibliografia"], "True")
					check_for_buttons = 1
					
					QMessageBox.warning(self, "Messaggio", "%s %d %s" % strings, QMessageBox.Ok)
		
		if check_for_buttons == 1:
			self.enable_button_search(1)
	
	def update_if(self, msg):
		rec_corr = self.REC_CORR
		self.msg = msg
		if self.msg == 1:
			test = self.update_record()
			if test == 1:
				id_list = []
				for i in self.DATA_LIST:
					id_list.append(eval("i." + self.ID_TABLE))
				self.DATA_LIST = []
				if self.SORT_STATUS == "n":
					temp_data_list = self.DB_MANAGER.query_sort(id_list, [self.ID_TABLE], 'asc',
					                                            self.MAPPER_TABLE_CLASS,
					                                            self.ID_TABLE)  # self.DB_MANAGER.query_bool(self.SEARCH_DICT_TEMP, self.MAPPER_TABLE_CLASS) #
				else:
					temp_data_list = self.DB_MANAGER.query_sort(id_list, self.SORT_ITEMS_CONVERTED, self.SORT_MODE,
					                                            self.MAPPER_TABLE_CLASS, self.ID_TABLE)
				for i in temp_data_list:
					self.DATA_LIST.append(i)
				self.BROWSE_STATUS = "b"
				self.label_status.setText(self.STATUS_ITEMS[self.BROWSE_STATUS])
				if type(self.REC_CORR) == "<type 'str'>":
					corr = 0
				else:
					corr = self.REC_CORR
				return 1
			elif test == 0:
				return 0
	
	def update_record(self):
		try:
			self.DB_MANAGER.update(self.MAPPER_TABLE_CLASS, self.ID_TABLE,
			                       [eval("int(self.DATA_LIST[self.REC_CORR]." + self.ID_TABLE + ")")],
			                       self.TABLE_FIELDS, self.rec_toupdate())
			return 1
		except Exception, e:
			QMessageBox.warning(self, "Messaggio",
			                    "Problema di encoding: sono stati inseriti accenti o caratteri non accettati dal database. Se chiudete ora la scheda senza correggere gli errori perderete i dati. Fare una copia di tutto su un foglio word a parte. Errore :" + str(
				                    e), QMessageBox.Ok)
			return 0
	
	def rec_toupdate(self):
		rec_to_update = self.UTILITY.pos_none_in_list(self.DATA_LIST_REC_TEMP)
		# rec_to_update = rec_to_update[:2]
		return rec_to_update
	
	# custom functions
	######old system
	##	def charge_records(self):
	##		self.DATA_LIST = []
	##		id_list = []
	##		for i in self.DB_MANAGER.query(eval(self.MAPPER_TABLE_CLASS)):
	##			id_list.append(eval("i."+ self.ID_TABLE))
	##
	##		temp_data_list = self.DB_MANAGER.query_sort(id_list, [self.ID_TABLE], 'asc', self.MAPPER_TABLE_CLASS, self.ID_TABLE)
	##		for i in temp_data_list:
	##			self.DATA_LIST.append(i)
	
	
	def charge_records(self):
		self.DATA_LIST = []
		
		if self.DB_SERVER == 'sqlite':
			for i in self.DB_MANAGER.query(eval(self.MAPPER_TABLE_CLASS)):
				self.DATA_LIST.append(i)
		else:
			id_list = []
			for i in self.DB_MANAGER.query(eval(self.MAPPER_TABLE_CLASS)):
				id_list.append(eval("i." + self.ID_TABLE))
			
			temp_data_list = self.DB_MANAGER.query_sort(id_list, [self.ID_TABLE], 'asc', self.MAPPER_TABLE_CLASS,
			                                            self.ID_TABLE)
			for i in temp_data_list:
				self.DATA_LIST.append(i)
	
	def setComboBoxEditable(self, f, n):
		field_names = f
		value = n
		
		for fn in field_names:
			cmd = ('%s%s%d%s') % (fn, '.setEditable(', n, ')')
			eval(cmd)
	
	def setComboBoxEnable(self, f, v):
		field_names = f
		value = v
		
		for fn in field_names:
			cmd = ('%s%s%s%s') % (fn, '.setEnabled(', v, ')')
			eval(cmd)
	
	def datestrfdate(self):
		now = date.today()
		today = now.strftime("%d-%m-%Y")
		return today
	
	def table2dict(self, n):
		self.tablename = n
		row = eval(self.tablename + ".rowCount()")
		col = eval(self.tablename + ".columnCount()")
		lista = []
		for r in range(row):
			sub_list = []
			for c in range(col):
				value = eval(self.tablename + ".item(r,c)")
				if value != None:
					sub_list.append(unicode(value.text()))
			
			if bool(sub_list) == True:
				lista.append(sub_list)
		
		return lista
	
	def tableInsertData(self, t, d):
		"""Set the value into alls Grid"""
		self.table_name = t
		self.data_list = eval(d)
		self.data_list.sort()
		
		# column table count
		table_col_count_cmd = ("%s.columnCount()") % (self.table_name)
		table_col_count = eval(table_col_count_cmd)
		
		# clear table
		table_clear_cmd = ("%s.clearContents()") % (self.table_name)
		eval(table_clear_cmd)
		
		for i in range(table_col_count):
			table_rem_row_cmd = ("%s.removeRow(%d)") % (self.table_name, i)
			eval(table_rem_row_cmd)
		
		# for i in range(len(self.data_list)):
		# self.insert_new_row(self.table_name)
		
		for row in range(len(self.data_list)):
			cmd = ('%s.insertRow(%s)') % (self.table_name, row)
			eval(cmd)
			for col in range(len(self.data_list[row])):
				# item = self.comboBox_sito.setEditText(self.data_list[0][col]
				item = QTableWidgetItem(unicode(self.data_list[row][col]))
				exec_str = ('%s.setItem(%d,%d,item)') % (self.table_name, row, col)
				eval(exec_str)
	
	def insert_new_row(self, table_name):
		"""insert new row into a table based on table_name"""
		cmd = table_name + ".insertRow(0)"
		eval(cmd)
	
	def remove_row(self, table_name):
		"""insert new row into a table based on table_name"""
		
		table_row_count_cmd = ("%s.rowCount()") % (table_name)
		table_row_count = eval(table_row_count_cmd)
		rowSelected_cmd = ("%s.selectedIndexes()") % (table_name)
		rowSelected = eval(rowSelected_cmd)
		try:
			rowIndex = (rowSelected[1].row())
			cmd = ("%s.removeRow(%d)") % (table_name, rowIndex)
			eval(cmd)
		except:
			QMessageBox.warning(self, "Messaggio", "Devi selezionare una riga", QMessageBox.Ok)
	
	def empty_fields(self):
		bibliografia_row_count = self.tableWidget_bibliografia.rowCount()
		
		self.comboBox_sito.setEditText("")  # 1 - Sito
		self.lineEdit_progetto.clear()  # 2 - progetto
		self.comboBox_metodo.setEditText("")  # 3 - metodo
		self.lineEdit_anno.clear()  # 4 - anno
		self.lineEdit_settore.clear()  # 5 - settore
		self.comboBox_area.setEditText("")  # 6 - area
		self.lineEdit_griglia.clear()  # 7 - griglia
		self.lineEdit_pdc.clear()  # 8 - piano di campagna
		self.lineEdit_quota.clear()  # 9 - quota assoluta
		self.textEdit_descrizione.clear()  # 10 - descrizione
		self.textEdit_interpretazione.clear()  # 11 - interpretazione
		self.comboBox_schedatore.setEditText("")  # 12 - schedatore
		self.lineEdit_data_schedatura.clear()  # 13 - data schedatura
		self.comboBox_modello.setEditText("")  # 14 - modello GPR
		self.comboBox_velocita.setEditText("")  # 15 - velocita'
		self.lineEdit_date.setText ("")  # 16 - data del progetto
		self.comboBox_frequenza.setEditText("")  # 17 - frequenza antenna
		self.lineEdit_risoluzione.clear()  # 18 - risoluzione
		self.lineEdit_max_prof.clear()  # 19 - massima profondita'
		self.lineEdit_range.clear()  # 20 - range
		self.lineEdit_x.clear()  # 21 - asse delle x
		self.lineEdit_y.clear()  # 22 - asse delle y
		
		for i in range(bibliografia_row_count):
			self.tableWidget_bibliografia.removeRow(0)
		self.insert_new_row("self.tableWidget_bibliografia")  # 19- bibliografia
	
	def fill_fields(self, n=0):
		self.rec_num = n
		# QMessageBox.warning(self, "check fill fields", str(self.rec_num),  QMessageBox.Ok)
		try:
			unicode(self.comboBox_sito.setEditText(self.DATA_LIST[self.rec_num].sito))  # 1 - Sito
			self.lineEdit_progetto.setText(str(self.DATA_LIST[self.rec_num].progetto))  # 2 - progetto
			unicode(self.comboBox_metodo.setEditText(self.DATA_LIST[self.rec_num].metodo))  # 3 - metodo
			self.lineEdit_anno.setText(str(self.DATA_LIST[self.rec_num].anno))  # 4 - anno
			self.lineEdit_settore.setText(str(self.DATA_LIST[self.rec_num].settore))  # 5 - settore
			unicode(self.comboBox_area.setEditText(self.DATA_LIST[self.rec_num].area))  # 6 - area
			self.lineEdit_griglia.setText(str(self.DATA_LIST[self.rec_num].griglia))  # 7 - griglia
			self.lineEdit_pdc.setText(str(self.DATA_LIST[self.rec_num].pdc))  # 8 - piano di campagna
			self.lineEdit_quota.setText(str(self.DATA_LIST[self.rec_num].quota))  # 9 - quota assoluta
			unicode(self.textEdit_descrizione.setText(self.DATA_LIST[self.rec_num].descrizione))  # 10 - descrizione
			unicode(self.textEdit_interpretazione.setText(self.DATA_LIST[self.rec_num].interpretazione))  # 11 - interpretazione
			unicode(self.comboBox_schedatore.setEditText(self.DATA_LIST[self.rec_num].schedatore))  # 12 - schedatore
			self.lineEdit_data_schedatura.setText(str(self.DATA_LIST[self.rec_num].data_schedatura))  # 13 - data schedatura
			unicode(self.comboBox_modello.setEditText(self.DATA_LIST[self.rec_num].modello))  # 14 - modello
			unicode(self.comboBox_velocita.setEditText(self.DATA_LIST[self.rec_num].velocita))  # 15 - velocita'
			self.lineEdit_x.setText(str(self.DATA_LIST[self.rec_num].x))  # 16 - asse delle x
			self.lineEdit_y.setText(str(self.DATA_LIST[self.rec_num].y)) # 17 - asse delle y
			unicode(self.lineEdit_date.setText(self.DATA_LIST[self.rec_num].date))  # 18 - data progetto
			self.lineEdit_risoluzione.setText(str(self.DATA_LIST[self.rec_num].risoluzione))  # 19 - risoluzione
			unicode(self.comboBox_frequenza.setEditText(self.DATA_LIST[self.rec_num].frequenza))  # 20 - frequenza
			self.lineEdit_max_prof.setText(str(self.DATA_LIST[self.rec_num].max_prof))  # 21 - massima profondità
			self.lineEdit_range.setText(str(self.DATA_LIST[self.rec_num].range))  # 22 - range
			self.tableInsertData("self.tableWidget_bibliografia",self.DATA_LIST[self.rec_num].bibliografia)  # 23 - bibliografia
			
			if self.DATA_LIST[self.rec_num].x == None:  # 9 - d_letto_posa
				self.lineEdit_x.setText("")
			else:
				self.lineEdit_x.setText(str(self.DATA_LIST[self.rec_num].x))
			
			if self.DATA_LIST[self.rec_num].y == None:  # 10 - d_letto_attesa
				self.lineEdit_y.setText("")
			else:
				self.lineEdit_y.setText(str(self.DATA_LIST[self.rec_num].y))
			
			
			#########
		except Exception, e:
			QMessageBox.warning(self, "Errore Fill Fields", str(e), QMessageBox.Ok)
	
	def set_rec_counter(self, t, c):
		self.rec_tot = t
		self.rec_corr = c
		self.label_rec_tot.setText(str(self.rec_tot))
		self.label_rec_corrente.setText(str(self.rec_corr))
	
	def set_LIST_REC_TEMP(self):
		# TableWidget
		
		# bibliografia
		bibliografia = self.table2dict("self.tableWidget_bibliografia")
		
		# data
		self.DATA_LIST_REC_TEMP = {unicode(self.comboBox_sito.currentText()),  # 1 - Sito
		                           unicode(self.lineEdit_progetto.text()),  # 2 - progetto
		                           unicode(self.comboBox_metodo.currentText()),  # 3 - metodo
		                           unicode(self.lineEdit_anno.text()),  # 4 - anno
		                           unicode(self.lineEdit_settore.text()),  # 5 - settore
		                           unicode(self.comboBox_area.currentText()),  # 6 - area
		                           unicode(self.lineEdit_griglia.text()),  # 7 - griglia
		                           unicode(self.lineEdit_pdc.text()),  # 8 - pdc
		                           unicode(self.lineEdit_quota.text()),  # 9 - quota
		                           unicode(self.textEdit_descrizione.toPlainText()),  # 10 - descrizione
		                           unicode(self.textEdit_interpretazione.toPlainText()),  # 11 - interpretazione
		                           unicode(self.comboBox_schedatore.currentText()),  # 12 - schedatore
		                           unicode(self.lineEdit_data_schedatura.text()),  # 13 - data schedatura
		                           unicode(self.comboBox_modello.currentText()),  # 14 - modello
		                           unicode(self.comboBox_velocita.currentText()),  # 15 - velocita
		                           unicode(self.lineEdit_x.text()),  # 16 - x
		                           unicode(self.lineEdit_y.text()),  # 17 - y
		                           unicode(self.lineEdit_date.text()),  # 18 - date
		                           unicode(self.comboBox_frequenza.currentText()),  # 19 - frequenza
		                           unicode(self.lineEdit_risoluzione.text()),  # 20 - risoluzione
		                           unicode(self.lineEdit_max_prof.text()),  # 21 - massima profondità
		                           unicode(self.lineEdit_range.text()),  # 22 - range
		                           str(bibliografia),
		                           }
	
	def setTableEnable(self, t, v):
		tab_names = t
		value = v
		
		for tn in tab_names:
			cmd = ('%s%s%s%s') % (tn, '.setEnabled(', v, ')')
			eval(cmd)
	
	def set_LIST_REC_CORR(self):
		self.DATA_LIST_REC_CORR = []
		for i in self.TABLE_FIELDS:
			self.DATA_LIST_REC_CORR.append(eval("unicode(self.DATA_LIST[self.REC_CORR]." + i + ")"))
	
	def records_equal_check(self):
		self.set_LIST_REC_TEMP()
		self.set_LIST_REC_CORR()
		
		# test
		
		# QMessageBox.warning(self, "ATTENZIONE", str(self.DATA_LIST_REC_CORR) + " temp " + str(self.DATA_LIST_REC_TEMP), QMessageBox.Ok)
		
		check_str = str(self.DATA_LIST_REC_CORR) + " " + str(self.DATA_LIST_REC_TEMP)
		
		if self.DATA_LIST_REC_CORR == self.DATA_LIST_REC_TEMP:
			return 0
		else:
			return 1
	
	def testing(self, errore, e):
		f = open(str("\users\giuse\desktop\errore.txt"), 'w')
		f.write(str(e))
		f.close()


if __name__ == "__main__":
	app = QApplication(sys.argv)
	ui = pyarchinit_geophysics_ui()
	ui.show()
	sys.exit(app.exec_())
