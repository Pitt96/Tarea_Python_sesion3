import array as ary
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
import Funciones as operaciones
from PyQt6 import uic,QtWidgets

class Ejercicio01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("suma19.ui",self)
        self.initUi()
    
    def initUi(self):
        self.bsalir.clicked.connect(self.salir)
        self.bnuevo.clicked.connect(self.nuevo)
        self.bcalcular.clicked.connect(self.calcular)

    def nuevo(self):
        self.txtnumero1.setText("")
        self.txtnumero2.setText("")
        self.lblsuma.setText("")
        self.txtnumero1.setFocus()    
    def calcular(self):
        numero1=int(self.txtnumero1.text())
        numero2=int(self.txtnumero2.text())
        suma=0
        if(numero1<numero2):
            suma=operaciones.sumar(numero1,numero2)
        else:
            suma=operaciones.sumar(numero2,numero1)
        self.lblsuma.setText(str(suma))
    def salir(self):
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_1=Ejercicio01()
    ventana_1.show()
    sys.exit(app.exec())