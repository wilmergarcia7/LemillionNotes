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
import time
import sqlite3
from sqlite3 import Error
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
        self.title = QLabel("A s i g n a t u r a", alignment=Qt.AlignCenter)
        self.title.setFixedHeight(70)
        self.title.setFixedWidth(457)
        self.title.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        
        self.asignature_list = QListWidget()     
        self.btn_new = QPushButton("Agregar")
      #  self.btn_new.clicked.connect(self.add_subject)
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")
        
        # Center Layout Widgets
        self.label_name_subject = QLabel("Nombre Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Asesinar II")
        self.label_check_in= QLabel("Hora de entrada: ")
        self.input_check_in = QTimeEdit()        
        #self.input_time_in.setPlaceholderText("12:00 p.m.")
        self.label_check_out= QLabel("Hora de salida: ")
        self.input_check_out = QTimeEdit()
        #self.input_time_out.setPlaceholderText("1:00 p.m.")
        self.label_day = QLabel("Día: ")
        self.input_day = QLineEdit()
        self.input_day.setPlaceholderText("Lunes, martes, miércoles, jueves, viernes, sábado, domingo")
        self.label_professor = QLabel("Catedrático: ")
        self.input_professor = QLineEdit()
        self.input_professor.setPlaceholderText("Wade Winston Wilson")
        self.label_classroom = QLabel("Aula: ")
        self.input_classroom = QLineEdit()
        self.input_classroom.setPlaceholderText("125") 
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        # Layouts
        # Layout principal el que contiene a left_main_layout
        # y right_main_layout
        self.main_layout = QVBoxLayout()
        
        # Layout principal del lado izquierdo que contiene a
        self.left_main_layout = QVBoxLayout()
        
        # Layouts contenidos en en left_main_layout
        self.left_top_layout = QHBoxLayout()
        self.left_center_layout = QFormLayout()
        self.left_bottom_layout = QHBoxLayout()
        
        # Layout pricipal del lado derecho
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QVBoxLayout()
        

        # Agregar los layouts hijos al layout padre
        # Layout principal
        self.main_layout.addLayout(self.left_main_layout, 45)
        self.main_layout.addLayout(self.right_main_layout, 55)
        
        # Layout Lado izquierdo
        self.left_main_layout.addLayout(self.left_top_layout, 30)
        self.left_main_layout.addLayout(self.left_center_layout, 40)
        self.left_main_layout.addLayout(self.left_bottom_layout, 30)
        
        # Layout lado derecho
        self.right_main_layout.addLayout(self.right_top_layout)

        # Agregar widgets a los layouts
        # Lista de asignaturas lado derecho
        self.right_top_layout.addWidget(self.asignature_list)
        
        # Titulo lado izquierdo superior
        self.left_top_layout.addWidget(self.title)
        
        # funciones de escribir datos lado izquierdo central
        self.left_center_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.left_center_layout.addRow(self.label_check_in , self.input_check_in )
        self.left_center_layout.addRow(self.label_check_out , self.input_check_out )
        self.left_center_layout.addRow(self.label_day , self.input_day )
        self.left_center_layout.addRow(self.label_professor , self.input_professor )
        self.left_center_layout.addRow(self.label_classroom , self.input_classroom )
        
        # Botones lado izquierdo inferior
        self.left_bottom_layout.addWidget(self.btn_new)
        self.left_bottom_layout.addWidget(self.btn_update)
        self.left_bottom_layout.addWidget(self.btn_delete)
        
        #Colocar el layout principal en la ventana principal
        self.setLayout(self.main_layout)

    def insert(self):
        """ Insertar los valores del formulario a la tabla de asignatura"""
        # Verificar si los valores requeridos fueron agregados
        if (self.input_id.text() or self.input_name.text() or
                self.input_phone.text() or self.input_email.text() != ""):
            employee = (self.input_id.text(), self.input_name.text(),
                        self.input_phone.text(), self.input_email.text(),
                        self.textedit_address.toPlainText(), "")

            try:
                self.employee_db.add_employee(employee)
                QMessageBox.information(
                    self, "Información", "Asignatura agregado correctamente")
                self.close()
                self.main = Main()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar la asignatura")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")
class Subject:
    " Base de datos para las asignaturas "

    def __init__(self, db_filename):
        """ Inicializador de la clase """
        self.connection = self.create_connection(db_filename)
        self.subject_query = """   
                                    CREATE TABLE IF NOT EXISTS asignatura
	                                (
	                                idSubject INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	                                nameSubject TEXT NOT NULL,
	                                chechkIn TIMESTAMP,
	                                chechkOut TIMESTAMP,
	                                day TEXT,
	                                professor TEXT,
	                                classroom TEXT,
	                                CONSTRAINT UQ_nameSubject UNIQUE (nameSubject)
	                                )
                              """
        self.create_table(self.connection, self.subject_query)
        
    def create_connection(self, db_filename):
        """ Crear una conexión a la base de datos SQLite """
        conn = None

        # Tratar de conectarse con SQLite y crear la base de datos
        try:
            conn = sqlite3.connect(db_filename)
            print("Conexión realizada. Versión {}".format(sqlite3.version))
        except Error as e:
            print(e)
        finally:
            return conn
    
    def create_table(self, conn, query):
        """
        Crea una tabla basado en los valores de query.
        :param conn: Conexión con la base de datos.
        :param query: La instrucción CREATE TABLE.
        :return:
        """
        try:
            cursor = conn.cursor()
            cursor.execute(query)
        except Error as e:
            print(e)

    def add_subject(self, subject):
        """
        Realiza una inserción a la tabla de empleados.
        :param subject: Una estructura que contiene
                         los datos del empleado.
        :return:
        """
        sqlInsert = """
                    INSERT INTO subject(
                        nameSubject, chechkIn, chechkOut,
	                    day, professor, classroom,)
                     VALUES(?, ?, ?, ?, ?, ?)
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, subject)
            # Indicarle al motor de base de datos
            # que los cambios sean persistentes
            self.connection.commit()
        except Error as e:
            print(e)

def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
