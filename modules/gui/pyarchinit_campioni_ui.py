# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_campioni_ui.ui'
#
# Created: Mon Aug 18 16:20:16 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogCampioni(object):
    def setupUi(self, DialogCampioni):
        DialogCampioni.setObjectName(_fromUtf8("DialogCampioni"))
        DialogCampioni.resize(540, 478)
        DialogCampioni.setMinimumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconSite.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogCampioni.setWindowIcon(icon)
        self.gridLayout_7 = QtGui.QGridLayout(DialogCampioni)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_29 = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_42 = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_43 = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setMargin(0)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(DialogCampioni)
        self.label_status.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setText(_fromUtf8(""))
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName(_fromUtf8("label_sort"))
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setMargin(0)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_27 = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setMargin(0)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setObjectName(_fromUtf8("label_rec_corrente"))
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setMargin(0)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(DialogCampioni)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setObjectName(_fromUtf8("label_rec_tot"))
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 0, 1, 3, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_last_rec = QtGui.QPushButton(DialogCampioni)
        self.pushButton_last_rec.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/7_rightArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon1)
        self.pushButton_last_rec.setObjectName(_fromUtf8("pushButton_last_rec"))
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 5, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/newrec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon2)
        self.pushButton_new_rec.setObjectName(_fromUtf8("pushButton_new_rec"))
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 6, 1, 1)
        self.pushButton_save = QtGui.QPushButton(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/b_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon3)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 0, 7, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon4)
        self.pushButton_new_search.setObjectName(_fromUtf8("pushButton_new_search"))
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 4, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon5)
        self.pushButton_search_go.setObjectName(_fromUtf8("pushButton_search_go"))
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 5, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon6)
        self.pushButton_sort.setObjectName(_fromUtf8("pushButton_sort"))
        self.gridLayout.addWidget(self.pushButton_sort, 1, 6, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(DialogCampioni)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon7)
        self.pushButton_view_all.setObjectName(_fromUtf8("pushButton_view_all"))
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 7, 1, 1)
        self.pushButton_next_rec = QtGui.QPushButton(DialogCampioni)
        self.pushButton_next_rec.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/6_rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon8)
        self.pushButton_next_rec.setObjectName(_fromUtf8("pushButton_next_rec"))
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 4, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(DialogCampioni)
        self.pushButton_prev_rec.setMaximumSize(QtCore.QSize(75, 16777215))
        self.pushButton_prev_rec.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/4_leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon9)
        self.pushButton_prev_rec.setObjectName(_fromUtf8("pushButton_prev_rec"))
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 3, 1, 1)
        self.pushButton_first_rec = QtGui.QPushButton(DialogCampioni)
        self.pushButton_first_rec.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/5_leftArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon10)
        self.pushButton_first_rec.setObjectName(_fromUtf8("pushButton_first_rec"))
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 2, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(DialogCampioni)
        self.pushButton_delete.setMaximumSize(QtCore.QSize(75, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon11)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.gridLayout.addWidget(self.pushButton_delete, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(DialogCampioni)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout_2.addWidget(self.pushButton_connect, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 1, 1, 3)
        self.line_8 = QtGui.QFrame(DialogCampioni)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_7.addWidget(self.line_8, 1, 1, 1, 3)
        self.comboBox_sito = QtGui.QComboBox(DialogCampioni)
        self.comboBox_sito.setEnabled(False)
        self.comboBox_sito.setMinimumSize(QtCore.QSize(350, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sito.setFont(font)
        self.comboBox_sito.setMouseTracking(True)
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setMaxVisibleItems(99999)
        self.comboBox_sito.setMaxCount(2147483647)
        self.comboBox_sito.setObjectName(_fromUtf8("comboBox_sito"))
        self.comboBox_sito.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_sito, 2, 1, 1, 1)
        self.lineEdit_nr_campione = QtGui.QLineEdit(DialogCampioni)
        self.lineEdit_nr_campione.setEnabled(False)
        self.lineEdit_nr_campione.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit_nr_campione.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_nr_campione.setObjectName(_fromUtf8("lineEdit_nr_campione"))
        self.gridLayout_7.addWidget(self.lineEdit_nr_campione, 2, 3, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox_tipo_campione = QtGui.QComboBox(DialogCampioni)
        self.comboBox_tipo_campione.setEditable(True)
        self.comboBox_tipo_campione.setObjectName(_fromUtf8("comboBox_tipo_campione"))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.comboBox_tipo_campione.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.comboBox_tipo_campione)
        self.label_2 = QtGui.QLabel(DialogCampioni)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_7.addLayout(self.verticalLayout, 4, 1, 1, 3)
        self.toolBox = QtGui.QToolBox(DialogCampioni)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 522, 146))
        self.page.setObjectName(_fromUtf8("page"))
        self.gridLayout_9 = QtGui.QGridLayout(self.page)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_13 = QtGui.QLabel(self.page)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.verticalLayout_3.addWidget(self.label_13)
        self.textEdit_descrizione_camp = QtGui.QTextEdit(self.page)
        self.textEdit_descrizione_camp.setMinimumSize(QtCore.QSize(0, 20))
        self.textEdit_descrizione_camp.setMaximumSize(QtCore.QSize(16777215, 16000000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_descrizione_camp.setFont(font)
        self.textEdit_descrizione_camp.setObjectName(_fromUtf8("textEdit_descrizione_camp"))
        self.verticalLayout_3.addWidget(self.textEdit_descrizione_camp)
        self.gridLayout_9.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.page)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_9.addWidget(self.label_6, 2, 0, 1, 1)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_4 = QtGui.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 505, 186))
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_4)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_15 = QtGui.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 4)
        self.label_7 = QtGui.QLabel(self.page_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_6.addWidget(self.label_7, 7, 3, 3, 1)
        self.lineEdit_n_inv_mat = QtGui.QLineEdit(self.page_4)
        self.lineEdit_n_inv_mat.setObjectName(_fromUtf8("lineEdit_n_inv_mat"))
        self.gridLayout_6.addWidget(self.lineEdit_n_inv_mat, 7, 4, 3, 1)
        self.line = QtGui.QFrame(self.page_4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_6.addWidget(self.line, 10, 0, 1, 5)
        self.gridLayout_10 = QtGui.QGridLayout()
        self.gridLayout_10.setObjectName(_fromUtf8("gridLayout_10"))
        self.label_14 = QtGui.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)
        self.gridLayout_8 = QtGui.QGridLayout()
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.lineEdit_luogo_conservazione = QtGui.QLineEdit(self.page_4)
        self.lineEdit_luogo_conservazione.setMinimumSize(QtCore.QSize(344, 0))
        self.lineEdit_luogo_conservazione.setObjectName(_fromUtf8("lineEdit_luogo_conservazione"))
        self.gridLayout_8.addWidget(self.lineEdit_luogo_conservazione, 0, 0, 1, 1)
        self.lineEdit_cassa = QtGui.QLineEdit(self.page_4)
        self.lineEdit_cassa.setMinimumSize(QtCore.QSize(61, 0))
        self.lineEdit_cassa.setObjectName(_fromUtf8("lineEdit_cassa"))
        self.gridLayout_8.addWidget(self.lineEdit_cassa, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.page_4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_8.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.page_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_8.addWidget(self.label_12, 1, 1, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_10, 11, 0, 1, 5)
        self.label_4 = QtGui.QLabel(self.page_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.page_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_6.addWidget(self.label_5, 6, 0, 1, 1)
        self.lineEdit_area = QtGui.QLineEdit(self.page_4)
        self.lineEdit_area.setObjectName(_fromUtf8("lineEdit_area"))
        self.gridLayout_6.addWidget(self.lineEdit_area, 2, 2, 1, 1)
        self.lineEdit_us = QtGui.QLineEdit(self.page_4)
        self.lineEdit_us.setObjectName(_fromUtf8("lineEdit_us"))
        self.gridLayout_6.addWidget(self.lineEdit_us, 6, 2, 1, 1)
        self.toolBox.addItem(self.page_4, _fromUtf8(""))
        self.page_3 = QtGui.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 522, 146))
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.formLayout = QtGui.QFormLayout(self.page_3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pushButton_exp_champ_sheet_pdf = QtGui.QPushButton(self.page_3)
        self.pushButton_exp_champ_sheet_pdf.setObjectName(_fromUtf8("pushButton_exp_champ_sheet_pdf"))
        self.horizontalLayout_2.addWidget(self.pushButton_exp_champ_sheet_pdf)
        self.pushButton_index_pdf = QtGui.QPushButton(self.page_3)
        self.pushButton_index_pdf.setEnabled(True)
        self.pushButton_index_pdf.setObjectName(_fromUtf8("pushButton_index_pdf"))
        self.horizontalLayout_2.addWidget(self.pushButton_index_pdf)
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_8 = QtGui.QLabel(self.page_3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_3.addWidget(self.label_8)
        self.pushButton_sites_geometry = QtGui.QPushButton(self.page_3)
        self.pushButton_sites_geometry.setEnabled(False)
        self.pushButton_sites_geometry.setObjectName(_fromUtf8("pushButton_sites_geometry"))
        self.horizontalLayout_3.addWidget(self.pushButton_sites_geometry)
        self.formLayout.setLayout(1, QtGui.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_9 = QtGui.QLabel(self.page_3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_4.addWidget(self.label_9)
        self.pushButton_rel_pdf = QtGui.QPushButton(self.page_3)
        self.pushButton_rel_pdf.setEnabled(False)
        self.pushButton_rel_pdf.setObjectName(_fromUtf8("pushButton_rel_pdf"))
        self.horizontalLayout_4.addWidget(self.pushButton_rel_pdf)
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout_4)
        self.toolBox.addItem(self.page_3, _fromUtf8(""))
        self.gridLayout_7.addWidget(self.toolBox, 5, 1, 1, 3)
        self.label_10 = QtGui.QLabel(DialogCampioni)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_7.addWidget(self.label_10, 2, 2, 1, 1)
        self.label = QtGui.QLabel(DialogCampioni)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 3, 1, 1, 1)

        self.retranslateUi(DialogCampioni)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DialogCampioni)

    def retranslateUi(self, DialogCampioni):
        DialogCampioni.setWindowTitle(QtGui.QApplication.translate("DialogCampioni", "pyArchInit Gestione Scavi - Scheda Campioni", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("DialogCampioni", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("DialogCampioni", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("DialogCampioni", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("DialogCampioni", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("DialogCampioni", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setText(QtGui.QApplication.translate("DialogCampioni", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("DialogCampioni", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setText(QtGui.QApplication.translate("DialogCampioni", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(QtGui.QApplication.translate("DialogCampioni", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(QtGui.QApplication.translate("DialogCampioni", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(QtGui.QApplication.translate("DialogCampioni", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(QtGui.QApplication.translate("DialogCampioni", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(QtGui.QApplication.translate("DialogCampioni", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(QtGui.QApplication.translate("DialogCampioni", "Connection test", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0, QtGui.QApplication.translate("DialogCampioni", "Inserisci un valore", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(0, QtGui.QApplication.translate("DialogCampioni", "Argilla", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(1, QtGui.QApplication.translate("DialogCampioni", "Calce", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(2, QtGui.QApplication.translate("DialogCampioni", "Carbone", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(3, QtGui.QApplication.translate("DialogCampioni", "Cocciopesto", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(4, QtGui.QApplication.translate("DialogCampioni", "Concotto", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(5, QtGui.QApplication.translate("DialogCampioni", "Intonaco", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(6, QtGui.QApplication.translate("DialogCampioni", "Laterizio", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(7, QtGui.QApplication.translate("DialogCampioni", "Legno", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(8, QtGui.QApplication.translate("DialogCampioni", "Minerale", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(9, QtGui.QApplication.translate("DialogCampioni", "Malta", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(10, QtGui.QApplication.translate("DialogCampioni", "Ossa", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(11, QtGui.QApplication.translate("DialogCampioni", "Ossa combuste", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(12, QtGui.QApplication.translate("DialogCampioni", "Pietrisco", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(13, QtGui.QApplication.translate("DialogCampioni", "Scoria", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(14, QtGui.QApplication.translate("DialogCampioni", "Scoria di ceramica", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(15, QtGui.QApplication.translate("DialogCampioni", "Scoria di metallo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(16, QtGui.QApplication.translate("DialogCampioni", "Scoria di vetro", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(17, QtGui.QApplication.translate("DialogCampioni", "Terra", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tipo_campione.setItemText(18, QtGui.QApplication.translate("DialogCampioni", "Terra e carboni", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogCampioni", "Tipo campione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("DialogCampioni", "Dati descrittivi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogCampioni", "Descrizione ", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QtGui.QApplication.translate("DialogCampioni", "Dati descrittivi", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("DialogCampioni", "Riferimenti stratigraific e Inventario Materiali", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogCampioni", "Riferimento Nr. Inventario Materiale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("DialogCampioni", "Riferimenti collocazione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DialogCampioni", "Luogo di conservazione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("DialogCampioni", "Cassa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogCampioni", "Area", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogCampioni", "US", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QtGui.QApplication.translate("DialogCampioni", "Dati stratigrafici e collocazione", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exp_champ_sheet_pdf.setText(QtGui.QApplication.translate("DialogCampioni", "Esporta scheda campioni", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_index_pdf.setText(QtGui.QApplication.translate("DialogCampioni", "Esporta elenco campioni PDF", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setToolTip(QtGui.QApplication.translate("DialogCampioni", "Carica tutti layer che contengono geometrie relative a questo sito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogCampioni", "..", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sites_geometry.setText(QtGui.QApplication.translate("DialogCampioni", "Carica", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DialogCampioni", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_rel_pdf.setText(QtGui.QApplication.translate("DialogCampioni", "Esporta", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QtGui.QApplication.translate("DialogCampioni", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DialogCampioni", "Nr Campione", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogCampioni", "Sito", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
