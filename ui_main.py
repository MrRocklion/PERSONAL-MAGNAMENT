# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainSPBhtP.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(755, 449)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(244, 246, 247);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(712, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"background-color: rgb(46, 64, 83);\n"
"border-radius:10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(236, 240, 241);\n"
"font: 18pt \"Roboto\";")

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(60, 16777215))
        self.frame_4.setStyleSheet(u"background-color: rgb(46, 64, 83);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.dash_btn = QPushButton(self.frame_4)
        self.dash_btn.setObjectName(u"dash_btn")
        self.dash_btn.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	border-radius:0px;\n"
"	background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(133, 146, 158);\n"
"}\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u":/iconos/icons/dashboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dash_btn.setIcon(icon)
        self.dash_btn.setIconSize(QSize(34, 34))
        self.dash_btn.setFlat(False)

        self.verticalLayout_3.addWidget(self.dash_btn)

        self.report_btn = QPushButton(self.frame_4)
        self.report_btn.setObjectName(u"report_btn")
        self.report_btn.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	border-radius:0px;\n"
"	background-color: rgb(52, 73, 94);\n"
"}\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(133, 146, 158);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos/icons/document.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.report_btn.setIcon(icon1)
        self.report_btn.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.report_btn)

        self.config_btn = QPushButton(self.frame_4)
        self.config_btn.setObjectName(u"config_btn")
        self.config_btn.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	border-radius:0px;\n"
