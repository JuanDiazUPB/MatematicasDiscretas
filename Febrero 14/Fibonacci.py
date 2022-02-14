# -*- coding: utf-8 -*-

# Hecho por Juan José Díaz 000451588

import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox 

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/Fibonacci.ui",self)
        self.btnCalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        fibonacci = []
        
        n = int(self.txtNumeros.text())
        c1 = 0
        c2 = 1
        temp = 0
        
        while temp < n:
            fibonacci.append(c1)
            f = c1 + c2
            c1 = c2
            c2 = f
            temp += 1
            
        QMessageBox.about(self, "Secuencia Fibonacci", f'Fibonacci con {n} números: {fibonacci}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
