# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/Jenks/maya/scripts/Jenks/scripts/modularRig/uiTest2_UI.ui'
#
# Created: Thu Jun 29 21:21:50 2017
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 750)
        Form.setMinimumSize(QtCore.QSize(450, 500))
        Form.setMaximumSize(QtCore.QSize(496, 16777215))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(6, 4, 6, 4)
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.colBox = QtWidgets.QGroupBox(Form)
        self.colBox.setMaximumSize(QtCore.QSize(16777215, 175))
        self.colBox.setObjectName("colBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.colBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainColsBox = QtWidgets.QGroupBox(self.colBox)
        self.mainColsBox.setTitle("")
        self.mainColsBox.setFlat(True)
        self.mainColsBox.setObjectName("mainColsBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.mainColsBox)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.main1Lab = QtWidgets.QLabel(self.mainColsBox)
        self.main1Lab.setObjectName("main1Lab")
        self.horizontalLayout_8.addWidget(self.main1Lab)
        self.main1SpnBox = QtWidgets.QSpinBox(self.mainColsBox)
        self.main1SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.main1SpnBox.setMinimum(1)
        self.main1SpnBox.setMaximum(33)
        self.main1SpnBox.setProperty("value", 11)
        self.main1SpnBox.setObjectName("main1SpnBox")
        self.horizontalLayout_8.addWidget(self.main1SpnBox)
        self.main1ImgBtn = QtWidgets.QPushButton(self.mainColsBox)
        self.main1ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.main1ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.main1ImgBtn.setText("")
        self.main1ImgBtn.setObjectName("main1ImgBtn")
        self.horizontalLayout_8.addWidget(self.main1ImgBtn)
        self.main2Lab = QtWidgets.QLabel(self.mainColsBox)
        self.main2Lab.setObjectName("main2Lab")
        self.horizontalLayout_8.addWidget(self.main2Lab)
        self.main2SpnBox = QtWidgets.QSpinBox(self.mainColsBox)
        self.main2SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.main2SpnBox.setMinimum(1)
        self.main2SpnBox.setMaximum(33)
        self.main2SpnBox.setProperty("value", 23)
        self.main2SpnBox.setObjectName("main2SpnBox")
        self.horizontalLayout_8.addWidget(self.main2SpnBox)
        self.main2ImgBtn = QtWidgets.QPushButton(self.mainColsBox)
        self.main2ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.main2ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.main2ImgBtn.setText("")
        self.main2ImgBtn.setObjectName("main2ImgBtn")
        self.horizontalLayout_8.addWidget(self.main2ImgBtn)
        self.main3Lab = QtWidgets.QLabel(self.mainColsBox)
        self.main3Lab.setObjectName("main3Lab")
        self.horizontalLayout_8.addWidget(self.main3Lab)
        self.main3SpnBox = QtWidgets.QSpinBox(self.mainColsBox)
        self.main3SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.main3SpnBox.setMinimum(1)
        self.main3SpnBox.setMaximum(33)
        self.main3SpnBox.setProperty("value", 24)
        self.main3SpnBox.setObjectName("main3SpnBox")
        self.horizontalLayout_8.addWidget(self.main3SpnBox)
        self.main3ImgBtn = QtWidgets.QPushButton(self.mainColsBox)
        self.main3ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.main3ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.main3ImgBtn.setText("")
        self.main3ImgBtn.setObjectName("main3ImgBtn")
        self.horizontalLayout_8.addWidget(self.main3ImgBtn)
        self.verticalLayout.addWidget(self.mainColsBox)
        self.leftColsBox = QtWidgets.QGroupBox(self.colBox)
        self.leftColsBox.setTitle("")
        self.leftColsBox.setFlat(True)
        self.leftColsBox.setObjectName("leftColsBox")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.leftColsBox)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.left1Lab = QtWidgets.QLabel(self.leftColsBox)
        self.left1Lab.setObjectName("left1Lab")
        self.horizontalLayout_7.addWidget(self.left1Lab)
        self.left1SpnBox = QtWidgets.QSpinBox(self.leftColsBox)
        self.left1SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.left1SpnBox.setMinimum(1)
        self.left1SpnBox.setMaximum(33)
        self.left1SpnBox.setProperty("value", 16)
        self.left1SpnBox.setObjectName("left1SpnBox")
        self.horizontalLayout_7.addWidget(self.left1SpnBox)
        self.left1ImgBtn = QtWidgets.QPushButton(self.leftColsBox)
        self.left1ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.left1ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.left1ImgBtn.setText("")
        self.left1ImgBtn.setObjectName("left1ImgBtn")
        self.horizontalLayout_7.addWidget(self.left1ImgBtn)
        self.left2Lab = QtWidgets.QLabel(self.leftColsBox)
        self.left2Lab.setObjectName("left2Lab")
        self.horizontalLayout_7.addWidget(self.left2Lab)
        self.left2SpnBox = QtWidgets.QSpinBox(self.leftColsBox)
        self.left2SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.left2SpnBox.setMinimum(1)
        self.left2SpnBox.setMaximum(33)
        self.left2SpnBox.setProperty("value", 29)
        self.left2SpnBox.setObjectName("left2SpnBox")
        self.horizontalLayout_7.addWidget(self.left2SpnBox)
        self.left2ImgBtn = QtWidgets.QPushButton(self.leftColsBox)
        self.left2ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.left2ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.left2ImgBtn.setText("")
        self.left2ImgBtn.setObjectName("left2ImgBtn")
        self.horizontalLayout_7.addWidget(self.left2ImgBtn)
        self.left3Lab = QtWidgets.QLabel(self.leftColsBox)
        self.left3Lab.setObjectName("left3Lab")
        self.horizontalLayout_7.addWidget(self.left3Lab)
        self.left3SpnBox = QtWidgets.QSpinBox(self.leftColsBox)
        self.left3SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.left3SpnBox.setMinimum(1)
        self.left3SpnBox.setMaximum(33)
        self.left3SpnBox.setProperty("value", 30)
        self.left3SpnBox.setObjectName("left3SpnBox")
        self.horizontalLayout_7.addWidget(self.left3SpnBox)
        self.left3ImgBtn = QtWidgets.QPushButton(self.leftColsBox)
        self.left3ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.left3ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.left3ImgBtn.setText("")
        self.left3ImgBtn.setObjectName("left3ImgBtn")
        self.horizontalLayout_7.addWidget(self.left3ImgBtn)
        self.verticalLayout.addWidget(self.leftColsBox)
        self.rightColsBox = QtWidgets.QGroupBox(self.colBox)
        self.rightColsBox.setTitle("")
        self.rightColsBox.setFlat(True)
        self.rightColsBox.setObjectName("rightColsBox")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.rightColsBox)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.right1Lab = QtWidgets.QLabel(self.rightColsBox)
        self.right1Lab.setObjectName("right1Lab")
        self.horizontalLayout_6.addWidget(self.right1Lab)
        self.right1SpnBox = QtWidgets.QSpinBox(self.rightColsBox)
        self.right1SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.right1SpnBox.setMinimum(1)
        self.right1SpnBox.setMaximum(33)
        self.right1SpnBox.setProperty("value", 13)
        self.right1SpnBox.setObjectName("right1SpnBox")
        self.horizontalLayout_6.addWidget(self.right1SpnBox)
        self.right1ImgBtn = QtWidgets.QPushButton(self.rightColsBox)
        self.right1ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.right1ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.right1ImgBtn.setText("")
        self.right1ImgBtn.setObjectName("right1ImgBtn")
        self.horizontalLayout_6.addWidget(self.right1ImgBtn)
        self.right2Lab = QtWidgets.QLabel(self.rightColsBox)
        self.right2Lab.setObjectName("right2Lab")
        self.horizontalLayout_6.addWidget(self.right2Lab)
        self.right2SpnBox = QtWidgets.QSpinBox(self.rightColsBox)
        self.right2SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.right2SpnBox.setMinimum(1)
        self.right2SpnBox.setMaximum(33)
        self.right2SpnBox.setProperty("value", 25)
        self.right2SpnBox.setObjectName("right2SpnBox")
        self.horizontalLayout_6.addWidget(self.right2SpnBox)
        self.right2ImgBtn = QtWidgets.QPushButton(self.rightColsBox)
        self.right2ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.right2ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.right2ImgBtn.setText("")
        self.right2ImgBtn.setObjectName("right2ImgBtn")
        self.horizontalLayout_6.addWidget(self.right2ImgBtn)
        self.right3Lab = QtWidgets.QLabel(self.rightColsBox)
        self.right3Lab.setObjectName("right3Lab")
        self.horizontalLayout_6.addWidget(self.right3Lab)
        self.right3SpnBox = QtWidgets.QSpinBox(self.rightColsBox)
        self.right3SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.right3SpnBox.setMinimum(1)
        self.right3SpnBox.setMaximum(33)
        self.right3SpnBox.setProperty("value", 22)
        self.right3SpnBox.setObjectName("right3SpnBox")
        self.horizontalLayout_6.addWidget(self.right3SpnBox)
        self.right3ImgBtn = QtWidgets.QPushButton(self.rightColsBox)
        self.right3ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.right3ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.right3ImgBtn.setText("")
        self.right3ImgBtn.setObjectName("right3ImgBtn")
        self.horizontalLayout_6.addWidget(self.right3ImgBtn)
        self.verticalLayout.addWidget(self.rightColsBox)
        self.settingsColsBox = QtWidgets.QGroupBox(self.colBox)
        self.settingsColsBox.setTitle("")
        self.settingsColsBox.setFlat(True)
        self.settingsColsBox.setObjectName("settingsColsBox")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.settingsColsBox)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.settings1Lab = QtWidgets.QLabel(self.settingsColsBox)
        self.settings1Lab.setObjectName("settings1Lab")
        self.horizontalLayout_5.addWidget(self.settings1Lab)
        self.settings1SpnBox = QtWidgets.QSpinBox(self.settingsColsBox)
        self.settings1SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.settings1SpnBox.setMinimum(1)
        self.settings1SpnBox.setMaximum(33)
        self.settings1SpnBox.setProperty("value", 27)
        self.settings1SpnBox.setObjectName("settings1SpnBox")
        self.horizontalLayout_5.addWidget(self.settings1SpnBox)
        self.settings1ImgBtn = QtWidgets.QPushButton(self.settingsColsBox)
        self.settings1ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.settings1ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.settings1ImgBtn.setText("")
        self.settings1ImgBtn.setObjectName("settings1ImgBtn")
        self.horizontalLayout_5.addWidget(self.settings1ImgBtn)
        self.settings2Lab = QtWidgets.QLabel(self.settingsColsBox)
        self.settings2Lab.setObjectName("settings2Lab")
        self.horizontalLayout_5.addWidget(self.settings2Lab)
        self.settings2SpnBox = QtWidgets.QSpinBox(self.settingsColsBox)
        self.settings2SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.settings2SpnBox.setMinimum(1)
        self.settings2SpnBox.setMaximum(33)
        self.settings2SpnBox.setProperty("value", 32)
        self.settings2SpnBox.setObjectName("settings2SpnBox")
        self.horizontalLayout_5.addWidget(self.settings2SpnBox)
        self.settings2ImgBtn = QtWidgets.QPushButton(self.settingsColsBox)
        self.settings2ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.settings2ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.settings2ImgBtn.setText("")
        self.settings2ImgBtn.setObjectName("settings2ImgBtn")
        self.horizontalLayout_5.addWidget(self.settings2ImgBtn)
        self.settings3Lab = QtWidgets.QLabel(self.settingsColsBox)
        self.settings3Lab.setObjectName("settings3Lab")
        self.horizontalLayout_5.addWidget(self.settings3Lab)
        self.settings3SpnBox = QtWidgets.QSpinBox(self.settingsColsBox)
        self.settings3SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.settings3SpnBox.setMinimum(1)
        self.settings3SpnBox.setMaximum(33)
        self.settings3SpnBox.setProperty("value", 8)
        self.settings3SpnBox.setObjectName("settings3SpnBox")
        self.horizontalLayout_5.addWidget(self.settings3SpnBox)
        self.settings3ImgBtn = QtWidgets.QPushButton(self.settingsColsBox)
        self.settings3ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.settings3ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.settings3ImgBtn.setText("")
        self.settings3ImgBtn.setObjectName("settings3ImgBtn")
        self.horizontalLayout_5.addWidget(self.settings3ImgBtn)
        self.verticalLayout.addWidget(self.settingsColsBox)
        self.miscColsBox = QtWidgets.QGroupBox(self.colBox)
        self.miscColsBox.setTitle("")
        self.miscColsBox.setFlat(True)
        self.miscColsBox.setObjectName("miscColsBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.miscColsBox)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.misc1Lab = QtWidgets.QLabel(self.miscColsBox)
        self.misc1Lab.setObjectName("misc1Lab")
        self.horizontalLayout_4.addWidget(self.misc1Lab)
        self.misc1SpnBox = QtWidgets.QSpinBox(self.miscColsBox)
        self.misc1SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.misc1SpnBox.setMinimum(1)
        self.misc1SpnBox.setMaximum(33)
        self.misc1SpnBox.setProperty("value", 31)
        self.misc1SpnBox.setObjectName("misc1SpnBox")
        self.horizontalLayout_4.addWidget(self.misc1SpnBox)
        self.misc1ImgBtn = QtWidgets.QPushButton(self.miscColsBox)
        self.misc1ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.misc1ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.misc1ImgBtn.setText("")
        self.misc1ImgBtn.setObjectName("misc1ImgBtn")
        self.horizontalLayout_4.addWidget(self.misc1ImgBtn)
        self.misc2Lab = QtWidgets.QLabel(self.miscColsBox)
        self.misc2Lab.setObjectName("misc2Lab")
        self.horizontalLayout_4.addWidget(self.misc2Lab)
        self.misc2SpnBox = QtWidgets.QSpinBox(self.miscColsBox)
        self.misc2SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.misc2SpnBox.setMinimum(1)
        self.misc2SpnBox.setMaximum(33)
        self.misc2SpnBox.setObjectName("misc2SpnBox")
        self.horizontalLayout_4.addWidget(self.misc2SpnBox)
        self.misc2ImgBtn = QtWidgets.QPushButton(self.miscColsBox)
        self.misc2ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.misc2ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.misc2ImgBtn.setText("")
        self.misc2ImgBtn.setObjectName("misc2ImgBtn")
        self.horizontalLayout_4.addWidget(self.misc2ImgBtn)
        self.misc3Lab = QtWidgets.QLabel(self.miscColsBox)
        self.misc3Lab.setObjectName("misc3Lab")
        self.horizontalLayout_4.addWidget(self.misc3Lab)
        self.misc3SpnBox = QtWidgets.QSpinBox(self.miscColsBox)
        self.misc3SpnBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.misc3SpnBox.setMinimum(1)
        self.misc3SpnBox.setMaximum(33)
        self.misc3SpnBox.setObjectName("misc3SpnBox")
        self.horizontalLayout_4.addWidget(self.misc3SpnBox)
        self.misc3ImgBtn = QtWidgets.QPushButton(self.miscColsBox)
        self.misc3ImgBtn.setMinimumSize(QtCore.QSize(20, 20))
        self.misc3ImgBtn.setMaximumSize(QtCore.QSize(20, 20))
        self.misc3ImgBtn.setText("")
        self.misc3ImgBtn.setObjectName("misc3ImgBtn")
        self.horizontalLayout_4.addWidget(self.misc3ImgBtn)
        self.verticalLayout.addWidget(self.miscColsBox)
        self.gridLayout.addWidget(self.colBox, 3, 0, 1, 4)
        self.creationLay = QtWidgets.QHBoxLayout()
        self.creationLay.setSpacing(8)
        self.creationLay.setContentsMargins(6, 4, 6, 4)
        self.creationLay.setObjectName("creationLay")
        self.locsBtn = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.locsBtn.sizePolicy().hasHeightForWidth())
        self.locsBtn.setSizePolicy(sizePolicy)
        self.locsBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.locsBtn.setObjectName("locsBtn")
        self.creationLay.addWidget(self.locsBtn)
        self.mirrorBtn = QtWidgets.QPushButton(Form)
        self.mirrorBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.mirrorBtn.setObjectName("mirrorBtn")
        self.creationLay.addWidget(self.mirrorBtn)
        self.createBtn = QtWidgets.QPushButton(Form)
        self.createBtn.setMinimumSize(QtCore.QSize(0, 60))
        self.createBtn.setObjectName("createBtn")
        self.creationLay.addWidget(self.createBtn)
        self.gridLayout.addLayout(self.creationLay, 4, 0, 2, 4)
        self.limbBox = QtWidgets.QGroupBox(Form)
        self.limbBox.setObjectName("limbBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.limbBox)
        self.gridLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.limbBox)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 396, 326))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 2, 10, 2)
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 1, 0, 1, 3)
        self.clearEntries = QtWidgets.QPushButton(self.limbBox)
        self.clearEntries.setMinimumSize(QtCore.QSize(0, 20))
        self.clearEntries.setMaximumSize(QtCore.QSize(16777215, 20))
        self.clearEntries.setObjectName("clearEntries")
        self.gridLayout_3.addWidget(self.clearEntries, 0, 2, 1, 1)
        self.newEntry = QtWidgets.QPushButton(self.limbBox)
        self.newEntry.setMinimumSize(QtCore.QSize(20, 20))
        self.newEntry.setMaximumSize(QtCore.QSize(20, 20))
        self.newEntry.setObjectName("newEntry")
        self.gridLayout_3.addWidget(self.newEntry, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.limbBox, 2, 0, 1, 4)
        self.nameBox = QtWidgets.QGroupBox(Form)
        self.nameBox.setObjectName("nameBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.nameBox)
        self.gridLayout_8.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.nameEdit = QtWidgets.QLineEdit(self.nameBox)
        self.nameEdit.setText("")
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout_8.addWidget(self.nameEdit, 0, 1, 1, 1)
        self.nameLab = QtWidgets.QLabel(self.nameBox)
        self.nameLab.setObjectName("nameLab")
        self.gridLayout_8.addWidget(self.nameLab, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.nameBox, 0, 0, 1, 1)
        self.scaleBox = QtWidgets.QGroupBox(Form)
        self.scaleBox.setObjectName("scaleBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.scaleBox)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setHorizontalSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ctrlScaleLab = QtWidgets.QLabel(self.scaleBox)
        self.ctrlScaleLab.setObjectName("ctrlScaleLab")
        self.gridLayout_5.addWidget(self.ctrlScaleLab, 0, 2, 1, 1)
        self.locScaleSpnBox = QtWidgets.QDoubleSpinBox(self.scaleBox)
        self.locScaleSpnBox.setMinimumSize(QtCore.QSize(52, 0))
        self.locScaleSpnBox.setMaximumSize(QtCore.QSize(52, 16777215))
        self.locScaleSpnBox.setMinimum(0.01)
        self.locScaleSpnBox.setSingleStep(0.25)
        self.locScaleSpnBox.setProperty("value", 1.0)
        self.locScaleSpnBox.setObjectName("locScaleSpnBox")
        self.gridLayout_5.addWidget(self.locScaleSpnBox, 0, 1, 1, 1)
        self.locScaleLab = QtWidgets.QLabel(self.scaleBox)
        self.locScaleLab.setObjectName("locScaleLab")
        self.gridLayout_5.addWidget(self.locScaleLab, 0, 0, 1, 1)
        self.ctrlScaleSpnBox = QtWidgets.QDoubleSpinBox(self.scaleBox)
        self.ctrlScaleSpnBox.setMinimumSize(QtCore.QSize(52, 0))
        self.ctrlScaleSpnBox.setMaximumSize(QtCore.QSize(52, 16777215))
        self.ctrlScaleSpnBox.setMinimum(0.01)
        self.ctrlScaleSpnBox.setSingleStep(0.25)
        self.ctrlScaleSpnBox.setProperty("value", 1.0)
        self.ctrlScaleSpnBox.setObjectName("ctrlScaleSpnBox")
        self.gridLayout_5.addWidget(self.ctrlScaleSpnBox, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.scaleBox, 1, 0, 1, 1)
        self.locBox = QtWidgets.QGroupBox(Form)
        self.locBox.setMaximumSize(QtCore.QSize(70, 16777215))
        self.locBox.setObjectName("locBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.locBox)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.saveLocsBtn = QtWidgets.QPushButton(self.locBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveLocsBtn.sizePolicy().hasHeightForWidth())
        self.saveLocsBtn.setSizePolicy(sizePolicy)
        self.saveLocsBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.saveLocsBtn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.saveLocsBtn.setObjectName("saveLocsBtn")
        self.verticalLayout_2.addWidget(self.saveLocsBtn)
        self.loadLocsBtn = QtWidgets.QPushButton(self.locBox)
        self.loadLocsBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.loadLocsBtn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.loadLocsBtn.setObjectName("loadLocsBtn")
        self.verticalLayout_2.addWidget(self.loadLocsBtn)
        self.delLocsBtn = QtWidgets.QPushButton(self.locBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delLocsBtn.sizePolicy().hasHeightForWidth())
        self.delLocsBtn.setSizePolicy(sizePolicy)
        self.delLocsBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.delLocsBtn.setMaximumSize(QtCore.QSize(16777215, 20))
        self.delLocsBtn.setObjectName("delLocsBtn")
        self.verticalLayout_2.addWidget(self.delLocsBtn)
        self.gridLayout.addWidget(self.locBox, 0, 3, 2, 1)
        self.settingsBox = QtWidgets.QGroupBox(Form)
        self.settingsBox.setObjectName("settingsBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.settingsBox)
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.modeLay = QtWidgets.QHBoxLayout()
        self.modeLay.setObjectName("modeLay")
        self.biRad = QtWidgets.QRadioButton(self.settingsBox)
        self.biRad.setMinimumSize(QtCore.QSize(50, 0))
        self.biRad.setMaximumSize(QtCore.QSize(50, 16777215))
        self.biRad.setChecked(True)
        self.biRad.setObjectName("biRad")
        self.modeLay.addWidget(self.biRad)
        self.quadRad = QtWidgets.QRadioButton(self.settingsBox)
        self.quadRad.setObjectName("quadRad")
        self.modeLay.addWidget(self.quadRad)
        self.gridLayout_2.addLayout(self.modeLay, 0, 0, 1, 2)
        self.spineLay = QtWidgets.QHBoxLayout()
        self.spineLay.setObjectName("spineLay")
        self.spineChkBox = QtWidgets.QCheckBox(self.settingsBox)
        self.spineChkBox.setMinimumSize(QtCore.QSize(80, 0))
        self.spineChkBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.spineChkBox.setChecked(True)
        self.spineChkBox.setObjectName("spineChkBox")
        self.spineLay.addWidget(self.spineChkBox)
        self.spineSpnBox = QtWidgets.QSpinBox(self.settingsBox)
        self.spineSpnBox.setMinimumSize(QtCore.QSize(45, 0))
        self.spineSpnBox.setMaximumSize(QtCore.QSize(45, 16777215))
        self.spineSpnBox.setMinimum(2)
        self.spineSpnBox.setMaximum(999)
        self.spineSpnBox.setProperty("value", 7)
        self.spineSpnBox.setObjectName("spineSpnBox")
        self.spineLay.addWidget(self.spineSpnBox)
        self.gridLayout_2.addLayout(self.spineLay, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.settingsBox, 0, 1, 2, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Jenks\' Wacky Waving Inflatable Auto-Rigger", None, -1))
        self.colBox.setTitle(QtWidgets.QApplication.translate("Form", "Colour", None, -1))
        self.main1Lab.setText(QtWidgets.QApplication.translate("Form", "Main I", None, -1))
        self.main2Lab.setText(QtWidgets.QApplication.translate("Form", "Main II", None, -1))
        self.main3Lab.setText(QtWidgets.QApplication.translate("Form", "Main III", None, -1))
        self.left1Lab.setText(QtWidgets.QApplication.translate("Form", "Left I", None, -1))
        self.left2Lab.setText(QtWidgets.QApplication.translate("Form", "Left II", None, -1))
        self.left3Lab.setText(QtWidgets.QApplication.translate("Form", "Left III", None, -1))
        self.right1Lab.setText(QtWidgets.QApplication.translate("Form", "Right I", None, -1))
        self.right2Lab.setText(QtWidgets.QApplication.translate("Form", "Right II", None, -1))
        self.right3Lab.setText(QtWidgets.QApplication.translate("Form", "Right III", None, -1))
        self.settings1Lab.setText(QtWidgets.QApplication.translate("Form", "L Settings", None, -1))
        self.settings2Lab.setText(QtWidgets.QApplication.translate("Form", "R Settings", None, -1))
        self.settings3Lab.setText(QtWidgets.QApplication.translate("Form", "Settings III", None, -1))
        self.misc1Lab.setText(QtWidgets.QApplication.translate("Form", "Misc I", None, -1))
        self.misc2Lab.setText(QtWidgets.QApplication.translate("Form", "Misc II", None, -1))
        self.misc3Lab.setText(QtWidgets.QApplication.translate("Form", "Misc III", None, -1))
        self.locsBtn.setText(QtWidgets.QApplication.translate("Form", "Create Locators", None, -1))
        self.mirrorBtn.setText(QtWidgets.QApplication.translate("Form", "Mirror All Locators", None, -1))
        self.createBtn.setText(QtWidgets.QApplication.translate("Form", "Create Rig", None, -1))
        self.limbBox.setTitle(QtWidgets.QApplication.translate("Form", "Limbs", None, -1))
        self.clearEntries.setText(QtWidgets.QApplication.translate("Form", "Clear All", None, -1))
        self.newEntry.setText(QtWidgets.QApplication.translate("Form", "+", None, -1))
        self.nameBox.setTitle(QtWidgets.QApplication.translate("Form", "Name", None, -1))
        self.nameEdit.setPlaceholderText(QtWidgets.QApplication.translate("Form", "e.g. Biped", None, -1))
        self.nameLab.setText(QtWidgets.QApplication.translate("Form", "Rig Name", None, -1))
        self.scaleBox.setTitle(QtWidgets.QApplication.translate("Form", "Scale", None, -1))
        self.ctrlScaleLab.setText(QtWidgets.QApplication.translate("Form", "Controls", None, -1))
        self.locScaleLab.setText(QtWidgets.QApplication.translate("Form", "Locators", None, -1))
        self.locBox.setTitle(QtWidgets.QApplication.translate("Form", "Locators", None, -1))
        self.saveLocsBtn.setText(QtWidgets.QApplication.translate("Form", "Save json", None, -1))
        self.loadLocsBtn.setText(QtWidgets.QApplication.translate("Form", "Load json", None, -1))
        self.delLocsBtn.setText(QtWidgets.QApplication.translate("Form", "Delete", None, -1))
        self.settingsBox.setTitle(QtWidgets.QApplication.translate("Form", "General Settings", None, -1))
        self.biRad.setText(QtWidgets.QApplication.translate("Form", "Biped", None, -1))
        self.quadRad.setText(QtWidgets.QApplication.translate("Form", "Quadruped", None, -1))
        self.spineChkBox.setText(QtWidgets.QApplication.translate("Form", " Spine Joints", None, -1))
