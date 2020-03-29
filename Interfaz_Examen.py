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
        self.setWindowTitle("Examen")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        """
        Funcion que contine los widgets de la ventana
        """
        self.tittle = QLabel("E X A M E N ")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(457)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        
        self.tittle.adjustSize()

        self.exam_list = QListWidget()   
        self.btn_new = QPushButton("Agregar")
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")
        
        # Center Layout Widgets
        self.label_Asignature = QLabel("Asignatura: ")
        self.input_Asignature = QLineEdit()
        self.input_Asignature.setPlaceholderText("Añadir una asignatura")

        self.label_Exam = QLabel("Examen: ")
        self.input_Exam  = QLineEdit()
        self.input_Exam.setPlaceholderText("Añadir un examen")

        self.label_Present = QLabel("Presentacion: ")
        self.input_Present = QLineEdit()
        self.input_Present.setPlaceholderText("Fecha de presentacion")

        self.label_category = QLabel("Categoria: ")
        self.input_category = QLineEdit()
        self.input_category.setPlaceholderText("Añadir una categoria")

        self.label_detail = QLabel("Detalle : ")
        self.input_detail = QLineEdit()
        self.input_detail.setPlaceholderText("Agregar un detalle")
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.botones_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()
    
      # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.down_layout.addWidget(self.exam_list)

        # Agregar los widgets (childrens) al main_layout
        self.main_layout.addLayout(self.top_layout,30)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.botones_layout,10)
        self.main_layout.addLayout(self.down_layout)
        
        #bottom
        self.bottom_layout.addRow(self.label_Asignature, self.input_Asignature)
        self.bottom_layout.addRow(self.label_Exam, self.input_Exam)
        self.bottom_layout.addRow(self.label_Present, self.input_Present)
        self.bottom_layout.addRow(self.label_category, self.input_category)
        self.bottom_layout.addRow(self.label_detail, self.input_detail)

        self.botones_layout.addWidget(self.btn_new)
        self.botones_layout.addWidget(self.btn_update)
        self.botones_layout.addWidget(self.btn_delete)
        
        self.setLayout(self.main_layout)

        #

def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
