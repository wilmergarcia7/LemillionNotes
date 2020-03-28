# -*- coding: utf-8 -*-
#Programa: Interfaz_Asignatura.py
#Objetivo: Mostrar los elementos y funciones 
#          de la pantalla de asignatura
# Autor: Nova
# Fecha: 27/Marzo/2020

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QRegion, QFontMetrics, QPixmap
import sys
import os
#from PyQt5.QtWidgets import QVBoxLayout

#from ..utils import gui_test, get_icon_pixmap
#from . import WidgetBase
class Main(QWidget):
    """
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asignatura")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        """
        Menú que añade una asignatura y ve sus detalles
        """
        self.title = QLabel("Agregar Asignatura")
        self.asignature_list = QListWidget()     
        self.btn_new = QPushButton("Agregar")
      #  self.btn_new.clicked.connect(self.add_employee)
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")
        # Bottom Layout Widgets
        self.label_name_subject = QLabel("Nombre Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Cálculo")
        self.label_time_in= QLabel("Hora de entrada: ")
        self.input_time_in = QLineEdit()
        self.input_time_in.setPlaceholderText("12:00 p.m.")
        self.label_time_out= QLabel("Hora de salida: ")
        self.input_time_out = QLineEdit()
        self.input_time_out.setPlaceholderText("1:00 p.m.")
        self.label_day = QLabel("Día: ")
        self.input_day = QLineEdit()
        self.input_day.setPlaceholderText("Lunes")
        self.label_professor = QLabel("Catedrático: ")
        self.input_professor = QLineEdit()
        self.input_professor.setPlaceholderText("Wade Wilson")
        self.label_classroom = QLabel("Aula: ")
        self.input_classroom = QLineEdit()
        self.input_classroom.setPlaceholderText("125") 
        #self.btn_Agenda.move(171,80)
    def layouts(self):
        """ Layouts que compone el menu principal"""
        #Layouts
        self.main_layout = QHBoxLayout()
        self.left_main_layout = QVBoxLayout()
        self.left_top_layout = QHBoxLayout()
        self.left_center_layout = QFormLayout()
        self.left_bottom_layout = QHBoxLayout()
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QHBoxLayout()
        

        # Agregar los layouts hijos al layout padre
        self.right_main_layout.addLayout(self.right_top_layout)
        self.left_main_layout.addLayout(self.left_top_layout, 30)
        self.left_main_layout.addLayout(self.left_center_layout, 40)
        self.left_main_layout.addLayout(self.left_bottom_layout, 30)
        self.main_layout.addLayout(self.left_main_layout, 45)
        self.main_layout.addLayout(self.right_main_layout, 55)

        # Agregar widgets a los layouts
        self.right_top_layout.addWidget(self.asignature_list)
        self.left_top_layout.addWidget(self.title, alignment=Qt.AlignHCenter)
        #self.left_center_layout.setAlignment(Qt.AlignVCenter)
        self.left_center_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.left_center_layout.addRow(self.label_time_in , self.input_time_in )
        self.left_center_layout.addRow(self.label_time_out , self.input_time_out )
        self.left_center_layout.addRow(self.label_day , self.input_day )
        self.left_center_layout.addRow(self.label_professor , self.input_professor )
        self.left_center_layout.addRow(self.label_classroom , self.input_classroom )
        self.left_bottom_layout.addWidget(self.btn_new)
        self.left_bottom_layout.addWidget(self.btn_update)
        self.left_bottom_layout.addWidget(self.btn_delete)
        
        #Colocar el layout principal en la ventana principal
        self.setLayout(self.main_layout)

def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
