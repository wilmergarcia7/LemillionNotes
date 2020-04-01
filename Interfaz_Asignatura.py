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
        self.setGeometry(450, 450, 457, 609)
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
        self.image = QLabel()        
        self.image.setPixmap(QPixmap("Resource/Asignatura_Banner.jpg"))
        
        self.asignature_list = QListWidget()     
        self.btn_new = QPushButton("Agregar")
      # self.btn_new.clicked.connect(self.add_subject)
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")
        
        # Center Layout Widgets
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
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        # Layouts
        
        # Layout de fondo que contiene a titulo y principal
        self.All_layout = QVBoxLayout()
        
        # Layout de titulo
        self.main_title = QHBoxLayout()
        
        # Layout principal el que contiene a central_main_layout
        # y bottom_main_layout   
        self.main_layout = QVBoxLayout()
    
        # Layout principal del lado izquierdo que contiene a
        self.central_main_layout = QVBoxLayout()
        
        # Layouts contenidos en en central_main_layout
        self.central_center_layout = QFormLayout()
        self.central_bottom_layout = QHBoxLayout()
        
        # Layout pricipal del lado derecho
        self.bottom_main_layout = QVBoxLayout()
        self.bottom_central_layout = QHBoxLayout()
        
        # Agregar los layouts hijos al layout padre
        # Layout fondo
        self.All_layout.addLayout(self.main_title, 10)
        self.All_layout.addLayout(self.main_layout, 90)
        
         # Layout titulo
        self.main_title.addWidget(self.image)
        # alignment=Qt.AlignHCenter
        # Layout principal
        self.main_layout.addLayout(self.central_main_layout, 40)
        self.main_layout.addLayout(self.bottom_main_layout, 60)
              
        # Layout central
        self.central_main_layout.addLayout(self.central_center_layout, 90)
        self.central_main_layout.addLayout(self.central_bottom_layout, 10)
                       
        # funciones de escribir datos layout central
        self.central_center_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.central_center_layout.addRow(self.label_time_in , self.input_time_in )
        self.central_center_layout.addRow(self.label_time_out , self.input_time_out )
        self.central_center_layout.addRow(self.label_day , self.input_day )
        self.central_center_layout.addRow(self.label_professor , self.input_professor )
        self.central_center_layout.addRow(self.label_classroom , self.input_classroom )
        
        # Botones layout central inferior
        self.central_bottom_layout.addWidget(self.btn_new)
        self.central_bottom_layout.addWidget(self.btn_update)
        self.central_bottom_layout.addWidget(self.btn_delete)
        
         # Layout inferior
        self.bottom_main_layout.addLayout(self.bottom_central_layout)
        
         # Agregar widgets a los layouts
        # Lista de asignaturas lado inferior
        self.bottom_central_layout.addWidget(self.asignature_list)
        
        #Colocar el layout principal en la ventana principal
        self.setLayout(self.All_layout)

def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
