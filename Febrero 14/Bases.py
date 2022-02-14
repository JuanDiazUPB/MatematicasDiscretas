# -*- coding: utf-8 -*-

# Hecho por Juan José Díaz 000451588

import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/Bases.ui",self)
        self.btnCalcular.clicked.connect(self.calcular_bases)
        
    
    def calcular_bases(self):
        cmbValue = self.cmbEleccion.currentText()
        if cmbValue == "Base 10 a cualquier base":
            n = int(self.txtNumero.text())
            b = int(self.txtBase.text())
            QMessageBox.about(self, "Base 10 a cualquier base", 
                              f'{n} en base {b}: {convertir_base10(n,b)}')
        elif cmbValue == "Cualquier base a base 10":
            n = str(self.txtNumero.text())
            b = int(self.txtBase.text())
            QMessageBox.about(self, "Cualquier base a base 10", 
                              f'{n} (base {b}) a base 10: {int(n, base=b)}')
        
def convertir_base10(numero10, base):
    lista_restantes = []
    digitos_base = []

    while numero10 > 0:  # El ciclo se detendra cuando el cociente sea 0
        restante = numero10 % base
        lista_restantes.append(restante)  # El restante se almacena en la lista
        numero10 = numero10 // base  # Se divide el número y pasa a tomar el valor del cociente

    while lista_restantes:
        digitos_base.append(str(lista_restantes.pop()))
        # Los dígitos en la lista de restantes se sacan desde el último al primero, y se construye el nuevo número en
        # una lista

    return ''.join(digitos_base)  # Los dígitos en la lista se unen en una sola cadena de texto.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

# Adaptados de https://bradfieldcs.com/algos/stacks/converting-number-bases/
# https://thecodingbot.com/convert-an-octal-numberbase-8-to-its-decimalbase-10-representation-in-python/