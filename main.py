from PyQt5.QtCore import  *
from PyQt5.QtWidgets import  *
from mainGui import Ui_MainWindow
import sys
import math
from xlrd import open_workbook
import csv


class SPDA(QMainWindow):
    Pvsinal = pyqtSignal(int)
    dicionario = {}
    def __init__(self):
        self.prontoPv=[False , False , False]
        self.LT=0.01
        self.NDJ = 0
        super(SPDA, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.Zona_nome.editingFinished.connect(self.salvar_zona)
        self.ui.Np.editingFinished.connect(self.salvar_np)
        self.ui.Npe.editingFinished.connect(self.salvar_npe)
        self.ui.deltaT.editingFinished.connect(self.salvar_deltat)
        self.ui.Ng.editingFinished.connect(self.salvar_Ng)
        self.ui.Uw.editingFinished.connect(self.salvar_Uw)
        self.ui.Uw_2.editingFinished.connect(self.salvar_Uw_2)
        self.ui.w1m.editingFinished.connect(self.salvar_w1m)
        self.ui.L.editingFinished.connect(self.salvar_L)
        self.ui.L_2.editingFinished.connect(self.salvar_L_2)
        self.ui.L_3.editingFinished.connect(self.salvar_L_3)
        self.ui.W.editingFinished.connect(self.salvar_W)
        self.ui.H.editingFinished.connect(self.salvar_H)
        self.ui.D.editingFinished.connect(self.salvar_D)
        self.ui.fator_Loc.activated.connect(self.setValue__Loc)
        self.ui.fator_Inst.activated.connect(self.setValue_Inst)
        self.ui.fator_Amb.activated.connect(self.setValue_famb)
        self.ui.T_linha.activated.connect(self.setValue_tlinha)
        self.ui.fator_Inst_2.activated.connect(self.setValue_Inst_2)
        self.ui.fator_Amb_2.activated.connect(self.setValue_famb_2)
        self.ui.T_linha_2.activated.connect(self.setValue_tlinha_2)
        self.ui.SPDA.activated.connect(self.setValue_SPDA)
        self.ui.DPS.activated.connect(self.setValue_DPS)
        self.ui.blin_lin.activated.connect(self.setValue_blinlin)
        self.ui.BAI.activated.connect(self.setValue_BAI)
        self.ui.tipLinha.activated.connect(self.setValue_tipLinha)
        self.ui.blin_lin_2.activated.connect(self.setValue_blinlin_2)
        self.ui.BAI_2.activated.connect(self.setValue_BAI_2)
        self.ui.tipLinha_2.activated.connect(self.setValue_tipLinha_2)
        self.ui.Tpiso.activated.connect(self.setValue_tpiso)
        self.ui.medProE.activated.connect(self.setValue_medpe)
        self.ui.medProL.activated.connect(self.setValue_medpl)
        self.ui.provIn.activated.connect(self.setValue_provin)
        self.ui.riscoInc.activated.connect(self.setValue_risco)
        self.ui.perigo_esp.activated.connect(self.setValue_perigo)
        self.ui.fiacao_en.activated.connect(self.setValue_fiaen)
        self.ui.DPS_en.activated.connect(self.setValue_dpsen)
        self.ui.fiacao_tel.activated.connect(self.setValue_fiatel)
        self.ui.DPS_tel.activated.connect(self.setValue_dpstel)
        self.ui.danos_fis.activated.connect(self.setValue_danos)
        self.ui.falhas_sis.activated.connect(self.setValue_falhas)
        self.ui.Ng.setToolTip("(1/km2/ano)")
        self.ui.calc_Ad.setToolTip("Requer todas as dimensões da estrutura")
        self.ui.calc_Am.setToolTip("Requer dimensões da estrutura e distância D")
        self.ui.calc_ks1.setToolTip("Requer largura da blindagem")
        self.ui.calc_Nd.setToolTip("Requer densidade de descargas, área de exposição e fator de localização")
        self.ui.D.setToolTip("Distância de uma linha ao perímetro da estrutura")
        self.ui.Calc_Fp.setToolTip("Requer número de pessoas na zona e na estrutura e tempo de ocupação")
        self.ui.calc_Nd.clicked.connect(self.calcularNd)
        self.ui.Calc_res.clicked.connect(self.calculares)
        self.ui.calc_Ad.clicked.connect(self.calcularAd)
        self.ui.calc_Am.clicked.connect(self.calcularAm)
        self.ui.calc_ks1.clicked.connect(self.calcularKs1)
        self.ui.Calc_Fp.clicked.connect(self.calcularFp)
        #self.ui.Calc_ris.clicked.connect(self.calcularis)
        self.Pvsinal.connect(self.calcularPv)
        self.ler_arquivo('localizacao_relativa.xlsx')

    def setValue_blinlin(self):
        try:
            self.ui.blin_lin.setToolTip(self.ui.blin_lin.currentText())
            if self.Uw == 1:
                self.ui.Pld.setText(str(self.dicionario[self.ui.blin_lin.currentText()][0]))
            elif self.Uw==1.5:
                self.ui.Pld.setText(str(self.dicionario[self.ui.blin_lin.currentText()][1]))
            elif self.Uw==2.5:
                self.ui.Pld.setText(str(self.dicionario[self.ui.blin_lin.currentText()][2]))
            elif self.Uw==4:
                self.ui.Pld.setText(str(self.dicionario[self.ui.blin_lin.currentText()][3]))
            elif self.Uw==6:
                self.ui.Pld.setText(str(self.dicionario[self.ui.blin_lin.currentText()][4]))
            else:
                self.ui.Pld.setText("Invalid")

        except:
            pass

    def setValue_blinlin_2(self):
        try:
            self.ui.blin_lin_2.setToolTip(self.ui.blin_lin_2.currentText())
            if self.Uw == 1:
                self.ui.Pld_2.setText(str(self.dicionario[self.ui.blin_lin_2.currentText()][0]))
            elif self.Uw==1.5:
                self.ui.Pld_2.setText(str(self.dicionario[self.ui.blin_lin_2.currentText()][1]))
            elif self.Uw==2.5:
                self.ui.Pld_2.setText(str(self.dicionario[self.ui.blin_lin_2.currentText()][2]))
            elif self.Uw==4:
                self.ui.Pld_2.setText(str(self.dicionario[self.ui.blin_lin_2.currentText()][3]))
            elif self.Uw==6:
                self.ui.Pld_2.setText(str(self.dicionario[self.ui.blin_lin_2.currentText()][4]))
            else:
                self.ui.Pld_2.setText("Invalid")

        except:
            pass

    def setValue_tlinha(self):
        self.ui.T_linha.setToolTip(self.ui.T_linha.currentText())
        self.ui.Ct.setText(str(self.dicionario[self.ui.T_linha.currentText()][0]))

    def setValue_tlinha_2(self):
        self.ui.T_linha_2.setToolTip(self.ui.T_linha_2.currentText())
        self.ui.Ct_2.setText(str(self.dicionario[self.ui.T_linha_2.currentText()][0]))

    def setValue_BAI(self):
        try:
            self.ui.BAI.setToolTip(self.ui.BAI.currentText())
            self.ui.Cld.setText(str(self.dicionario[self.ui.BAI.currentText()][0]))
            self.ui.Cli.setText(str(self.dicionario[self.ui.BAI.currentText()][1]))
        except:
            pass

    def setValue_BAI_2(self):
        try:
            self.ui.BAI_2.setToolTip(self.ui.BAI_2.currentText())
            self.ui.Cld_2.setText(str(self.dicionario[self.ui.BAI_2.currentText()][0]))
            self.ui.Cli_2.setText(str(self.dicionario[self.ui.BAI_2.currentText()][1]))
        except:
            pass

    def setValue_tipLinha(self):
        try:
            self.ui.tipLinha.setToolTip(self.ui.tipLinha.currentText())
            if self.Uw == 1:
                self.ui.Pli.setText(str(self.dicionario[self.ui.tipLinha.currentText()][0]))
            elif self.Uw == 1.5:
                self.ui.Pli.setText(str(self.dicionario[self.ui.tipLinha.currentText()][1]))
            elif self.Uw == 2.5:
                self.ui.Pli.setText(str(self.dicionario[self.ui.tipLinha.currentText()][2]))
            elif self.Uw == 4:
                self.ui.Pli.setText(str(self.dicionario[self.ui.tipLinha.currentText()][3]))
            elif self.Uw == 6:
                self.ui.Pli.setText(str(self.dicionario[self.ui.tipLinha.currentText()][4]))
            else:
                self.ui.Pli.setText("Invalid")
        except:
            pass
    def setValue_tipLinha_2(self):
        try:
            self.ui.tipLinha_2.setToolTip(self.ui.tipLinha_2.currentText())
            if self.Uw == 1:
                self.ui.Pli_2.setText(str(self.dicionario[self.ui.tipLinha_2.currentText()][0]))
            elif self.Uw == 1.5:
                self.ui.Pli_2.setText(str(self.dicionario[self.ui.tipLinha_2.currentText()][1]))
            elif self.Uw == 2.5:
                self.ui.Pli_2.setText(str(self.dicionario[self.ui.tipLinha_2.currentText()][2]))
            elif self.Uw == 4:
                self.ui.Pli_2.setText(str(self.dicionario[self.ui.tipLinha_2.currentText()][3]))
            elif self.Uw == 6:
                self.ui.Pli_2.setText(str(self.dicionario[self.ui.tipLinha_2.currentText()][4]))
            else:
                self.ui.Pli_2.setText("Invalid")
        except:
            pass

    def setValue_famb(self):
        self.ui.fator_Amb.setToolTip(self.ui.fator_Amb.currentText())
        self.ui.Ce.setText(str(self.dicionario[self.ui.fator_Amb.currentText()][0]))

    def setValue_famb_2(self):
        self.ui.fator_Amb_2.setToolTip(self.ui.fator_Amb_2.currentText())
        self.ui.Ce_2.setText(str(self.dicionario[self.ui.fator_Amb_2.currentText()][0]))

    def setValue__Loc(self):
        try:
            self.ui.fator_Loc.setToolTip(self.ui.fator_Loc.currentText())
            self.Cd = self.dicionario[self.ui.fator_Loc.currentText()][0]
            self.ui.Cd.setText(str(self.Cd))
        except:
            pass
    def setValue_SPDA(self):
        self.ui.SPDA.setToolTip(self.ui.SPDA.currentText())
        self.Pb = self.dicionario[self.ui.SPDA.currentText()][0]
        self.ui.Pb.setText(str(self.dicionario[self.ui.SPDA.currentText()][0]))

    def setValue_DPS(self):
        self.ui.DPS.setToolTip(self.ui.DPS.currentText())
        self.Peb = self.dicionario[self.ui.DPS.currentText()][0]
        self.prontoPv[0] = True
        cont = 0
        for elem in self.prontoPv:
            if elem:
                cont += 1
        if cont == 3:
            self.Pvsinal.emit(1)

        self.ui.Peb.setText(str(self.Peb))

    def setValue_Inst(self):
        self.ui.fator_Inst.setToolTip(self.ui.fator_Inst.currentText())
        self.ui.Cl.setText(str(self.dicionario[self.ui.fator_Inst.currentText()][0]))

    def setValue_Inst_2(self):
        self.ui.fator_Inst_2.setToolTip(self.ui.fator_Inst_2.currentText())
        self.ui.Cl_2.setText(str(self.dicionario[self.ui.fator_Inst_2.currentText()][0]))

    def setValue_tpiso(self):
        self.ui.Tpiso.setToolTip(self.ui.Tpiso.currentText())
        self.rt=self.dicionario[self.ui.Tpiso.currentText()][0]
        self.ui.rt.setText(str(self.dicionario[self.ui.Tpiso.currentText()][0]))

    def setValue_medpe(self):
        self.ui.medProE.setToolTip(self.ui.medProE.currentText())
        self.ui.pta.setText(str(self.dicionario[self.ui.medProE.currentText()][0]))

    def setValue_medpl(self):
        self.ui.medProL.setToolTip(self.ui.medProL.currentText())
        self.ui.ptu.setText(str(self.dicionario[self.ui.medProL.currentText()][0]))

    def setValue_provin(self):
        self.ui.provIn.setToolTip(self.ui.provIn.currentText())
        self.rp = self.dicionario[self.ui.provIn.currentText()][0]
        self.ui.rp.setText(str(self.dicionario[self.ui.provIn.currentText()][0]))

    def setValue_risco(self):
        self.ui.riscoInc.setToolTip(self.ui.riscoInc.currentText())
        self.rf = self.dicionario[self.ui.riscoInc.currentText()][0]
        self.ui.rf.setText(str(self.dicionario[self.ui.riscoInc.currentText()][0]))

    def setValue_perigo(self):
        self.ui.perigo_esp.setToolTip(self.ui.perigo_esp.currentText())
        self.hz=self.dicionario[self.ui.perigo_esp.currentText()][0]
        self.ui.hz.setText(str(self.dicionario[self.ui.perigo_esp.currentText()][0]))
    def setValue_fiaen(self):
        self.ui.fiacao_en.setToolTip(self.ui.fiacao_en.currentText())
        self.ui.ks3.setText(str(self.dicionario[self.ui.fiacao_en.currentText()][0]))

    def setValue_dpsen(self):
        self.ui.DPS_en.setToolTip(self.ui.DPS_en.currentText())
        self.ui.PSPD.setText(str(self.dicionario[self.ui.DPS_en.currentText()][0]))

    def setValue_fiatel(self):
        self.ui.fiacao_tel.setToolTip(self.ui.fiacao_tel.currentText())
        self.ui.ks3_2.setText(str(self.dicionario[self.ui.fiacao_tel.currentText()][0]))

    def setValue_dpstel(self):
        self.ui.DPS_tel.setToolTip(self.ui.DPS_tel.currentText())
        self.ui.PSPD_2.setText(str(self.dicionario[self.ui.DPS_tel.currentText()][0]))

    def setValue_danos(self):
        self.ui.danos_fis.setToolTip(self.ui.danos_fis.currentText())
        self. LF = self.dicionario[self.ui.danos_fis.currentText()][0]
        self.ui.LF.setText(str(self.dicionario[self.ui.danos_fis.currentText()][0]))
    def setValue_falhas(self):
        self.ui.falhas_sis.setToolTip(self.ui.falhas_sis.currentText())
        self.LO = self.dicionario[self.ui.falhas_sis.currentText()][0]
        self.ui.LO.setText(str(self.dicionario[self.ui.falhas_sis.currentText()][0]))

    def salvar_zona(self):
        try:
            self.zona = self.ui.Zona_nome.text()
        except:
            pass

    def salvar_np(self):
        try:
            self.np = float(self.ui.Np.text())
        except:
            pass

    def salvar_npe(self):
        try:
            self.npe = int(self.ui.Npe.text())
        except:
            pass

    def salvar_deltat(self):
        try:
            self.deltat = float(self.ui.deltaT.text())
        except:
            pass

    def salvar_Uw(self):
        try:
            self.Uw = float(self.ui.Uw.text())
            self.ks4 = 1 / self.Uw
        except:
            pass

    def salvar_Uw_2(self):
        try:
            self.Uw_2 = float(self.ui.Uw_2.text())
            self.ks4_2 = 1 / self.Uw_2
        except:
            pass

    def salvar_L_3(self):
        try:
            self.L_3 = float(self.ui.L_3.text())
        except:
            pass

    def salvar_L_2(self):
        try:
            self.L_2 = float(self.ui.L_2.text())
        except:
            pass

    def salvar_w1m(self):
        try:
            self.w1m = float(self.ui.w1m.text())
        except:
            pass
    def salvar_Ng(self):
        try:
            self.Ng = float(self.ui.Ng.text())
        except:
            pass
    def salvar_D(self):
        try:
            self.D = float(self.ui.D.text())
        except:
            pass

    def calcularNd(self):
        try:
            self.Nd= self.Cd * self.Ng * self.Ad * 0.000001
            self.ui.Nd.setText('{:.6f}'.format(self.Nd))
        except:
            pass

    def calcularPv(self):
        try:
            self.Pv = self.Peb * self.Cld * self.Pld
        except:
            pass

    def calcularAm(self):
        try:
            Am = 2 * self.D * (self.L + self.W) + math.pi * self.D ** 2
            self.ui.Am.setText('{0:.2f}'.format(Am))
        except:
            pass

    def calcularKs1(self):
        try:
            Ks1 = 0.12 * self.w1m
            self.ui.Ks1.setText('{0:.2f}'.format(Ks1))
        except:
            pass

    def calcularFp(self):
        try:
            self.Fp = (self.np/self.npe)*(self.deltat/8760)
            self.ui.Fp.setText('{0:.3f}'.format(self.Fp))
        except:
            pass

    def calcularis(self):
        try:
            self.ui.Nd_2.setText('{:.6f}'.format(self.Nd))
            self.PA = self.pta * self.Pb
            self.PC = self.PSPD * self.Cld
            self.PMS = (self.Ks1 * self.Ks2 * self.Ks3 * self.Ks4)**2
            self.PM = self.PSPD *self.PMS
            self.PV = self.Peb * self.Cld * self.Pld
            self.PW = self.Cld*self.PSPD*self.Pld
            self.PZ = self.Cli*self.PSPD*self.Pli
            self.NL = self.NG * self.Cl * self.Ce*self.Ct*40*self.L_2*0.000001
            self.RU = (self.NL + self.NDJ)*self.PU * self.LU
            self.NM = self.NG * self.L_2 *4000 * self.Cl * self.Ct * self.Ce *0.000001


            self.ui.PA.setText(self.PA)
            self.ui.PC.setText(self.PC)
            self.ui.PMS.setText(self.PMS)
            self.ui.PM.setText(self.PM)
            self.ui.PV.setText(self.PV)
            self.ui.PW.setText(self.PW)
            self.ui.PZ.setText(self.PZ)
            self.ui.NL.setText(self.NL)
            self.ui.RU.setText(self.RU)
            self.ui.NM.setText(self.NM)

        except:
            pass

    def calculares(self):
        try:
            self.LA = self.rt * self.LT * self.Fp
            self.ui.LA.setText(str(self.LA))
            self.LU = self.LA
            self.ui.LU.setText(str(self.LU))
            self.LB = self.rp * self.rf * self.hz * self.LF * self.Fp
            self.ui.LB.setText(str(self.LB))
            self.LV = self.LO * self.Fp
            self.ui.LV.setText(str(self.LV))
        except:
            pass

    def salvar_L(self):
        try:
            self.L = float(self.ui.L.text())
            """
            self.preenchido[0]= True
            cont = 0
            for elem in self.preenchido:
                if elem:
                    cont+=1
            if c                  233:
                self.Ad.emit(1) """
        except:
            pass
    def salvar_W(self):
        try:
            self.W = float(self.ui.W.text())
            """self.preenchido[1]=True
            cont = 0
            for elem in self.preenchido:
                if elem:
                    cont += 1
            if cont == 3:
                self.Ad.emit(1)"""
        except:
            pass
    def salvar_H(self):
        try:
            self.H = float(self.ui.H.text())
            """self.preenchido[2] = True
            cont = 0
            for elem in self.preenchido:
                if elem:
                    cont += 1
            if cont == 3:
                self.Ad.emit(1)"""
        except:
            pass
    def calcularAd(self):
        try:
            self.Ad = self.L*self.W + 6*self.H* (self.L+self.W)+ math.pi *(3*self.H)**2
            self.ui.Ad.setText('{0:.2f}'.format(self.Ad))
        except:
            pass

    def ler_arquivo(self, nome):
        cont = 0
        with open_workbook(nome) as wb:
            for planilha in wb.sheets():
                linhas = planilha.nrows
                colunas = planilha.ncols
                for i in range(linhas):
                    valor = []
                    for j in range(colunas):
                        if j == 0:
                            nome = planilha.cell(i, j).value
                            if cont == 0:
                                self.ui.fator_Loc.addItem(nome)
                            elif cont == 1:
                                self.ui.SPDA.addItem(nome)
                            elif cont == 2:
                                self.ui.DPS.addItem(nome)
                                self.ui.DPS_en.addItem(nome)
                                self.ui.DPS_tel.addItem(nome)
                            elif cont == 3:
                                self.ui.fator_Inst.addItem(nome)
                                self.ui.fator_Inst_2.addItem(nome)
                            elif cont == 4:
                                self.ui.T_linha.addItem(nome)
                                self.ui.T_linha_2.addItem(nome)
                            elif cont == 5:
                                self.ui.fator_Amb.addItem(nome)
                                self.ui.fator_Amb_2.addItem(nome)
                            elif cont==6:
                                self.ui.blin_lin.addItem(nome)
                                self.ui.blin_lin_2.addItem(nome)
                            elif cont==7:
                                self.ui.BAI.addItem(nome)
                                self.ui.BAI_2.addItem(nome)
                            elif cont==8:
                                self.ui.tipLinha.addItem(nome)
                                self.ui.tipLinha_2.addItem(nome)
                            elif cont==9:
                                self.ui.Tpiso.addItem(nome)
                            elif cont == 10:
                                self.ui.medProE.addItem(nome)
                            elif cont==11:
                                self.ui.medProL.addItem(nome)
                            elif cont==12:
                                self.ui.riscoInc.addItem(nome)
                            elif cont==13:
                                self.ui.provIn.addItem(nome)
                            elif cont==14:
                                self.ui.fiacao_en.addItem(nome)
                                self.ui.fiacao_tel.addItem(nome)
                            elif cont==15:
                                self.ui.perigo_esp.addItem(nome)
                            elif cont==16:
                                self.ui.danos_fis.addItem(nome)
                            elif cont==17:
                                self.ui.falhas_sis.addItem(nome)
                        else:
                            try:
                                valor.append(float(planilha.cell(i, j).value))
                            except:
                                valor.append(planilha.cell(i, j).value)
                        self.dicionario[nome] = valor
                cont += 1


app = QApplication(sys.argv)
form = SPDA()
form.show()
sys.exit(app.exec_())
