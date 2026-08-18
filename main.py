from PySide6.QtWidgets import QWidget,QLabel,QHBoxLayout,QVBoxLayout,QApplication,QPushButton,QLineEdit,QLayout
from PySide6.QtCore import Qt
import math
import sys


class Calcu(QWidget):
    def __init__(self,):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setFixedSize(300, 400)

        organizador=QVBoxLayout()
        
        fileira1 = QHBoxLayout()

        fileira2 = QHBoxLayout()

        fileira3 = QHBoxLayout()

        fileira4 = QHBoxLayout()

        self.visor = QLineEdit()

        self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8,self.b9,self.b0,self.bmais,self.bigual,self.bmult,self.bsub =QPushButton("1"),QPushButton("2"),QPushButton("3"),\
        QPushButton("4"),QPushButton("5"),QPushButton("6"),QPushButton("7"),\
        QPushButton("8"),QPushButton("9"),QPushButton("0"),QPushButton("+"),QPushButton("="),\
        QPushButton("*"),QPushButton("-")

        

        self.setLayout(organizador)
       

        fileira1.setSpacing(0)
        fileira1.setContentsMargins(0, 0, 0, 0)

        fileira2.setSpacing(0)
        fileira2.setContentsMargins(0, 0, 0, 0)

        fileira3.setSpacing(0)
        fileira3.setContentsMargins(0, 0, 0, 0)

        fileira4.setSpacing(0)
        fileira4.setContentsMargins(0, 0, 0, 0)

        organizador.setSpacing(0)
        organizador.setContentsMargins(0, 0, 0, 0)


        
        organizador.addWidget(self.visor)
        organizador.addLayout(fileira1)
        organizador.addLayout(fileira2)
        organizador.addLayout(fileira3)
        organizador.addLayout(fileira4)

        fileira1.addWidget(self.b1)
        fileira1.addWidget(self.b2)
        fileira1.addWidget(self.b3)
        fileira1.addWidget(self.bsub)
        fileira2.addWidget(self.b4)
        fileira2.addWidget(self.b5)
        fileira2.addWidget(self.b6)
        fileira2.addWidget(self.bmult)
        fileira3.addWidget(self.b7)
        fileira3.addWidget(self.b8)
        fileira3.addWidget(self.b9)
        fileira4.addWidget(self.b0)
        fileira4.addWidget(self.bmais)
        fileira4.addWidget(self.bigual)

        self.visor.setReadOnly(True)
        self.visor.setText("0")
        
        
        self.b1.clicked.connect(lambda:self.colq_num("1"))
        self.b2.clicked.connect(lambda:self.colq_num("2"))
        self.b3.clicked.connect(lambda:self.colq_num("3"))
        self.b4.clicked.connect(lambda:self.colq_num("4"))
        self.b5.clicked.connect(lambda:self.colq_num("5"))
        self.b6.clicked.connect(lambda:self.colq_num("6"))
        self.b7.clicked.connect(lambda:self.colq_num("7"))
        self.b8.clicked.connect(lambda:self.colq_num("8"))
        self.b9.clicked.connect(lambda:self.colq_num("9"))
        self.b0.clicked.connect(lambda:self.colq_num("0"))
        self.bmais.clicked.connect(lambda:self.colq_num("+"))
        self.bmult.clicked.connect(lambda:self.colq_num("*"))
        self.bsub.clicked.connect(lambda:self.colq_num("-"))
        self.bigual.clicked.connect(lambda:self.resultado())

    def colq_num(self,numero):
        if self.visor.text() == "0":
            self.visor.setText(numero)
        else:
            self.visor.insert(numero)

    def resultado(self,):
        cal = self.visor.text()
        for i in cal:
            if i == "+" :
                resul = cal.split("+")
                resul = [int(i) for i in resul]
                resul_final = str(sum(resul))
            
            elif i == "-" :
                resul = cal.split("-")
                resul = [int(i) for i in resul]
                resul_final = str(resul[0] - resul [1])
        
            elif i == "*" :
                resul = cal.split("*")
                resul = [int(i) for i in resul]
                resul_final = str(resul[0] * resul[1])
        self.visor.setText(resul_final)

    
       
        
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Calcu()
    janela.show()
    sys.exit(app.exec())