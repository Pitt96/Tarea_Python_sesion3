import array as ary
import sys
from PyQt6.QtWidgets import QMainWindow,QApplication
from PyQt6 import uic,QtWidgets

class Ejercicio01(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("suma.ui",self)
        self.initUi()
    
    def initUi(self):
        lista=[]
        suma=0

        for x in range(10,50,3):
            if(x%2==0):
                lista.append(x)

        for x in range(0,len(lista)):
            self.listdatos.addItem(">"+str(lista[x]))
            suma+=lista[x]
        self.lblsuma.setText(str(suma))
        self.bsalir.clicked.connect(self.salir)
        

    
    
    def salir(self):
        self.close()
if __name__=='__main__':
    app=QApplication(sys.argv)
    ventana_1=Ejercicio01()
    ventana_1.show()
    sys.exit(app.exec())