"	background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(133, 146, 158);\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/iconos/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.config_btn.setIcon(icon2)
        self.config_btn.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.config_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn = QPushButton(self.frame_4)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setStyleSheet(u"QPushButton:hover{\n"
"\n"
"	border-radius:0px;\n"
"	background-color: rgb(52, 73, 94);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(133, 146, 158);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/iconos/icons/logout.svg", QSize(), QIcon.Normal, QIcon.On)
        self.exit_btn.setIcon(icon3)
        self.exit_btn.setIconSize(QSize(34, 34))

        self.verticalLayout_3.addWidget(self.exit_btn)

        self.verticalSpacer_3 = QSpacerItem(5, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(1000, 385))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_5)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.DashBoardView = QWidget()
        self.DashBoardView.setObjectName(u"DashBoardView")
        self.horizontalLayout_4 = QHBoxLayout(self.DashBoardView)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.DashBoardView)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 130))
        self.frame_9.setStyleSheet(u"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setSpacing(9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMinimumSize(QSize(256, 110))
        self.frame_13.setStyleSheet(u"background-color: rgb(236, 240, 241);\n"
"border-radius:10px;\n"
"\n"
"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_13)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_5 = QLabel(self.frame_13)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)

        self.nameLabel = QLabel(self.frame_13)
        self.nameLabel.setObjectName(u"nameLabel")

        self.gridLayout.addWidget(self.nameLabel, 1, 1, 1, 1)

        self.lastnameLabel = QLabel(self.frame_13)
        self.lastnameLabel.setObjectName(u"lastnameLabel")

        self.gridLayout.addWidget(self.lastnameLabel, 2, 1, 1, 1)

        self.macLabel = QLabel(self.frame_13)
        self.macLabel.setObjectName(u"macLabel")

        self.gridLayout.addWidget(self.macLabel, 3, 1, 1, 1)

        self.label_4 = QLabel(self.frame_13)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Roboto Black"])
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setMinimumSize(QSize(400, 0))
        self.frame_14.setMaximumSize(QSize(1000, 110))
        self.frame_14.setStyleSheet(u"background-color: rgb(236, 240, 241);\n"
"border-radius:10px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.radSalida = QRadioButton(self.frame_14)
        self.radSalida.setObjectName(u"radSalida")

        self.gridLayout_2.addWidget(self.radSalida, 0, 1, 1, 1)

        self.comentario = QLineEdit(self.frame_14)
        self.comentario.setObjectName(u"comentario")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comentario.sizePolicy().hasHeightForWidth())
        self.comentario.setSizePolicy(sizePolicy1)
        self.comentario.setMinimumSize(QSize(0, 30))
        self.comentario.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:4px;")

        self.gridLayout_2.addWidget(self.comentario, 1, 1, 1, 1)

        self.radIngreso = QRadioButton(self.frame_14)
        self.radIngreso.setObjectName(u"radIngreso")
        self.radIngreso.setChecked(True)

        self.gridLayout_2.addWidget(self.radIngreso, 0, 0, 1, 1)

        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)

        self.registrar_btn = QPushButton(self.frame_14)
        self.registrar_btn.setObjectName(u"registrar_btn")
        self.registrar_btn.setMinimumSize(QSize(0, 30))
        self.registrar_btn.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(130, 224, 170);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	border-radius:0px;\n"
"	background-color: rgb(171, 235, 198);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(40, 180, 99);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"")

        self.gridLayout_2.addWidget(self.registrar_btn, 2, 1, 1, 1)


        self.horizontalLayout_10.addLayout(self.gridLayout_2)


        self.horizontalLayout_8.addWidget(self.frame_14)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(16777215, 241))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setSpacing(9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(328, 0))
        self.frame_11.setStyleSheet(u"background-color: rgb(236, 240, 241);\n"
"border-radius:10px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 9pt \"Roboto\";")

        self.verticalLayout_4.addWidget(self.label)

        self.tableIngresos = QTableWidget(self.frame_11)
        if (self.tableIngresos.columnCount() < 4):
            self.tableIngresos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableIngresos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableIngresos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableIngresos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableIngresos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableIngresos.rowCount() < 1):
            self.tableIngresos.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableIngresos.setVerticalHeaderItem(0, __qtablewidgetitem4)
        self.tableIngresos.setObjectName(u"tableIngresos")
        self.tableIngresos.setShowGrid(False)
        self.tableIngresos.setWordWrap(True)
        self.tableIngresos.setCornerButtonEnabled(True)
        self.tableIngresos.setColumnCount(4)
        self.tableIngresos.horizontalHeader().setCascadingSectionResizes(False)
        self.tableIngresos.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableIngresos.horizontalHeader().setStretchLastSection(True)
        self.tableIngresos.verticalHeader().setVisible(False)
        self.tableIngresos.verticalHeader().setHighlightSections(True)

        self.verticalLayout_4.addWidget(self.tableIngresos)


        self.horizontalLayout_7.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(328, 0))
        self.frame_12.setStyleSheet(u"background-color: rgb(236, 240, 241);\n"
"border-radius:10px;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.frame_12)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 9pt \"Roboto\";")

        self.verticalLayout_5.addWidget(self.label_2)

        self.tableSalidas = QTableWidget(self.frame_12)
        if (self.tableSalidas.columnCount() < 4):
            self.tableSalidas.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableSalidas.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableSalidas.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableSalidas.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableSalidas.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.tableSalidas.setObjectName(u"tableSalidas")
        self.tableSalidas.setShowGrid(False)
        self.tableSalidas.setWordWrap(True)
        self.tableSalidas.setCornerButtonEnabled(True)
        self.tableSalidas.setColumnCount(4)
        self.tableSalidas.horizontalHeader().setCascadingSectionResizes(False)
        self.tableSalidas.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableSalidas.horizontalHeader().setStretchLastSection(True)
        self.tableSalidas.verticalHeader().setVisible(False)
        self.tableSalidas.verticalHeader().setHighlightSections(True)

        self.verticalLayout_5.addWidget(self.tableSalidas)


        self.horizontalLayout_7.addWidget(self.frame_12)


        self.verticalLayout_2.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.DashBoardView)
        self.ConfigView = QWidget()
        self.ConfigView.setObjectName(u"ConfigView")
        self.horizontalLayout_5 = QHBoxLayout(self.ConfigView)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_7 = QFrame(self.ConfigView)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lastTxt = QLineEdit(self.frame_7)
        self.lastTxt.setObjectName(u"lastTxt")
        self.lastTxt.setMinimumSize(QSize(0, 30))
        self.lastTxt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:4px;")

        self.gridLayout_3.addWidget(self.lastTxt, 2, 1, 1, 1)

        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setFamilies([u"Roboto Black"])
        font1.setPointSize(15)
        self.label_12.setFont(font1)

        self.gridLayout_3.addWidget(self.label_12, 0, 1, 1, 1)

        self.btnNames = QPushButton(self.frame_7)
        self.btnNames.setObjectName(u"btnNames")
        self.btnNames.setMinimumSize(QSize(0, 40))
        self.btnNames.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(130, 224, 170);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	border-radius:0px;\n"
