# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SchedTable.ui'
#
# Created: Wed Jan 23 22:21:55 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ScheduleTable(object):
    def setupUi(self, ScheduleTable):
        ScheduleTable.setObjectName(_fromUtf8("ScheduleTable"))
        ScheduleTable.resize(816, 584)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        ScheduleTable.setFont(font)
        self.trSchedTable = QtGui.QTreeWidget(ScheduleTable)
        self.trSchedTable.setGeometry(QtCore.QRect(20, 10, 371, 561))
        self.trSchedTable.setObjectName(_fromUtf8("trSchedTable"))
        self.tblSchedTable = QtGui.QTabWidget(ScheduleTable)
        self.tblSchedTable.setGeometry(QtCore.QRect(410, 450, 391, 121))
        self.tblSchedTable.setObjectName(_fromUtf8("tblSchedTable"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(14, 31, 361, 27))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.cmbxActTskId = QtGui.QComboBox(self.layoutWidget)
        self.cmbxActTskId.setMinimumSize(QtCore.QSize(200, 0))
        self.cmbxActTskId.setObjectName(_fromUtf8("cmbxActTskId"))
        self.horizontalLayout.addWidget(self.cmbxActTskId)
        self.tblSchedTable.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget1 = QtGui.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(14, 14, 361, 58))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 2)
        self.cmbxSetTskId = QtGui.QComboBox(self.layoutWidget1)
        self.cmbxSetTskId.setMinimumSize(QtCore.QSize(200, 0))
        self.cmbxSetTskId.setObjectName(_fromUtf8("cmbxSetTskId"))
        self.gridLayout_2.addWidget(self.cmbxSetTskId, 0, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.cmbxSetEnt = QtGui.QComboBox(self.layoutWidget1)
        self.cmbxSetEnt.setMinimumSize(QtCore.QSize(150, 0))
        self.cmbxSetEnt.setObjectName(_fromUtf8("cmbxSetEnt"))
        self.gridLayout_2.addWidget(self.cmbxSetEnt, 1, 1, 1, 2)
        self.tblSchedTable.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget2 = QtGui.QWidget(self.tab_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(60, 30, 271, 27))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.spbxSchedEpOffset = QtGui.QSpinBox(self.layoutWidget2)
        self.spbxSchedEpOffset.setMinimumSize(QtCore.QSize(200, 0))
        self.spbxSchedEpOffset.setMaximum(65535)
        self.spbxSchedEpOffset.setObjectName(_fromUtf8("spbxSchedEpOffset"))
        self.horizontalLayout_3.addWidget(self.spbxSchedEpOffset)
        self.tblSchedTable.addTab(self.tab_3, _fromUtf8(""))
        self.layoutWidget3 = QtGui.QWidget(ScheduleTable)
        self.layoutWidget3.setGeometry(QtCore.QRect(410, 20, 183, 95))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.btnAdd = QtGui.QPushButton(self.layoutWidget3)
        self.btnAdd.setMinimumSize(QtCore.QSize(181, 0))
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout.addWidget(self.btnAdd)
        self.btnInsert = QtGui.QPushButton(self.layoutWidget3)
        self.btnInsert.setObjectName(_fromUtf8("btnInsert"))
        self.verticalLayout.addWidget(self.btnInsert)
        self.btnDelete = QtGui.QPushButton(self.layoutWidget3)
        self.btnDelete.setObjectName(_fromUtf8("btnDelete"))
        self.verticalLayout.addWidget(self.btnDelete)
        self.layoutWidget4 = QtGui.QWidget(ScheduleTable)
        self.layoutWidget4.setGeometry(QtCore.QRect(410, 131, 383, 302))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cbxSchedTblRepeatable = QtGui.QCheckBox(self.layoutWidget4)
        self.cbxSchedTblRepeatable.setObjectName(_fromUtf8("cbxSchedTblRepeatable"))
        self.gridLayout.addWidget(self.cbxSchedTblRepeatable, 0, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.layoutWidget4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.cmbxSchedTblDrivingCounter = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxSchedTblDrivingCounter.setMinimumSize(QtCore.QSize(231, 0))
        self.cmbxSchedTblDrivingCounter.setObjectName(_fromUtf8("cmbxSchedTblDrivingCounter"))
        self.gridLayout.addWidget(self.cmbxSchedTblDrivingCounter, 1, 1, 1, 1)
        self.cbxSchedTblAutostartable = QtGui.QCheckBox(self.layoutWidget4)
        self.cbxSchedTblAutostartable.setObjectName(_fromUtf8("cbxSchedTblAutostartable"))
        self.gridLayout.addWidget(self.cbxSchedTblAutostartable, 2, 0, 1, 2)
        self.label_6 = QtGui.QLabel(self.layoutWidget4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.cmbxSchedTblAutoStartType = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxSchedTblAutoStartType.setMinimumSize(QtCore.QSize(231, 0))
        self.cmbxSchedTblAutoStartType.setObjectName(_fromUtf8("cmbxSchedTblAutoStartType"))
        self.cmbxSchedTblAutoStartType.addItem(_fromUtf8(""))
        self.cmbxSchedTblAutoStartType.addItem(_fromUtf8(""))
        self.cmbxSchedTblAutoStartType.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbxSchedTblAutoStartType, 3, 1, 1, 1)
        self.lblSchedTblAbsRel = QtGui.QLabel(self.layoutWidget4)
        self.lblSchedTblAbsRel.setObjectName(_fromUtf8("lblSchedTblAbsRel"))
        self.gridLayout.addWidget(self.lblSchedTblAbsRel, 4, 0, 1, 1)
        self.spbxSchedTblAbsRel = QtGui.QSpinBox(self.layoutWidget4)
        self.spbxSchedTblAbsRel.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblAbsRel.setMaximum(65535)
        self.spbxSchedTblAbsRel.setObjectName(_fromUtf8("spbxSchedTblAbsRel"))
        self.gridLayout.addWidget(self.spbxSchedTblAbsRel, 4, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.layoutWidget4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.spbxSchedTblFinalDelay = QtGui.QSpinBox(self.layoutWidget4)
        self.spbxSchedTblFinalDelay.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblFinalDelay.setMinimum(1)
        self.spbxSchedTblFinalDelay.setMaximum(65535)
        self.spbxSchedTblFinalDelay.setObjectName(_fromUtf8("spbxSchedTblFinalDelay"))
        self.gridLayout.addWidget(self.spbxSchedTblFinalDelay, 5, 1, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 1)
        self.cmbxSchedTblSyncStrategy = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxSchedTblSyncStrategy.setMinimumSize(QtCore.QSize(231, 0))
        self.cmbxSchedTblSyncStrategy.setObjectName(_fromUtf8("cmbxSchedTblSyncStrategy"))
        self.cmbxSchedTblSyncStrategy.addItem(_fromUtf8(""))
        self.cmbxSchedTblSyncStrategy.addItem(_fromUtf8(""))
        self.cmbxSchedTblSyncStrategy.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbxSchedTblSyncStrategy, 6, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget4)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 7, 0, 1, 1)
        self.spbxSchedTblMaxAdvance = QtGui.QSpinBox(self.layoutWidget4)
        self.spbxSchedTblMaxAdvance.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblMaxAdvance.setMinimum(1)
        self.spbxSchedTblMaxAdvance.setMaximum(65535)
        self.spbxSchedTblMaxAdvance.setObjectName(_fromUtf8("spbxSchedTblMaxAdvance"))
        self.gridLayout.addWidget(self.spbxSchedTblMaxAdvance, 7, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.layoutWidget4)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)
        self.spbxSchedTblMaxRetard = QtGui.QSpinBox(self.layoutWidget4)
        self.spbxSchedTblMaxRetard.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblMaxRetard.setMinimum(1)
        self.spbxSchedTblMaxRetard.setMaximum(65535)
        self.spbxSchedTblMaxRetard.setObjectName(_fromUtf8("spbxSchedTblMaxRetard"))
        self.gridLayout.addWidget(self.spbxSchedTblMaxRetard, 8, 1, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget4)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)
        self.spbxSchedTblPrecision = QtGui.QSpinBox(self.layoutWidget4)
        self.spbxSchedTblPrecision.setMinimumSize(QtCore.QSize(181, 0))
        self.spbxSchedTblPrecision.setMinimum(0)
        self.spbxSchedTblPrecision.setMaximum(65535)
        self.spbxSchedTblPrecision.setProperty(_fromUtf8("value"), 0)
        self.spbxSchedTblPrecision.setObjectName(_fromUtf8("spbxSchedTblPrecision"))
        self.gridLayout.addWidget(self.spbxSchedTblPrecision, 9, 1, 1, 1)

        self.retranslateUi(ScheduleTable)
        self.tblSchedTable.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(ScheduleTable)

    def retranslateUi(self, ScheduleTable):
        ScheduleTable.setWindowTitle(QtGui.QApplication.translate("ScheduleTable", "GaInOS Schedule Table Configure", None, QtGui.QApplication.UnicodeUTF8))
        self.trSchedTable.headerItem().setText(0, QtGui.QApplication.translate("ScheduleTable", "GaInOS Schedule Table", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ScheduleTable", "Activate Task Id:", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSchedTable.setTabText(self.tblSchedTable.indexOf(self.tab), QtGui.QApplication.translate("ScheduleTable", "ActivateTask", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ScheduleTable", "SetEvent Task Id:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ScheduleTable", "SetEvent Event:", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSchedTable.setTabText(self.tblSchedTable.indexOf(self.tab_2), QtGui.QApplication.translate("ScheduleTable", "SetEvent", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ScheduleTable", "Offset:", None, QtGui.QApplication.UnicodeUTF8))
        self.tblSchedTable.setTabText(self.tblSchedTable.indexOf(self.tab_3), QtGui.QApplication.translate("ScheduleTable", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("ScheduleTable", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.btnInsert.setText(QtGui.QApplication.translate("ScheduleTable", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDelete.setText(QtGui.QApplication.translate("ScheduleTable", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSchedTblRepeatable.setText(QtGui.QApplication.translate("ScheduleTable", "Schedule Table Repeatable", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ScheduleTable", "Dirving Counter:", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxSchedTblAutostartable.setText(QtGui.QApplication.translate("ScheduleTable", "Schedule Table Auto-Start", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ScheduleTable", "Auto-Start Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblAutoStartType.setItemText(0, QtGui.QApplication.translate("ScheduleTable", "ABSOLUTE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblAutoStartType.setItemText(1, QtGui.QApplication.translate("ScheduleTable", "RELATIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblAutoStartType.setItemText(2, QtGui.QApplication.translate("ScheduleTable", "SYNCHRON", None, QtGui.QApplication.UnicodeUTF8))
        self.lblSchedTblAbsRel.setText(QtGui.QApplication.translate("ScheduleTable", "Absolut Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ScheduleTable", "Final Delay:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ScheduleTable", "Sync Strategy:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblSyncStrategy.setItemText(0, QtGui.QApplication.translate("ScheduleTable", "NONE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblSyncStrategy.setItemText(1, QtGui.QApplication.translate("ScheduleTable", "EXPLICIT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxSchedTblSyncStrategy.setItemText(2, QtGui.QApplication.translate("ScheduleTable", "IMPLICIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ScheduleTable", "Max Advance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ScheduleTable", "Max Retard:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ScheduleTable", "Precision:", None, QtGui.QApplication.UnicodeUTF8))

