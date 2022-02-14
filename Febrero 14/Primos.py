# -*- coding: utf-8 -*-

# Hecho por Juan José Díaz 000451588

import sys
import math
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QMessageBox


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("uic/Primos.ui", self)
        self.btnCalcular.clicked.connect(self.calcular_primo)

    def calcular_primo(self):
        primos = []  # Donde se almacenarán todos los números primos

        p1 = int(self.txtInicio.text())
        p2 = int(self.txtFinal.text())
        for n in range(p1, p2):
            raiz_entera = math.isqrt(n)  # Solo se considera la parte entera del resultado
            for i in range(2, raiz_entera + 1):
                if n % i == 0:  # Tiene un divisor, no es primo y se continua al siguiente número
                    break
            else:
                primos.append(n)  # Si no, es un primo y se añade a la lista

        QMessageBox.about(self, "Respuesta",
                          f'Se han encontrado {len(primos)} números primos entre {p1} y {p2}: \n{primos}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())

# Adaptado de https://www.programiz.com/python-programming/examples/prime-number