"	background-color: rgb(171, 235, 198);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(40, 180, 99);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"")

        self.gridLayout_3.addWidget(self.btnNames, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.nameTxt = QLineEdit(self.frame_7)
        self.nameTxt.setObjectName(u"nameTxt")
        self.nameTxt.setMinimumSize(QSize(0, 30))
        self.nameTxt.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border:1px solid;\n"
"border-radius:4px;")

        self.gridLayout_3.addWidget(self.nameTxt, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_14 = QLabel(self.frame_7)
        self.label_14.setObjectName(u"label_14")
        font2 = QFont()
        font2.setFamilies([u"Roboto Black"])
        font2.setPointSize(11)
        self.label_14.setFont(font2)

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_3)


        self.horizontalLayout_5.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.ConfigView)
        self.ReportView = QWidget()
        self.ReportView.setObjectName(u"ReportView")
        self.horizontalLayout_6 = QHBoxLayout(self.ReportView)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_8 = QFrame(self.ReportView)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_4 = QWidget(self.frame_8)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 0, 649, 341))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnExcel = QPushButton(self.gridLayoutWidget_4)
        self.btnExcel.setObjectName(u"btnExcel")
        self.btnExcel.setMinimumSize(QSize(180, 40))
        self.btnExcel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(130, 224, 170);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	border-radius:0px;\n"
"	background-color: rgb(171, 235, 198);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-radius:0px;\n"
"	background-color: rgb(40, 180, 99);\n"
"border-radius:3px;\n"
"color:white\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.btnExcel, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.ReportView)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Panel de Administracion", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Software de marcacion hitraffic", None))
        self.dash_btn.setText("")
        self.report_btn.setText("")
        self.config_btn.setText("")
        self.exit_btn.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Apellidos:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Mac:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nombres:", None))
        self.nameLabel.setText(QCoreApplication.translate("MainWindow", u"ir a configuraciones", None))
        self.lastnameLabel.setText(QCoreApplication.translate("MainWindow", u"ir a configuraciones", None))
        self.macLabel.setText(QCoreApplication.translate("MainWindow", u"ir a configuraciones", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Datos Personales", None))
        self.radSalida.setText(QCoreApplication.translate("MainWindow", u"Salida", None))
        self.radIngreso.setText(QCoreApplication.translate("MainWindow", u"Ingreso", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Comentario:    ", None))
        self.registrar_btn.setText(QCoreApplication.translate("MainWindow", u"REGISTRAR", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Marcaciones de Ingreso", None))
        ___qtablewidgetitem = self.tableIngresos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.tableIngresos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem2 = self.tableIngresos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem3 = self.tableIngresos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Comentario", None));
        ___qtablewidgetitem4 = self.tableIngresos.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Marcaciones de Salida", None))
        ___qtablewidgetitem5 = self.tableSalidas.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem6 = self.tableSalidas.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem7 = self.tableSalidas.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem8 = self.tableSalidas.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Comentario", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Configuracion de datos personales", None))
        self.btnNames.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Apellidos:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Nombres:", None))
        self.btnExcel.setText(QCoreApplication.translate("MainWindow", u"DESCARGAR REPORTE EXCEL", None))
    # retranslateUi

