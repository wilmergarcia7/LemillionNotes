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
        self.subject_db = SubjectDB("subject.db")
        self.setWindowTitle("Asignatura")
        self.setGeometry(450, 450, 457, 609)
        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()
        self.set_subject_list()

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
        
        self.subject_list = QListWidget()     
        self.btn_new = QPushButton("Agregar")
        self.btn_new.clicked.connect(self.add_subject)
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
        self.right_main_layout = QVBoxLayout()
        self.right_top_layout = QVBoxLayout()
        
        # Agregar los layouts hijos al layout padre
        # Layout fondo
        self.All_layout.addLayout(self.main_title, 10)
        self.All_layout.addLayout(self.main_layout, 90)
        
        # Layout lado derecho
        self.right_main_layout.addLayout(self.right_top_layout)

        # Agregar widgets a los layouts
        # Lista de asignaturas lado derecho
        self.right_top_layout.addWidget(self.subject_list)
        
        # Titulo lado izquierdo superior
        self.left_top_layout.addWidget(self.title)
        
        # funciones de escribir datos lado izquierdo central
        self.left_center_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.left_center_layout.addRow(self.label_check_in , self.input_check_in )
        self.left_center_layout.addRow(self.label_check_out , self.input_check_out )
        self.left_center_layout.addRow(self.label_day , self.input_day )
        self.left_center_layout.addRow(self.label_professor , self.input_professor )
        self.left_center_layout.addRow(self.label_classroom , self.input_classroom )
        
         # Agregar widgets a los layouts
        # Lista de asignaturas lado inferior
        self.bottom_central_layout.addWidget(self.asignature_list)
        
        #Colocar el layout principal en la ventana principal
        self.setLayout(self.All_layout)

    def add_subject(self):
        """ Inicia el formulario de ingreso de datos del empleado """
        #self.new_subject = AddSubject(self.subject_db)
        #self.close()
        if (self.input_name_subject.text() or self.input_day.text() or
            self.input_professor.text() or self.input_classroom.text() != ""):
            subject = (self.input_name_subject.text(), self.input_check_in.text(),
                       self.input_check_out.text(), self.input_day.text(),
                       self.input_professor.text(), self.input_classroom.text())
            try:
                self.subject_db.add_subject(subject)
                QMessageBox.information(
                    self, "Información", "Asignatura agregada correctamente")
                self.close()
                self.main = Main()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar la asignatura")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la información")

    def set_subject_list(self):
        """ Obtiene las tuplas de empleados y las muestra en la lista """
        subjects = self.subject_db.get_all_subjects()

        if subjects:
            for subject in subjects:
                self.subject_list.addItem(
                    "{0} --- {1} ".format(subject[1], subject[6]))
                
    def show_subject_list(self):
        """ obtiene las tuplas de empleados y las muestra en la lista """
        # Obtener el valor de la identidad del empleado seleccionado
        subject = self.subject_list.currentItem().text()
        id = subject.split(" --- ")[0]
        
        # crear y agregar los widget necesarios para mostrar la información
        if id:
            name_subject = QLabel(subject[1])
            checkIn = QLabel(subject[2])
            checkOut = QLabel(subject[3])
            days = QLabel(subject[4])
            professor = QLabel(subject[5])
            classroom = QLabel(subject[6])           
                
            #self.left_layout.addRow("Asignatura", name_subject)
            #self.left_layout.addRow("Hora Entrada", checkIn)
            #self.left_layout.addRow("Hora Salida", checkOut)
            #self.left_layout.addRow("Días", days)
            #self.left_layout.addRow("Hora Entrada", checkIn)
            #self.left_layout.addRow("Catedratico", professor)
            #self.left_layout.addRow("Aula", classroom)
            
            
class SubjectDB:
    " Base de datos para las asignaturas "

    def __init__(self, db_filename):
        """ Inicializador de la clase """
        self.connection = self.create_connection(db_filename)
        self.subject_query = """   
                                    CREATE TABLE IF NOT EXISTS subject
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
	                    day, professor, classroom)
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
            
    def get_all_subjects(self):
        """ Obtiene todas las tuplas de la tabla subject """
        sqlQuery = " SELECT * FROM subject ORDER BY ROWID ASC "

        try:
            cursor = self.connection.cursor()
            subjects = cursor.execute(sqlQuery).fetchall()

            return subjects
        except Error as e:
            print(e)

        return None
        


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
