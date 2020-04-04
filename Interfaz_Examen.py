# -*- coding: utf-8 -*-
#Programa: Interfaz_Examen.py
#Objetivo: Mostrar los elementos y funciones 
#          de la pantalla de examen
# Autor: Pues yo weeey
# Fecha: En el año 1600

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QRegion, QFontMetrics, QPixmap
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

#from PyQt5.QtWidgets import QVBoxLayout

#from ..utils import gui_test, get_icon_pixmap
#from . import WidgetBase
class Exam_interfaz(QWidget):
    """
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.examen_db = examenBd("lemilion.bd")
        self.setWindowTitle("Examen")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

        

    def UI(self):
        self.Exam_interfaz_design()
        self.layouts()
        self.consultar()
        self.conjunto_de_examen()

    def Exam_interfaz_design(self):
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
        
        self.label_ver_examen = QLabel("  ")
        self.tittle.adjustSize()

        #Lista
        self.exam_list = QListWidget()
        self.exam_list.setStyleSheet("""
                                        background-image: url(Resource/List.jpg);
                                        font-size: 20px;
                                        """)

        self.btn_retorno = QPushButton("←")
        self.btn_retorno.setStyleSheet("""
                                        color:white;
                                         border-style: none;
                                         background-image: url(Resource/BoronRetornoInterfaz.jpg)
                                         """)    
        self.btn_retorno.setFixedHeight(70)
        self.btn_retorno.setFixedWidth(40)                         

        self.btn_new = QPushButton("Agregar")
        self.btn_new.clicked.connect(self.insert_exam)
        self.btn_new.clicked.connect(self.ultimo_conjunto_de_Examen)
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
        self.input_Present.setPlaceholderText("dia/mes/año")

        self.label_category = QLabel("Categoria: ")
        self.input_category = QLineEdit()
        self.input_category.setPlaceholderText("Añadir una categoria")

        self.label_detail = QLabel("Detalle : ")
        self.input_detail = QLineEdit()
        self.input_detail.setPlaceholderText("Agregar un detalle")
        
    def layouts(self):
        """ Layouts que compone la ventana de examen"""
        self.Exam_interfaz_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.boton_exam_layout = QFormLayout()
        self.botobes_exam_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()
    
      # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.top_layout.addWidget(self.btn_retorno)
        self.down_layout.addWidget(self.label_ver_examen)
        self.down_layout.addWidget(self.exam_list)

        # Agregar los widgets (childrens) al Exam_interfaz_layout
        self.Exam_interfaz_layout.addLayout(self.top_layout,30)
        self.Exam_interfaz_layout.addLayout(self.boton_exam_layout)
        self.Exam_interfaz_layout.addLayout(self.botobes_exam_layout,10)
        self.Exam_interfaz_layout.addLayout(self.down_layout)
        
        #boton_exam
        self.boton_exam_layout.addRow(self.label_Asignature, self.input_Asignature)
        self.boton_exam_layout.addRow(self.label_Exam, self.input_Exam)
        self.boton_exam_layout.addRow(self.label_Present, self.input_Present)
        self.boton_exam_layout.addRow(self.label_category, self.input_category)
        self.boton_exam_layout.addRow(self.label_detail, self.input_detail)

        self.botobes_exam_layout.addWidget(self.btn_new)
        self.botobes_exam_layout.addWidget(self.btn_update)
        self.botobes_exam_layout.addWidget(self.btn_delete)
        
        self.setLayout(self.Exam_interfaz_layout)

    def consultar(self):
        if self.exam_list.selectedItems():
            Exam_interfaz = self.exam_list.currentItem().text()
            
            QMessageBox.Yes

            if Exam_interfaz:
                question_text=f"desea eliminar{Exam_interfaz[1]}"
                question = QMessageBox.question(self, "advertencia",question_text,QMessageBox.Yes | QMessageBox.No,QMessageBox.No)


    def conjunto_de_examen(self):
        """ 
        Obtiene todos los registros en la tabla examen
        """

        examenes = self.examen_db.obtener_todos_los_examenes()

        if examenes:
            for examen in examenes:
                self.exam_list.addItem(
                    """ • {0} }} {1} }} {2} """.format(examen[1], examen[2], examen[3]))

    def ultimo_conjunto_de_Examen(self):
        """
        Ultimo dato de los registros
        """
        examenes = self.examen_db.obtener_solo_la_ultima_examen()

        if examenes:
            for examen in examenes:
                self.exam_list.addItem(
                    """ • {0} }} {1} }} {2} """.format(examen[1], examen[2], examen[3]))



    def insert_exam(self):
        """ Inserta los valores del fomulario a la tabla de examen"""
        if(self.input_Asignature.text() or self.input_Exam.text() or self.input_Present.text()
            or self.input_category.text() or self.input_detail.text() != ""):

            examen = (   self.input_Asignature.text(), self.input_Exam.text(),
                        self.input_Present.text(), self.input_category.text(), 
                        self.input_detail.text()
                        )
            try:
                self.examen_db.add_examen(examen)
                QMessageBox.information(
                    self, "Información", "examen agregado correctamente")
                #self.close()
                #self.main = Main()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar la examen")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la informacion")

        
class examenBd:
    """ Base de datos para examen"""
    def __init__(self,db_filename):
        """Iniciliziador de la clase"""
        self.connection = self.create_connection(db_filename)
        self.categoria_exam_query =  """
                                CREATE TABLE IF NOT EXISTS CategoriaExamen(
                                    IdCategoria INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    NombreCategoria NVARCHAR(8)
                                );
                                """
        self.examen_query = """
                                CREATE TABLE IF NOT EXISTS examen(
                                    Idexamen INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    IdAsignature INTEGER,
                                    examen TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    IdCategoria INTEGER,
                                    Detalles TEXT,
                                    FOREIGN KEY (IdCategoria)
                                        REFERENCES Categoriaexamen (IdCategoria)
                                );
                            """
        self.create_table(self.connection,self.categoria_exam_query)
        self.insert_categoria_examen()
        self.create_table(self.connection ,self.examen_query)
    
    
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

    def insert_categoria_examen(self):
        """ """
        sqlInsert = """
                    INSERT INTO Categoriaexamen (NombreCategoria)
                                            VALUES	('Escrito'),
                                                ('Documento'),
                                                ('Exposicion'),
                                                ('Ensayo'),
                                                ('Practico'),
                                                ('Virtual');
                    """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert)
            self.connection.commit()
        except Error as e:
            print(e)


    def add_examen(self, examen):
        """
        Realiza una inserción a la tabla de examen.
        :param examen: Una estructura que contiene
                         los datos del examen.
        :return:
        """
        sqlInsert = """                 
                    INSERT INTO examen(
                        IdAsignature, examen, Fecha,
                        IdCategoria, Detalles)
                     VALUES(?, ?, ?, ?, ?)
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, examen)
            # Indicarle al motor de base de datos
            # que los cambios sean persistentes
            self.connection.commit()
        except Error as e:
            print(e)

    def obtener_todos_los_examenes(self):
        """ Obtiene todas las tuplas de la tabla Examen """
        sqlQuery = "SELECT * FROM examen ORDER BY ROWID ASC;"

        try:
            cursor = self.connection.cursor()
            examenes = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return examenes
        except Error as e:
            print(e)

        return None


    def obtener_solo_la_ultima_examen(self):
        sqlQuery ="SELECT * FROM examen ORDER BY Idexamen DESC LIMIT 1;"

        try:
            cursor = self.connection.cursor()
            examenes = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return examenes
        except Error as e:
            print(e)

        return None

 

def main():
    app = QApplication(sys.argv)
    window = Exam_interfaz()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
