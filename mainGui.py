# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(837, 785)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1341, 931))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 821, 281))
        self.groupBox.setObjectName("groupBox")
        self.Peb = QtWidgets.QLabel(self.groupBox)
        self.Peb.setGeometry(QtCore.QRect(280, 240, 51, 20))
        self.Peb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Peb.setText("")
        self.Peb.setObjectName("Peb")
        self.Am = QtWidgets.QLabel(self.groupBox)
        self.Am.setGeometry(QtCore.QRect(640, 200, 71, 20))
        self.Am.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Am.setText("")
        self.Am.setObjectName("Am")
        self.SPDA = QtWidgets.QComboBox(self.groupBox)
        self.SPDA.setGeometry(QtCore.QRect(10, 200, 251, 22))
        self.SPDA.setObjectName("SPDA")
        self.Cd = QtWidgets.QLabel(self.groupBox)
        self.Cd.setGeometry(QtCore.QRect(280, 160, 51, 20))
        self.Cd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cd.setText("")
        self.Cd.setObjectName("Cd")
        self.Pb = QtWidgets.QLabel(self.groupBox)
        self.Pb.setGeometry(QtCore.QRect(280, 200, 51, 20))
        self.Pb.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pb.setText("")
        self.Pb.setObjectName("Pb")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(10, 90, 256, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.calc_ks1 = QtWidgets.QPushButton(self.groupBox)
        self.calc_ks1.setGeometry(QtCore.QRect(330, 50, 75, 23))
        self.calc_ks1.setObjectName("calc_ks1")
        self.D = QtWidgets.QLineEdit(self.groupBox)
        self.D.setGeometry(QtCore.QRect(590, 120, 31, 20))
        self.D.setObjectName("D")
        self.Ng = QtWidgets.QLineEdit(self.groupBox)
        self.Ng.setGeometry(QtCore.QRect(140, 20, 51, 20))
        self.Ng.setObjectName("Ng")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(490, 30, 86, 20))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 121, 31))
        self.label_4.setObjectName("label_4")
        self.L = QtWidgets.QLineEdit(self.groupBox)
        self.L.setGeometry(QtCore.QRect(590, 30, 61, 20))
        self.L.setObjectName("L")
        self.W = QtWidgets.QLineEdit(self.groupBox)
        self.W.setGeometry(QtCore.QRect(590, 60, 61, 20))
        self.W.setObjectName("W")
        self.H = QtWidgets.QLineEdit(self.groupBox)
        self.H.setGeometry(QtCore.QRect(592, 90, 61, 20))
        self.H.setObjectName("H")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(520, 80, 52, 31))
        self.label_7.setObjectName("label_7")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(390, 200, 244, 20))
        self.label_13.setObjectName("label_13")
        self.w1m = QtWidgets.QLineEdit(self.groupBox)
        self.w1m.setGeometry(QtCore.QRect(130, 50, 61, 20))
        self.w1m.setObjectName("w1m")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(480, 170, 152, 20))
        self.label_12.setObjectName("label_12")
        self.fator_Loc = QtWidgets.QComboBox(self.groupBox)
        self.fator_Loc.setGeometry(QtCore.QRect(10, 160, 251, 22))
        self.fator_Loc.setObjectName("fator_Loc")
        self.Ks1 = QtWidgets.QLabel(self.groupBox)
        self.Ks1.setGeometry(QtCore.QRect(270, 50, 51, 20))
        self.Ks1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ks1.setText("")
        self.Ks1.setObjectName("Ks1")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(244, 50, 21, 20))
        self.label_15.setObjectName("label_15")
        self.calc_Ad = QtWidgets.QPushButton(self.groupBox)
        self.calc_Ad.setGeometry(QtCore.QRect(720, 170, 75, 23))
        self.calc_Ad.setObjectName("calc_Ad")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(510, 50, 60, 34))
        self.label_6.setObjectName("label_6")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 50, 107, 29))
        self.label_14.setObjectName("label_14")
        self.calc_Am = QtWidgets.QPushButton(self.groupBox)
        self.calc_Am.setGeometry(QtCore.QRect(720, 200, 75, 23))
        self.calc_Am.setObjectName("calc_Am")
        self.DPS = QtWidgets.QComboBox(self.groupBox)
        self.DPS.setGeometry(QtCore.QRect(10, 240, 251, 22))
        self.DPS.setObjectName("DPS")
        self.Ad = QtWidgets.QLabel(self.groupBox)
        self.Ad.setGeometry(QtCore.QRect(640, 170, 71, 20))
        self.Ad.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ad.setText("")
        self.Ad.setObjectName("Ad")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(560, 120, 20, 20))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 290, 821, 171))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 86, 20))
        self.label_8.setObjectName("label_8")
        self.L_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.L_2.setGeometry(QtCore.QRect(110, 30, 61, 20))
        self.L_2.setObjectName("L_2")
        self.fator_Inst = QtWidgets.QComboBox(self.groupBox_2)
        self.fator_Inst.setGeometry(QtCore.QRect(10, 60, 251, 22))
        self.fator_Inst.setObjectName("fator_Inst")
        self.Cl = QtWidgets.QLabel(self.groupBox_2)
        self.Cl.setGeometry(QtCore.QRect(280, 60, 51, 20))
        self.Cl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cl.setText("")
        self.Cl.setObjectName("Cl")
        self.Ct = QtWidgets.QLabel(self.groupBox_2)
        self.Ct.setGeometry(QtCore.QRect(280, 90, 51, 20))
        self.Ct.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ct.setText("")
        self.Ct.setObjectName("Ct")
        self.T_linha = QtWidgets.QComboBox(self.groupBox_2)
        self.T_linha.setGeometry(QtCore.QRect(10, 90, 251, 22))
        self.T_linha.setObjectName("T_linha")
        self.Ce = QtWidgets.QLabel(self.groupBox_2)
        self.Ce.setGeometry(QtCore.QRect(280, 120, 51, 20))
        self.Ce.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ce.setText("")
        self.Ce.setObjectName("Ce")
        self.fator_Amb = QtWidgets.QComboBox(self.groupBox_2)
        self.fator_Amb.setGeometry(QtCore.QRect(10, 120, 251, 22))
        self.fator_Amb.setObjectName("fator_Amb")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(356, 30, 121, 20))
        self.label_2.setObjectName("label_2")
        self.Uw = QtWidgets.QLineEdit(self.groupBox_2)
        self.Uw.setGeometry(QtCore.QRect(480, 30, 61, 20))
        self.Uw.setObjectName("Uw")
        self.Pld = QtWidgets.QLabel(self.groupBox_2)
        self.Pld.setGeometry(QtCore.QRect(630, 60, 51, 20))
        self.Pld.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pld.setText("")
        self.Pld.setObjectName("Pld")
        self.blin_lin = QtWidgets.QComboBox(self.groupBox_2)
        self.blin_lin.setGeometry(QtCore.QRect(360, 60, 251, 22))
        self.blin_lin.setObjectName("blin_lin")
        self.Cld = QtWidgets.QLabel(self.groupBox_2)
        self.Cld.setGeometry(QtCore.QRect(630, 90, 51, 20))
        self.Cld.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cld.setText("")
        self.Cld.setObjectName("Cld")
        self.BAI = QtWidgets.QComboBox(self.groupBox_2)
        self.BAI.setGeometry(QtCore.QRect(360, 90, 251, 22))
        self.BAI.setObjectName("BAI")
        self.tipLinha = QtWidgets.QComboBox(self.groupBox_2)
        self.tipLinha.setGeometry(QtCore.QRect(360, 120, 251, 22))
        self.tipLinha.setObjectName("tipLinha")
        self.Pli = QtWidgets.QLabel(self.groupBox_2)
        self.Pli.setGeometry(QtCore.QRect(630, 120, 51, 20))
        self.Pli.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pli.setText("")
        self.Pli.setObjectName("Pli")
        self.Cli = QtWidgets.QLabel(self.groupBox_2)
        self.Cli.setGeometry(QtCore.QRect(700, 90, 51, 20))
        self.Cli.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cli.setText("")
        self.Cli.setObjectName("Cli")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 460, 821, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        self.Cl_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Cl_2.setGeometry(QtCore.QRect(280, 60, 51, 20))
        self.Cl_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cl_2.setText("")
        self.Cl_2.setObjectName("Cl_2")
        self.Cld_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Cld_2.setGeometry(QtCore.QRect(630, 90, 51, 20))
        self.Cld_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cld_2.setText("")
        self.Cld_2.setObjectName("Cld_2")
        self.Cli_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Cli_2.setGeometry(QtCore.QRect(700, 90, 51, 20))
        self.Cli_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Cli_2.setText("")
        self.Cli_2.setObjectName("Cli_2")
        self.L_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.L_3.setGeometry(QtCore.QRect(110, 30, 61, 20))
        self.L_3.setObjectName("L_3")
        self.Ct_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Ct_2.setGeometry(QtCore.QRect(280, 90, 51, 20))
        self.Ct_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ct_2.setText("")
        self.Ct_2.setObjectName("Ct_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(356, 30, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 86, 20))
        self.label_9.setObjectName("label_9")
        self.T_linha_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.T_linha_2.setGeometry(QtCore.QRect(10, 90, 251, 22))
        self.T_linha_2.setObjectName("T_linha_2")
        self.fator_Amb_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.fator_Amb_2.setGeometry(QtCore.QRect(10, 120, 251, 22))
        self.fator_Amb_2.setObjectName("fator_Amb_2")
        self.BAI_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.BAI_2.setGeometry(QtCore.QRect(360, 90, 251, 22))
        self.BAI_2.setObjectName("BAI_2")
        self.Ce_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Ce_2.setGeometry(QtCore.QRect(280, 120, 51, 20))
        self.Ce_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Ce_2.setText("")
        self.Ce_2.setObjectName("Ce_2")
        self.blin_lin_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.blin_lin_2.setGeometry(QtCore.QRect(360, 60, 251, 22))
        self.blin_lin_2.setObjectName("blin_lin_2")
        self.fator_Inst_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.fator_Inst_2.setGeometry(QtCore.QRect(10, 60, 251, 22))
        self.fator_Inst_2.setObjectName("fator_Inst_2")
        self.Uw_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.Uw_2.setGeometry(QtCore.QRect(480, 30, 61, 20))
        self.Uw_2.setObjectName("Uw_2")
        self.Pld_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Pld_2.setGeometry(QtCore.QRect(630, 60, 51, 20))
        self.Pld_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pld_2.setText("")
        self.Pld_2.setObjectName("Pld_2")
        self.Pli_2 = QtWidgets.QLabel(self.groupBox_3)
        self.Pli_2.setGeometry(QtCore.QRect(630, 120, 51, 20))
        self.Pli_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Pli_2.setText("")
        self.Pli_2.setObjectName("Pli_2")
        self.tipLinha_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.tipLinha_2.setGeometry(QtCore.QRect(360, 120, 251, 22))
        self.tipLinha_2.setObjectName("tipLinha_2")
        self.calc_Nd = QtWidgets.QPushButton(self.groupBox_3)
        self.calc_Nd.setGeometry(QtCore.QRect(140, 170, 75, 23))
        self.calc_Nd.setObjectName("calc_Nd")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 170, 21, 16))
        self.label_10.setObjectName("label_10")
        self.Nd = QtWidgets.QLabel(self.groupBox_3)
        self.Nd.setGeometry(QtCore.QRect(40, 170, 91, 16))
        self.Nd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Nd.setText("")
        self.Nd.setObjectName("Nd")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Tpiso = QtWidgets.QComboBox(self.tab_2)
        self.Tpiso.setGeometry(QtCore.QRect(20, 51, 281, 31))
        self.Tpiso.setObjectName("Tpiso")
        self.rt = QtWidgets.QLabel(self.tab_2)
        self.rt.setGeometry(QtCore.QRect(310, 60, 51, 20))
        self.rt.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rt.setText("")
        self.rt.setObjectName("rt")
        self.medProE = QtWidgets.QComboBox(self.tab_2)
        self.medProE.setGeometry(QtCore.QRect(20, 90, 281, 22))
        self.medProE.setObjectName("medProE")
        self.pta = QtWidgets.QLabel(self.tab_2)
        self.pta.setGeometry(QtCore.QRect(310, 90, 51, 20))
        self.pta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pta.setText("")
        self.pta.setObjectName("pta")
        self.medProL = QtWidgets.QComboBox(self.tab_2)
        self.medProL.setGeometry(QtCore.QRect(20, 120, 281, 22))
        self.medProL.setObjectName("medProL")
        self.ptu = QtWidgets.QLabel(self.tab_2)
        self.ptu.setGeometry(QtCore.QRect(310, 120, 51, 20))
        self.ptu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ptu.setText("")
        self.ptu.setObjectName("ptu")
        self.provIn = QtWidgets.QComboBox(self.tab_2)
        self.provIn.setGeometry(QtCore.QRect(20, 150, 281, 22))
        self.provIn.setObjectName("provIn")
        self.rp = QtWidgets.QLabel(self.tab_2)
        self.rp.setGeometry(QtCore.QRect(310, 150, 51, 20))
        self.rp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rp.setText("")
        self.rp.setObjectName("rp")
        self.riscoInc = QtWidgets.QComboBox(self.tab_2)
        self.riscoInc.setGeometry(QtCore.QRect(20, 180, 281, 22))
        self.riscoInc.setObjectName("riscoInc")
        self.rf = QtWidgets.QLabel(self.tab_2)
        self.rf.setGeometry(QtCore.QRect(310, 180, 51, 20))
        self.rf.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rf.setText("")
        self.rf.setObjectName("rf")
        self.perigo_esp = QtWidgets.QComboBox(self.tab_2)
        self.perigo_esp.setGeometry(QtCore.QRect(410, 30, 271, 22))
        self.perigo_esp.setObjectName("perigo_esp")
        self.hz = QtWidgets.QLabel(self.tab_2)
        self.hz.setGeometry(QtCore.QRect(700, 30, 51, 20))
        self.hz.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hz.setText("")
        self.hz.setObjectName("hz")
        self.fiacao_en = QtWidgets.QComboBox(self.tab_2)
        self.fiacao_en.setGeometry(QtCore.QRect(410, 60, 271, 22))
        self.fiacao_en.setObjectName("fiacao_en")
        self.ks3 = QtWidgets.QLabel(self.tab_2)
        self.ks3.setGeometry(QtCore.QRect(700, 60, 51, 20))
        self.ks3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ks3.setText("")
        self.ks3.setObjectName("ks3")
        self.DPS_en = QtWidgets.QComboBox(self.tab_2)
        self.DPS_en.setGeometry(QtCore.QRect(410, 90, 271, 22))
        self.DPS_en.setObjectName("DPS_en")
        self.PSPD = QtWidgets.QLabel(self.tab_2)
        self.PSPD.setGeometry(QtCore.QRect(700, 90, 51, 20))
        self.PSPD.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PSPD.setText("")
        self.PSPD.setObjectName("PSPD")
        self.fiacao_tel = QtWidgets.QComboBox(self.tab_2)
        self.fiacao_tel.setGeometry(QtCore.QRect(410, 120, 271, 22))
        self.fiacao_tel.setObjectName("fiacao_tel")
        self.ks3_2 = QtWidgets.QLabel(self.tab_2)
        self.ks3_2.setGeometry(QtCore.QRect(700, 120, 51, 20))
        self.ks3_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ks3_2.setText("")
        self.ks3_2.setObjectName("ks3_2")
        self.DPS_tel = QtWidgets.QComboBox(self.tab_2)
        self.DPS_tel.setGeometry(QtCore.QRect(410, 150, 271, 22))
        self.DPS_tel.setObjectName("DPS_tel")
        self.PSPD_2 = QtWidgets.QLabel(self.tab_2)
        self.PSPD_2.setGeometry(QtCore.QRect(700, 150, 51, 20))
        self.PSPD_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PSPD_2.setText("")
        self.PSPD_2.setObjectName("PSPD_2")
        self.danos_fis = QtWidgets.QComboBox(self.tab_2)
        self.danos_fis.setGeometry(QtCore.QRect(410, 180, 271, 22))
        self.danos_fis.setObjectName("danos_fis")
        self.LF = QtWidgets.QLabel(self.tab_2)
        self.LF.setGeometry(QtCore.QRect(700, 180, 51, 20))
        self.LF.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LF.setText("")
        self.LF.setObjectName("LF")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(40, 20, 81, 21))
        self.label_11.setObjectName("label_11")
        self.Zona_nome = QtWidgets.QLineEdit(self.tab_2)
        self.Zona_nome.setGeometry(QtCore.QRect(140, 20, 113, 20))
        self.Zona_nome.setObjectName("Zona_nome")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(130, 300, 161, 21))
        self.label_16.setObjectName("label_16")
        self.ks2 = QtWidgets.QLabel(self.tab_2)
        self.ks2.setGeometry(QtCore.QRect(300, 300, 41, 21))
        self.ks2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ks2.setText("")
        self.ks2.setObjectName("ks2")
        self.Np = QtWidgets.QLineEdit(self.tab_2)
        self.Np.setGeometry(QtCore.QRect(300, 330, 41, 20))
        self.Np.setObjectName("Np")
        self.Npe = QtWidgets.QLineEdit(self.tab_2)
        self.Npe.setGeometry(QtCore.QRect(300, 360, 41, 20))
        self.Npe.setObjectName("Npe")
        self.deltaT = QtWidgets.QLineEdit(self.tab_2)
        self.deltaT.setGeometry(QtCore.QRect(300, 390, 41, 20))
        self.deltaT.setObjectName("deltaT")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(140, 330, 151, 21))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.tab_2)
        self.label_19.setGeometry(QtCore.QRect(130, 360, 161, 21))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(30, 390, 261, 21))
        self.label_20.setObjectName("label_20")
        self.Calc_ks2 = QtWidgets.QPushButton(self.tab_2)
        self.Calc_ks2.setGeometry(QtCore.QRect(350, 300, 75, 23))
        self.Calc_ks2.setObjectName("Calc_ks2")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(490, 260, 141, 21))
        self.label_21.setObjectName("label_21")
        self.Fp = QtWidgets.QLabel(self.tab_2)
        self.Fp.setGeometry(QtCore.QRect(640, 260, 41, 21))
        self.Fp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Fp.setText("")
        self.Fp.setObjectName("Fp")
        self.Calc_Fp = QtWidgets.QPushButton(self.tab_2)
        self.Calc_Fp.setGeometry(QtCore.QRect(690, 260, 75, 23))
        self.Calc_Fp.setObjectName("Calc_Fp")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(510, 300, 121, 21))
        self.label_22.setObjectName("label_22")
        self.LA = QtWidgets.QLabel(self.tab_2)
        self.LA.setGeometry(QtCore.QRect(640, 300, 71, 21))
        self.LA.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LA.setText("")
        self.LA.setObjectName("LA")
        self.LU = QtWidgets.QLabel(self.tab_2)
        self.LU.setGeometry(QtCore.QRect(640, 330, 41, 21))
        self.LU.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LU.setText("")
        self.LU.setObjectName("LU")
        self.LB = QtWidgets.QLabel(self.tab_2)
        self.LB.setGeometry(QtCore.QRect(640, 360, 41, 21))
        self.LB.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LB.setText("")
        self.LB.setObjectName("LB")
        self.LV = QtWidgets.QLabel(self.tab_2)
        self.LV.setGeometry(QtCore.QRect(640, 390, 41, 21))
        self.LV.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LV.setText("")
        self.LV.setObjectName("LV")
        self.Calc_res = QtWidgets.QPushButton(self.tab_2)
        self.Calc_res.setGeometry(QtCore.QRect(530, 330, 75, 23))
        self.Calc_res.setObjectName("Calc_res")
        self.label_23 = QtWidgets.QLabel(self.tab_2)
        self.label_23.setGeometry(QtCore.QRect(720, 300, 31, 21))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(700, 330, 31, 21))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(700, 360, 31, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(700, 390, 31, 21))
        self.label_26.setObjectName("label_26")
        self.checkEx = QtWidgets.QCheckBox(self.tab_2)
        self.checkEx.setGeometry(QtCore.QRect(30, 240, 70, 17))
        self.checkEx.setObjectName("checkEx")
        self.checkIn = QtWidgets.QCheckBox(self.tab_2)
        self.checkIn.setGeometry(QtCore.QRect(130, 240, 70, 17))
        self.checkIn.setObjectName("checkIn")
        self.checkEI = QtWidgets.QCheckBox(self.tab_2)
        self.checkEI.setGeometry(QtCore.QRect(230, 240, 121, 17))
        self.checkEI.setObjectName("checkEI")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(30, 220, 47, 13))
        self.label_17.setObjectName("label_17")
        self.LO = QtWidgets.QLabel(self.tab_2)
        self.LO.setGeometry(QtCore.QRect(700, 210, 51, 20))
        self.LO.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LO.setText("")
        self.LO.setObjectName("LO")
        self.falhas_sis = QtWidgets.QComboBox(self.tab_2)
        self.falhas_sis.setGeometry(QtCore.QRect(410, 210, 271, 22))
        self.falhas_sis.setObjectName("falhas_sis")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 837, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuSPDA = QtWidgets.QMenu(self.menuBar)
        self.menuSPDA.setObjectName("menuSPDA")
        self.menuSobre = QtWidgets.QMenu(self.menuBar)
        self.menuSobre.setObjectName("menuSobre")
        self.menuEmitir = QtWidgets.QMenu(self.menuBar)
        self.menuEmitir.setObjectName("menuEmitir")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionRelat_rio_Parcial = QtWidgets.QAction(MainWindow)
        self.actionRelat_rio_Parcial.setObjectName("actionRelat_rio_Parcial")
        self.actionRelat_rio_Final = QtWidgets.QAction(MainWindow)
        self.actionRelat_rio_Final.setShortcut("")
        self.actionRelat_rio_Final.setObjectName("actionRelat_rio_Final")
        self.menuSPDA.addAction(self.actionNew)
        self.menuSPDA.addAction(self.actionOpen)
        self.menuEmitir.addAction(self.actionRelat_rio_Parcial)
        self.menuEmitir.addSeparator()
        self.menuEmitir.addAction(self.actionRelat_rio_Final)
        self.menuBar.addAction(self.menuSPDA.menuAction())
        self.menuBar.addAction(self.menuSobre.menuAction())
        self.menuBar.addAction(self.menuEmitir.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.H, self.SPDA)
        MainWindow.setTabOrder(self.SPDA, self.DPS)
        MainWindow.setTabOrder(self.DPS, self.w1m)
        MainWindow.setTabOrder(self.w1m, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.W)
        MainWindow.setTabOrder(self.W, self.L)
        MainWindow.setTabOrder(self.L, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.fator_Loc)
        MainWindow.setTabOrder(self.fator_Loc, self.L_3)
        MainWindow.setTabOrder(self.L_3, self.T_linha_2)
        MainWindow.setTabOrder(self.T_linha_2, self.fator_Amb_2)
        MainWindow.setTabOrder(self.fator_Amb_2, self.BAI_2)
        MainWindow.setTabOrder(self.BAI_2, self.blin_lin_2)
        MainWindow.setTabOrder(self.blin_lin_2, self.fator_Inst_2)
        MainWindow.setTabOrder(self.fator_Inst_2, self.Uw_2)
        MainWindow.setTabOrder(self.Uw_2, self.tipLinha_2)
        MainWindow.setTabOrder(self.tipLinha_2, self.calc_Nd)
        MainWindow.setTabOrder(self.calc_Nd, self.L_2)
        MainWindow.setTabOrder(self.L_2, self.fator_Inst)
        MainWindow.setTabOrder(self.fator_Inst, self.T_linha)
        MainWindow.setTabOrder(self.T_linha, self.fator_Amb)
        MainWindow.setTabOrder(self.fator_Amb, self.Uw)
        MainWindow.setTabOrder(self.Uw, self.blin_lin)
        MainWindow.setTabOrder(self.blin_lin, self.BAI)
        MainWindow.setTabOrder(self.BAI, self.tipLinha)
        MainWindow.setTabOrder(self.tipLinha, self.calc_ks1)
        MainWindow.setTabOrder(self.calc_ks1, self.D)
        MainWindow.setTabOrder(self.D, self.calc_Ad)
        MainWindow.setTabOrder(self.calc_Ad, self.calc_Am)
        MainWindow.setTabOrder(self.calc_Am, self.Tpiso)
        MainWindow.setTabOrder(self.Tpiso, self.medProE)
        MainWindow.setTabOrder(self.medProE, self.medProL)
        MainWindow.setTabOrder(self.medProL, self.provIn)
        MainWindow.setTabOrder(self.provIn, self.riscoInc)
        MainWindow.setTabOrder(self.riscoInc, self.perigo_esp)
        MainWindow.setTabOrder(self.perigo_esp, self.fiacao_en)
        MainWindow.setTabOrder(self.fiacao_en, self.DPS_en)
        MainWindow.setTabOrder(self.DPS_en, self.Ng)
        MainWindow.setTabOrder(self.Ng, self.fiacao_tel)
        MainWindow.setTabOrder(self.fiacao_tel, self.DPS_tel)
        MainWindow.setTabOrder(self.DPS_tel, self.danos_fis)
        MainWindow.setTabOrder(self.danos_fis, self.Zona_nome)
        MainWindow.setTabOrder(self.Zona_nome, self.Np)
        MainWindow.setTabOrder(self.Np, self.Npe)
        MainWindow.setTabOrder(self.Npe, self.deltaT)
        MainWindow.setTabOrder(self.deltaT, self.Calc_ks2)
        MainWindow.setTabOrder(self.Calc_ks2, self.Calc_Fp)
        MainWindow.setTabOrder(self.Calc_Fp, self.Calc_res)
        MainWindow.setTabOrder(self.Calc_res, self.checkEx)
        MainWindow.setTabOrder(self.checkEx, self.checkIn)
        MainWindow.setTabOrder(self.checkIn, self.checkEI)
        MainWindow.setTabOrder(self.checkEI, self.falhas_sis)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPDA"))
        self.groupBox.setTitle(_translate("MainWindow", "Estrutura e Meio Ambiente"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Para blindagens metálicas contínuas com espessura não inferior a 0,1 mm, KS1 = KS2 = 10–4</p></body></html>"))
        self.calc_ks1.setText(_translate("MainWindow", "Calcular"))
        self.label_5.setText(_translate("MainWindow", "Comprimento (m):"))
        self.label_4.setText(_translate("MainWindow", "Densidade de descargas:"))
        self.label_7.setText(_translate("MainWindow", "Altura (m):"))
        self.label_13.setText(_translate("MainWindow", "Área de exposição equivalente perto da estrutura:"))
        self.label_12.setText(_translate("MainWindow", "Área de exposição equivalente:"))
        self.label_15.setText(_translate("MainWindow", "Ks1:"))
        self.calc_Ad.setText(_translate("MainWindow", "Calcular"))
        self.label_6.setText(_translate("MainWindow", "Largura (m):"))
        self.label_14.setText(_translate("MainWindow", "Largura da blindagem:"))
        self.calc_Am.setText(_translate("MainWindow", "Calcular"))
        self.label.setText(_translate("MainWindow", "D:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Linha de Energia"))
        self.label_8.setText(_translate("MainWindow", "Comprimento (m):"))
        self.label_2.setText(_translate("MainWindow", "Tensão suportável Uw:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Linha de Sinal"))
        self.label_3.setText(_translate("MainWindow", "Tensão suportável Uw:"))
        self.label_9.setText(_translate("MainWindow", "Comprimento (m):"))
        self.calc_Nd.setText(_translate("MainWindow", "Calcular"))
        self.label_10.setText(_translate("MainWindow", "Nd:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Características Estruturais"))
        self.label_11.setText(_translate("MainWindow", "Nome da Zona:"))
        self.label_16.setText(_translate("MainWindow", "Blindagem espacial interna (Ks2):"))
        self.label_18.setText(_translate("MainWindow", "Número de pessoas na zona:"))
        self.label_19.setText(_translate("MainWindow", "Número de pessoas na estrutura:"))
        self.label_20.setText(_translate("MainWindow", "Período de tempo de ocupação com pessoas (h/ano):"))
        self.Calc_ks2.setText(_translate("MainWindow", "Calcular"))
        self.label_21.setText(_translate("MainWindow", "Fator para pessoas na zona:"))
        self.Calc_Fp.setText(_translate("MainWindow", "Calcular"))
        self.label_22.setText(_translate("MainWindow", "Parâmetros resultantes:"))
        self.Calc_res.setText(_translate("MainWindow", "Calcular"))
        self.label_23.setText(_translate("MainWindow", "LA"))
        self.label_24.setText(_translate("MainWindow", "LU"))
        self.label_25.setText(_translate("MainWindow", "LB"))
        self.label_26.setText(_translate("MainWindow", "LV"))
        self.checkEx.setText(_translate("MainWindow", "Explosão"))
        self.checkIn.setText(_translate("MainWindow", "Incêndio"))
        self.checkEI.setText(_translate("MainWindow", "Explosão e Incêndio"))
        self.label_17.setText(_translate("MainWindow", "Risco:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Zona 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Cálculos Zona 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Resumo"))
        self.menuSPDA.setTitle(_translate("MainWindow", "File"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.menuEmitir.setTitle(_translate("MainWindow", "Emitir"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionRelat_rio_Parcial.setText(_translate("MainWindow", "Relatório Parcial"))
        self.actionRelat_rio_Final.setText(_translate("MainWindow", "Relatório Final"))

