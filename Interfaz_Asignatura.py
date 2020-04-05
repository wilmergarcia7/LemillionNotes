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
        self.subject_db = SubjectDB("SubjectDB.db")
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
        self.btn_new.clicked.connect(self.show_list)    
        self.btn_update = QPushButton("Modificar")
        self.btn_update.clicked.connect(self.update_subject)
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.delete_subject)
        self.btn_information = QPushButton("Información")
        self.btn_information.clicked.connect(self.show_information_messagebox)
        
        
        # Center Layout Widgets
        self.label_name_subject = QLabel("Nombre Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Asesinar II")
        self.label_check_in= QLabel("Hora de entrada: ")
        self.input_check_in = QTimeEdit()     
        self.label_check_out= QLabel("Hora de salida: ")
        self.input_check_out = QTimeEdit()
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
        
         # Layout de titulo
        self.title_layout = QVBoxLayout()
        
        # Layout contenerdor de la información sobre la asignatura
        self.content_layout = QFormLayout()
              
        # Layout que contiene botones 
        self.button_layout = QHBoxLayout()
    
        # Layout que contiene la lista de asignaturas
        self.list_layout = QVBoxLayout()

        # Agregar los layouts hijos al layout padre
        # Layout fondo
        self.main_layout.addLayout(self.title_layout, 10)
        self.main_layout.addLayout(self.content_layout, 40)
        self.main_layout.addLayout(self.button_layout, 5)
        self.main_layout.addLayout(self.list_layout, 40)
        
        # Agregar widgets a los layouts
        
        # Titulo 
        self.title_layout.addWidget(self.title)
        
        # funciones de escribir datos lado izquierdo central
        self.content_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.content_layout.addRow(self.label_check_in , self.input_check_in )
        self.content_layout.addRow(self.label_check_out , self.input_check_out )
        self.content_layout.addRow(self.label_day , self.input_day )
        self.content_layout.addRow(self.label_professor , self.input_professor )
        self.content_layout.addRow(self.label_classroom , self.input_classroom )
        
        # Botones
        self.button_layout.addWidget(self.btn_new)
        self.button_layout.addWidget(self.btn_update)
        self.button_layout.addWidget(self.btn_delete)
        self.button_layout.addWidget(self.btn_information)
        
        # Lista de asignaturas 
        self.list_layout.addWidget(self.subject_list)
        
        
        #Colocar el layout principal en la ventana principal
        self.setLayout(self.main_layout)

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
        """ Obtiene las tuplas de asignaturas y las muestra en la lista """
        subjects = self.subject_db.get_all_subjects()

        if subjects:
            for subject in subjects:
                self.subject_list.addItem(
                    "{0} --- Aula: {1} --- Hora entrada: {2}".format(subject[1], subject[6], subject[2]))
                
    def show_list(self):
        """
        Ultimo dato de los registros
        """
        subjects = self.subject_db.get_only_last_subject()

        if subjects:
            for subject in subjects:
                self.subject_list.addItem(
                    "{0} --- Aula: {1} --- Hora entrada: {2}".format(subject[1], subject[6], subject[2]))
    
   
    def delete_subject(self):
        """ Elimina la asignatura que se encuentra seleccionada """
        # Obtener el valor de la asignatura seleccionada
        # Verificar que un elemento de la lista se encuentre seleccionado
        if self.subject_list.selectedItems():
            subject = self.subject_list.currentItem().text()
            id = subject.split(" --- ")[0]

            subject = self.subject_db.get_subjects_by_id(id)

            yes = QMessageBox.Yes

            if subject:
                question_text = ("¿Está seguro de eliminar la asignatura {0}?".format(subject[1]))
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.subject_db.delete_subject_by_id(subject[1])
                    QMessageBox.information(self, "Información", "asignatura eliminada satisfactoriamente!")
                    self.subject_list.clear()
                    self.set_subject_list()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar la asignatura que desea a eliminar")

    def show_information_messagebox(self):
        """ Muestra todos los datos de un registro
            en un messagebox
        """
        if self.subject_list.selectedItems():
            subject = self.subject_list.currentItem().text()
            id = subject.split(" --- ")[0]

            subject = self.subject_db.get_subjects_by_id(id)

            if subject:
                question_text = ("""
                                Asignatura: {0}\n
                                Hora de Entrada: {1}\n
                                Hora de Salida: {2}\n
                                Días: {3}\n
                                Catedrático: {4}\n
                                Aula: {5}\n
                                """.format(subject[1],subject[2],subject[3],subject[4],subject[5],subject[6]))
                question = QMessageBox.information(self, "Informacion", question_text, QMessageBox.Ok)
    
    def update_subject(self):
        if self.subject_list.selectedItems():
            subject = self.subject_list.currentItem().text()
            id = subject.split(" --- ")[0]
                
            subject = self.subject_db.get_subjects_by_id(id)
            
            yes = QMessageBox.Yes

            if subject:
                self.input_name_subject.setText("{0}".format(subject[1]))
                
                self.input_check_in.setTime("{0}".format(subject[2]))

                self.input_check_out.setTime("{0}".format(subject[3])) 
                
                self.input_day.setText("{0}".format(subject[4])) 
                
                self.input_professor.setText("{0}".format(subject[5]))
                
                self.input_classroom.setText("{0}".format(subject[6]))                  
                self.subject_db.update_subject_by_id(subject[1])
                QMessageBox.information(self, "Información", "asignatura eliminada satisfactoriamente!")
                self.subject_list.clear()
                self.set_subject_list()
                
            
            
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
        Realiza una inserción a la tabla de asignaturas.
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
            self.connection.commit()
            return subjects
        except Error as e:
            print(e)

        return None
    
    def get_subjects_by_id(self, id):
        """
        Busca una asignatura mediante el valor del id.
        param: id: El valor de la asignatura.
        :return: Un arreglo con los atributos de la asignatura.
        """
        sqlQuery = " SELECT * FROM subject WHERE nameSubject = ?"

        try:
            cursor = self.connection.cursor()
            # fetchone espera que se retorne una tupla (1,)
            subject = cursor.execute(sqlQuery, (id,)).fetchone()
            
            return subject
        except Error as e:
            print(e)

        return None
    
    def get_only_last_subject(self):
        sqlQuery ="SELECT * FROM subject ORDER BY nameSubject DESC LIMIT 1;"

        try:
            cursor = self.connection.cursor()
            subjects = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return subjects
        except Error as e:
            print(e)

        return None

    def delete_subject_by_id(self, id):
        """
        Elimina una asignatura mediante el valor del id.
        param: id: El valor de la asignatura.
        :return: True si la asginatura se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM subject WHERE nameSubject = ?;"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None
    
    def update_subject_by_id(self, id):
        """
        Actualiza una asignatura mediante el valor del id.
        param: id: El valor de la asignatura.
        :return: True si la asginatura se actualizó. None en caso contrario.
        """
        sqlQuery = """UPDATE subject set 
                        nameSubject = ?, chechkIn = ?, chechkOut = ?,
	                    day = ?, professor = ?, classroom = ?
                        WHERE nameSubject = ?;
                   """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None
        


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
