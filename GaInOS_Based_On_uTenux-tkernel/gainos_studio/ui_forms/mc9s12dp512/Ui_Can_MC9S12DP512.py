# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\parai@foxmail.com\nt\gainos-tkernel\gainos_studio\ui_forms\mc9s12dp512\Can_MC9S12DP512.ui'
#
# Created: Sun Apr 07 23:37:10 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DlgCanMC9S12DP512(object):
    def setupUi(self, DlgCanMC9S12DP512):
        DlgCanMC9S12DP512.setObjectName(_fromUtf8("DlgCanMC9S12DP512"))
        DlgCanMC9S12DP512.resize(1023, 563)
        DlgCanMC9S12DP512.setStyleSheet(_fromUtf8("font: 12pt \"Consolas\";"))
        self.groupBox = QtGui.QGroupBox(DlgCanMC9S12DP512)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 1001, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 31, 311, 87))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cbxDevErr = QtGui.QCheckBox(self.layoutWidget)
        self.cbxDevErr.setObjectName(_fromUtf8("cbxDevErr"))
        self.verticalLayout.addWidget(self.cbxDevErr)
        self.cbxCanVersionInfo = QtGui.QCheckBox(self.layoutWidget)
        self.cbxCanVersionInfo.setObjectName(_fromUtf8("cbxCanVersionInfo"))
        self.verticalLayout.addWidget(self.cbxCanVersionInfo)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spbxTimeout = QtGui.QSpinBox(self.layoutWidget)
        self.spbxTimeout.setMinimumSize(QtCore.QSize(101, 0))
        self.spbxTimeout.setMinimum(1)
        self.spbxTimeout.setMaximum(65535)
        self.spbxTimeout.setProperty(_fromUtf8("value"), 10)
        self.spbxTimeout.setObjectName(_fromUtf8("spbxTimeout"))
        self.horizontalLayout.addWidget(self.spbxTimeout)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtGui.QGroupBox(DlgCanMC9S12DP512)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 1001, 421))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.trCanCfg = QtGui.QTreeWidget(self.groupBox_2)
        self.trCanCfg.setGeometry(QtCore.QRect(20, 30, 311, 371))
        self.trCanCfg.setObjectName(_fromUtf8("trCanCfg"))
        item_0 = QtGui.QTreeWidgetItem(self.trCanCfg)
        item_0 = QtGui.QTreeWidgetItem(self.trCanCfg)
        self.tabCfg = QtGui.QTabWidget(self.groupBox_2)
        self.tabCfg.setGeometry(QtCore.QRect(490, 30, 491, 381))
        self.tabCfg.setObjectName(_fromUtf8("tabCfg"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget1 = QtGui.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 70, 275, 165))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_36 = QtGui.QHBoxLayout()
        self.horizontalLayout_36.setObjectName(_fromUtf8("horizontalLayout_36"))
        self.label_33 = QtGui.QLabel(self.layoutWidget1)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.horizontalLayout_36.addWidget(self.label_33)
        self.leCtrlName = QtGui.QLineEdit(self.layoutWidget1)
        self.leCtrlName.setText(_fromUtf8(""))
        self.leCtrlName.setObjectName(_fromUtf8("leCtrlName"))
        self.horizontalLayout_36.addWidget(self.leCtrlName)
        self.verticalLayout_9.addLayout(self.horizontalLayout_36)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_23 = QtGui.QHBoxLayout()
        self.horizontalLayout_23.setObjectName(_fromUtf8("horizontalLayout_23"))
        self.label_20 = QtGui.QLabel(self.layoutWidget1)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.horizontalLayout_23.addWidget(self.label_20)
        self.spbxBaudrate = QtGui.QSpinBox(self.layoutWidget1)
        self.spbxBaudrate.setMinimumSize(QtCore.QSize(128, 0))
        self.spbxBaudrate.setMinimum(1)
        self.spbxBaudrate.setMaximum(2000)
        self.spbxBaudrate.setProperty(_fromUtf8("value"), 250)
        self.spbxBaudrate.setObjectName(_fromUtf8("spbxBaudrate"))
        self.horizontalLayout_23.addWidget(self.spbxBaudrate)
        self.verticalLayout_6.addLayout(self.horizontalLayout_23)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_25 = QtGui.QHBoxLayout()
        self.horizontalLayout_25.setObjectName(_fromUtf8("horizontalLayout_25"))
        self.label_22 = QtGui.QLabel(self.layoutWidget1)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_25.addWidget(self.label_22)
        self.spbxPropSeg = QtGui.QSpinBox(self.layoutWidget1)
        self.spbxPropSeg.setMaximum(3)
        self.spbxPropSeg.setObjectName(_fromUtf8("spbxPropSeg"))
        self.horizontalLayout_25.addWidget(self.spbxPropSeg)
        self.verticalLayout_4.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_23 = QtGui.QLabel(self.layoutWidget1)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.horizontalLayout_26.addWidget(self.label_23)
        self.spbxSeg1 = QtGui.QSpinBox(self.layoutWidget1)
        self.spbxSeg1.setMaximum(15)
        self.spbxSeg1.setProperty(_fromUtf8("value"), 13)
        self.spbxSeg1.setObjectName(_fromUtf8("spbxSeg1"))
        self.horizontalLayout_26.addWidget(self.spbxSeg1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        self.horizontalLayout_27 = QtGui.QHBoxLayout()
        self.horizontalLayout_27.setObjectName(_fromUtf8("horizontalLayout_27"))
        self.label_24 = QtGui.QLabel(self.layoutWidget1)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_27.addWidget(self.label_24)
        self.spbxSeg2 = QtGui.QSpinBox(self.layoutWidget1)
        self.spbxSeg2.setMaximum(7)
        self.spbxSeg2.setProperty(_fromUtf8("value"), 2)
        self.spbxSeg2.setObjectName(_fromUtf8("spbxSeg2"))
        self.horizontalLayout_27.addWidget(self.spbxSeg2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_27)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.tabCfg.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 40, 362, 229))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_35 = QtGui.QHBoxLayout()
        self.horizontalLayout_35.setObjectName(_fromUtf8("horizontalLayout_35"))
        self.label_32 = QtGui.QLabel(self.layoutWidget2)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.horizontalLayout_35.addWidget(self.label_32)
        self.leHohName = QtGui.QLineEdit(self.layoutWidget2)
        self.leHohName.setText(_fromUtf8(""))
        self.leHohName.setObjectName(_fromUtf8("leHohName"))
        self.horizontalLayout_35.addWidget(self.leHohName)
        self.verticalLayout_8.addLayout(self.horizontalLayout_35)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_28 = QtGui.QHBoxLayout()
        self.horizontalLayout_28.setObjectName(_fromUtf8("horizontalLayout_28"))
        self.label_25 = QtGui.QLabel(self.layoutWidget2)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.horizontalLayout_28.addWidget(self.label_25)
        self.cmbxHohType = QtGui.QComboBox(self.layoutWidget2)
        self.cmbxHohType.setMinimumSize(QtCore.QSize(250, 0))
        self.cmbxHohType.setObjectName(_fromUtf8("cmbxHohType"))
        self.cmbxHohType.addItem(_fromUtf8(""))
        self.cmbxHohType.addItem(_fromUtf8(""))
        self.horizontalLayout_28.addWidget(self.cmbxHohType)
        self.verticalLayout_5.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_29 = QtGui.QHBoxLayout()
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.label_26 = QtGui.QLabel(self.layoutWidget2)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_29.addWidget(self.label_26)
        self.cmbxIdType = QtGui.QComboBox(self.layoutWidget2)
        self.cmbxIdType.setObjectName(_fromUtf8("cmbxIdType"))
        self.cmbxIdType.addItem(_fromUtf8(""))
        self.cmbxIdType.addItem(_fromUtf8(""))
        self.horizontalLayout_29.addWidget(self.cmbxIdType)
        self.verticalLayout_5.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_30 = QtGui.QHBoxLayout()
        self.horizontalLayout_30.setObjectName(_fromUtf8("horizontalLayout_30"))
        self.label_27 = QtGui.QLabel(self.layoutWidget2)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_30.addWidget(self.label_27)
        self.spbxIdValue = QtGui.QSpinBox(self.layoutWidget2)
        self.spbxIdValue.setObjectName(_fromUtf8("spbxIdValue"))
        self.horizontalLayout_30.addWidget(self.spbxIdValue)
        self.verticalLayout_5.addLayout(self.horizontalLayout_30)
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.label_28 = QtGui.QLabel(self.layoutWidget2)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.horizontalLayout_31.addWidget(self.label_28)
        self.cmbxObjType = QtGui.QComboBox(self.layoutWidget2)
        self.cmbxObjType.setObjectName(_fromUtf8("cmbxObjType"))
        self.cmbxObjType.addItem(_fromUtf8(""))
        self.cmbxObjType.addItem(_fromUtf8(""))
        self.horizontalLayout_31.addWidget(self.cmbxObjType)
        self.verticalLayout_5.addLayout(self.horizontalLayout_31)
        self.horizontalLayout_32 = QtGui.QHBoxLayout()
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.label_29 = QtGui.QLabel(self.layoutWidget2)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.horizontalLayout_32.addWidget(self.label_29)
        self.cmbxFilterMask = QtGui.QComboBox(self.layoutWidget2)
        self.cmbxFilterMask.setMinimumSize(QtCore.QSize(231, 0))
        self.cmbxFilterMask.setObjectName(_fromUtf8("cmbxFilterMask"))
        self.horizontalLayout_32.addWidget(self.cmbxFilterMask)
        self.verticalLayout_5.addLayout(self.horizontalLayout_32)
        self.horizontalLayout_33 = QtGui.QHBoxLayout()
        self.horizontalLayout_33.setObjectName(_fromUtf8("horizontalLayout_33"))
        self.label_30 = QtGui.QLabel(self.layoutWidget2)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.horizontalLayout_33.addWidget(self.label_30)
        self.leMbMask = QtGui.QLineEdit(self.layoutWidget2)
        self.leMbMask.setText(_fromUtf8(""))
        self.leMbMask.setObjectName(_fromUtf8("leMbMask"))
        self.horizontalLayout_33.addWidget(self.leMbMask)
        self.verticalLayout_5.addLayout(self.horizontalLayout_33)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        self.tabCfg.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.layoutWidget3 = QtGui.QWidget(self.tab_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 110, 461, 136))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_4 = QtGui.QLabel(self.layoutWidget3)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_3.addWidget(self.label_4)
        self.leIdar0 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar0.setText(_fromUtf8(""))
        self.leIdar0.setObjectName(_fromUtf8("leIdar0"))
        self.horizontalLayout_3.addWidget(self.leIdar0)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_5 = QtGui.QLabel(self.layoutWidget3)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_4.addWidget(self.label_5)
        self.leIdar1 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar1.setText(_fromUtf8(""))
        self.leIdar1.setObjectName(_fromUtf8("leIdar1"))
        self.horizontalLayout_4.addWidget(self.leIdar1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_6 = QtGui.QLabel(self.layoutWidget3)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_5.addWidget(self.label_6)
        self.leIdar2 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar2.setText(_fromUtf8(""))
        self.leIdar2.setObjectName(_fromUtf8("leIdar2"))
        self.horizontalLayout_5.addWidget(self.leIdar2)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_7 = QtGui.QLabel(self.layoutWidget3)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_6.addWidget(self.label_7)
        self.leIdar3 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar3.setText(_fromUtf8(""))
        self.leIdar3.setObjectName(_fromUtf8("leIdar3"))
        self.horizontalLayout_6.addWidget(self.leIdar3)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_8 = QtGui.QLabel(self.layoutWidget3)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_9.addWidget(self.label_8)
        self.leIdmr0 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr0.setText(_fromUtf8(""))
        self.leIdmr0.setObjectName(_fromUtf8("leIdmr0"))
        self.horizontalLayout_9.addWidget(self.leIdmr0)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_9 = QtGui.QLabel(self.layoutWidget3)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_10.addWidget(self.label_9)
        self.leIdmr1 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr1.setText(_fromUtf8(""))
        self.leIdmr1.setObjectName(_fromUtf8("leIdmr1"))
        self.horizontalLayout_10.addWidget(self.leIdmr1)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.label_10 = QtGui.QLabel(self.layoutWidget3)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_11.addWidget(self.label_10)
        self.leIdmr2 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr2.setText(_fromUtf8(""))
        self.leIdmr2.setObjectName(_fromUtf8("leIdmr2"))
        self.horizontalLayout_11.addWidget(self.leIdmr2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_11 = QtGui.QLabel(self.layoutWidget3)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_12.addWidget(self.label_11)
        self.leIdmr3 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr3.setText(_fromUtf8(""))
        self.leIdmr3.setObjectName(_fromUtf8("leIdmr3"))
        self.horizontalLayout_12.addWidget(self.leIdmr3)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.label_16 = QtGui.QLabel(self.layoutWidget3)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_19.addWidget(self.label_16)
        self.leIdar4 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar4.setText(_fromUtf8(""))
        self.leIdar4.setObjectName(_fromUtf8("leIdar4"))
        self.horizontalLayout_19.addWidget(self.leIdar4)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_17 = QtGui.QLabel(self.layoutWidget3)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_20.addWidget(self.label_17)
        self.leIdar5 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar5.setText(_fromUtf8(""))
        self.leIdar5.setObjectName(_fromUtf8("leIdar5"))
        self.horizontalLayout_20.addWidget(self.leIdar5)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.label_18 = QtGui.QLabel(self.layoutWidget3)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.horizontalLayout_21.addWidget(self.label_18)
        self.leIdar6 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar6.setText(_fromUtf8(""))
        self.leIdar6.setObjectName(_fromUtf8("leIdar6"))
        self.horizontalLayout_21.addWidget(self.leIdar6)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.label_19 = QtGui.QLabel(self.layoutWidget3)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.horizontalLayout_22.addWidget(self.label_19)
        self.leIdar7 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdar7.setText(_fromUtf8(""))
        self.leIdar7.setObjectName(_fromUtf8("leIdar7"))
        self.horizontalLayout_22.addWidget(self.leIdar7)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_22)
        self.verticalLayout_3.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_12 = QtGui.QLabel(self.layoutWidget3)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_14.addWidget(self.label_12)
        self.leIdmr4 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr4.setText(_fromUtf8(""))
        self.leIdmr4.setObjectName(_fromUtf8("leIdmr4"))
        self.horizontalLayout_14.addWidget(self.leIdmr4)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_13 = QtGui.QLabel(self.layoutWidget3)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_15.addWidget(self.label_13)
        self.leIdmr5 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr5.setText(_fromUtf8(""))
        self.leIdmr5.setObjectName(_fromUtf8("leIdmr5"))
        self.horizontalLayout_15.addWidget(self.leIdmr5)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.label_14 = QtGui.QLabel(self.layoutWidget3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_16.addWidget(self.label_14)
        self.leIdmr6 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr6.setText(_fromUtf8(""))
        self.leIdmr6.setObjectName(_fromUtf8("leIdmr6"))
        self.horizontalLayout_16.addWidget(self.leIdmr6)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_15 = QtGui.QLabel(self.layoutWidget3)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_17.addWidget(self.label_15)
        self.leIdmr7 = QtGui.QLineEdit(self.layoutWidget3)
        self.leIdmr7.setText(_fromUtf8(""))
        self.leIdmr7.setObjectName(_fromUtf8("leIdmr7"))
        self.horizontalLayout_17.addWidget(self.leIdmr7)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_17)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.layoutWidget4 = QtGui.QWidget(self.tab_3)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 30, 279, 62))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_34 = QtGui.QHBoxLayout()
        self.horizontalLayout_34.setObjectName(_fromUtf8("horizontalLayout_34"))
        self.label_31 = QtGui.QLabel(self.layoutWidget4)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.horizontalLayout_34.addWidget(self.label_31)
        self.leFmName = QtGui.QLineEdit(self.layoutWidget4)
        self.leFmName.setText(_fromUtf8(""))
        self.leFmName.setObjectName(_fromUtf8("leFmName"))
        self.horizontalLayout_34.addWidget(self.leFmName)
        self.verticalLayout_7.addLayout(self.horizontalLayout_34)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.layoutWidget4)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cmbxIdam = QtGui.QComboBox(self.layoutWidget4)
        self.cmbxIdam.setObjectName(_fromUtf8("cmbxIdam"))
        self.cmbxIdam.addItem(_fromUtf8(""))
        self.cmbxIdam.addItem(_fromUtf8(""))
        self.cmbxIdam.addItem(_fromUtf8(""))
        self.cmbxIdam.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cmbxIdam)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.tabCfg.addTab(self.tab_3, _fromUtf8(""))
        self.layoutWidget5 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget5.setGeometry(QtCore.QRect(350, 50, 121, 62))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btnAdd = QtGui.QPushButton(self.layoutWidget5)
        self.btnAdd.setObjectName(_fromUtf8("btnAdd"))
        self.verticalLayout_2.addWidget(self.btnAdd)
        self.btnDel = QtGui.QPushButton(self.layoutWidget5)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.verticalLayout_2.addWidget(self.btnDel)

        self.retranslateUi(DlgCanMC9S12DP512)
        self.tabCfg.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DlgCanMC9S12DP512)

    def retranslateUi(self, DlgCanMC9S12DP512):
        DlgCanMC9S12DP512.setWindowTitle(QtGui.QApplication.translate("DlgCanMC9S12DP512", "MSCAN(MC9S12DP512)  Autosar", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Can General", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxDevErr.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "CanDevErrorDetection", None, QtGui.QApplication.UnicodeUTF8))
        self.cbxCanVersionInfo.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "CanVersionInfoApi", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "CanTimeoutDuration:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Can Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.trCanCfg.headerItem().setText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "Can", None, QtGui.QApplication.UnicodeUTF8))
        __sortingEnabled = self.trCanCfg.isSortingEnabled()
        self.trCanCfg.setSortingEnabled(False)
        self.trCanCfg.topLevelItem(0).setText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CanFilterMask", None, QtGui.QApplication.UnicodeUTF8))
        self.trCanCfg.topLevelItem(1).setText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CanController", None, QtGui.QApplication.UnicodeUTF8))
        self.trCanCfg.setSortingEnabled(__sortingEnabled)
        self.label_33.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Baudrate(kbps):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "PropSeg:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Seg1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Seg2:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab), QtGui.QApplication.translate("DlgCanMC9S12DP512", "Controller", None, QtGui.QApplication.UnicodeUTF8))
        self.label_32.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Hoh Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxHohType.setItemText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_ARC_HANDLE_TYPE_BASIC", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxHohType.setItemText(1, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_ARC_HANDLE_TYPE_FULL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Id Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxIdType.setItemText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_ID_TYPE_EXTENDED", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxIdType.setItemText(1, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_ID_TYPE_STANDARD", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Id Value:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Object Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxObjType.setItemText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_OBJECT_TYPE_RECEIVE", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxObjType.setItemText(1, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_OBJECT_TYPE_TRANSMIT", None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Filter Mask:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "MbMask:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_2), QtGui.QApplication.translate("DlgCanMC9S12DP512", "Hardware Object", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar0:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr0:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr3:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar4:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar5:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar6:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idar7:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr4:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr5:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr6:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "idmr7:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "IDAM:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxIdam.setItemText(0, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_IDAM_2_32BIT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxIdam.setItemText(1, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_IDAM_4_16BIT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxIdam.setItemText(2, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_IDAM_8_8BIT", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbxIdam.setItemText(3, QtGui.QApplication.translate("DlgCanMC9S12DP512", "CAN_IDAM_FILTER_CLOSED", None, QtGui.QApplication.UnicodeUTF8))
        self.tabCfg.setTabText(self.tabCfg.indexOf(self.tab_3), QtGui.QApplication.translate("DlgCanMC9S12DP512", "Filter Mask", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAdd.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Add Hoh", None, QtGui.QApplication.UnicodeUTF8))
        self.btnDel.setText(QtGui.QApplication.translate("DlgCanMC9S12DP512", "Del", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DlgCanMC9S12DP512 = QtGui.QDialog()
    ui = Ui_DlgCanMC9S12DP512()
    ui.setupUi(DlgCanMC9S12DP512)
    DlgCanMC9S12DP512.show()
    sys.exit(app.exec_())

