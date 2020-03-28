# -*- coding: utf-8 -*-
#Programa: Interfaz_Tarea.py
#Objetivo: Mostrar los elementos y funciones 
#          de la pantalla de asignatura
# Autor: Nova
# Fecha: 27/Marzo/2020
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image


class Interfaz_Tarea(QWidget):
    """
    Ventana princiapal de tarea
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tarea")
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
        self.tittle = QLabel("T A R E A ")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(457)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)


        self.label_agregar_tarea = QLabel("A g r e g a r  T a r e a")
        self.label_agregar_tarea.setStyleSheet("""  color: #856065; 
                                                    font-size: 20px""")
                                            
        self.label_ver_tareas = QLabel("T a r e a s")
        self.label_ver_tareas.setStyleSheet("""  color: #856065; 
                                                font-size: 20px;""")
        
        self.tittle.adjustSize()
        self.homework_List = QListWidget()
        self.btn_agregar = QPushButton("Agregar")
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")

        #Widgets
        self.label_Asignatura = QLabel("Nombre Asignaura: ")
        self.input_Asignatura = QLineEdit()

        self.label_Tarea = QLabel("Tarea: ")
        self.input_Tarea = QLineEdit()

        self.label_fecha_de_entrega = QLabel("Fecha de entrega: ")
        self.input_fecha_de_entrega = QLineEdit()
        self.input_fecha_de_entrega.setPlaceholderText("day/mounth/year")

        self.label_categoria_tarea = QLabel("Categoria: ")
        self.input_categria_tarea = QLineEdit()

        self.label_detalle = QLabel("Detalle: ")
        self.input_detalle = QLineEdit()

    def layouts(self):
        
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.botones_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()

        # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.down_layout.addWidget(self.label_ver_tareas)
        self.down_layout.addWidget(self.homework_List)

        # Agregar los widgets (childrens) al main_layout
        self.main_layout.addLayout(self.top_layout,30)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.botones_layout,10)
        self.main_layout.addLayout(self.down_layout)
        
        #bottom
        self.bottom_layout.addRow(self.label_agregar_tarea)
        self.bottom_layout.addRow(self.label_Asignatura, self.input_Asignatura)
        self.bottom_layout.addRow(self.label_Tarea, self.input_Tarea)
        self.bottom_layout.addRow(self.label_fecha_de_entrega, self.input_fecha_de_entrega)
        self.bottom_layout.addRow(self.label_categoria_tarea, self.input_categria_tarea)
        self.bottom_layout.addRow(self.label_detalle, self.input_detalle)

        self.botones_layout.addWidget(self.btn_agregar)
        self.botones_layout.addWidget(self.btn_update)
        self.botones_layout.addWidget(self.btn_delete)
        
        self.setLayout(self.main_layout)

        #
        
        


def main():
    app = QApplication(sys.argv)
    window = Interfaz_Tarea()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    




