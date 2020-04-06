# -*- coding: utf-8 -*-
#Programa: Interfaz_Examen.py
#Objetivo: Mostrar los elementos y funciones 
#          de la pantalla de examen
# Autor: Pues yo weeey
# Fecha: En el año 1600

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont
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
    Ventana principal de examen.
    """
    def __init__(self):
        super().__init__()
        self.examen_db = examenBd("examen.bd")
        self.setWindowTitle("Examen")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

        

    def UI(self):
        self.estado = 0
        self.Exam_interfaz_design()
        self.layouts_exam()
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
        self.btn_update.clicked.connect(self.modificar_examen)
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.eliminar_examen)
        self.btn_Mostrar = QPushButton("Informacion")
        self.btn_Mostrar.clicked.connect(self.mostrar_informacion_messagebox)
        
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
        
    def layouts_exam(self):
        """ Layouts que compone la ventana de examen"""
        self.Exam_interfaz_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.boton_exam_layout = QFormLayout()
        self.botones_exam_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()
    
      # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.top_layout.addWidget(self.btn_retorno)
        self.down_layout.addWidget(self.label_ver_examen)
        self.down_layout.addWidget(self.exam_list)

        # Agregar los widgets (childrens) al Exam_interfaz_layout
        self.Exam_interfaz_layout.addLayout(self.top_layout,30)
        self.Exam_interfaz_layout.addLayout(self.boton_exam_layout)
        self.Exam_interfaz_layout.addLayout(self.botones_exam_layout,10)
        self.Exam_interfaz_layout.addLayout(self.down_layout)
        
        #boton_exam
        self.boton_exam_layout.addRow(self.label_Asignature, self.input_Asignature)
        self.boton_exam_layout.addRow(self.label_Exam, self.input_Exam)
        self.boton_exam_layout.addRow(self.label_Present, self.input_Present)
        self.boton_exam_layout.addRow(self.label_category, self.input_category)
        self.boton_exam_layout.addRow(self.label_detail, self.input_detail)

        self.botones_exam_layout.addWidget(self.btn_new)
        self.botones_exam_layout.addWidget(self.btn_update)
        self.botones_exam_layout.addWidget(self.btn_delete)
        self.botones_exam_layout.addWidget(self.btn_Mostrar)

        self.setLayout(self.Exam_interfaz_layout)

  
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
    
    def modificar_examen(self):

        if self.estado == 0:
            if self.exam_list.selectedItems():
                examen = self.exam_list.currentItem().text()
                id = examen.split(" --- ")[0]

                #no retorna nada  
                examen = self.examen_db.obtener_examen_por_id(id)

                if examen:
                    self.input_Asignature.setText("{0}".format(examen[1]))
                    
                    self.input_Exam.setText("{0}".format(examen[2]))

                    self.input_Present.setText("{0}".format(examen[3])) 
                    
                    self.input_category.setText("{0}".format(examen[4])) 
                    
                    self.input_detail.setText("{0}".format(examen[5]))

                    self.btn_update.setText("Guardar")
                    self.estado = 1

        else:  
            #Obtengo el id de la selccion
            if self.exam_list.selectedItems() and self.input_Exam.text() != "":

                #campo = (self.input_Exam.text())

                examen = self.exam_list.currentItem().text()
                id = examen.split(" --- ")[0]
                examen = self.examen_db.obtener_examen_por_id(id)

                id_para_consulta = int(examen[0])

                #datos = (id_para_consulta,campo)
                try:
                    self.examen_db.update_examen((self.input_Asignature.text(), 
                                                self.input_Exam.text(),
                                                self.input_Present.text(), 
                                                self.input_category.text(), 
                                                self.input_detail.text(),
                                                id_para_consulta))
                    QMessageBox.information(self, "Información", "examen actulizada correctamente")
                    self.exam_list.clear()
                    self.conjunto_de_examens()
                    self.vaciar_inputs()

                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de actualizar la examen")
            else:
                QMessageBox.information(
                    self, "Advertencia", "Debes ingresar toda la informacion")
            self.btn_update.setText("Modificar")
            self.estado = 0

    def vaciar_inputs(self):
        """
        Me deja vacio los inputs sin los valores que le cargue.
        """
        self.input_Asignature.setText("") 
        self.input_Exam.setText("")
        self.input_Present.setText("")         
        self.input_category.setText("")             
        self.input_detail.setText("")

    def eliminar_examen(self):
        """ ELimina el examen seleccionado"""
        if self.exam_list.selectedItems():
            examen = self.exam_list.currentItem().text()
            id = examen.split(" --- ")[0]

            examen = self.examen_db.obtener_examen_por_id(id)
            #AQUI NO RETORNA NADA 
            

            yes = QMessageBox.Yes

            if examen:
                question_text = ("¿Está seguro de eliminar el examen {0}?".format(examen[1]))
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.examen_db.eliminar_examen_por_id(examen[2])
                    QMessageBox.information(self, "Información", "¡examen eliminado satisfactoriamente!")
                    self.exam_list.clear()
                    self.conjunto_de_examen()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un examen a eliminar")

    def mostrar_informacion_messagebox(self):
        """ Muestra todos los datos de un registro
            en un messagebox
        """
        if self.exam_list.selectedItems():
            examen = self.exam_list.currentItem().text()
            id = examen.split(" --- ")[0]

            examen = self.examen_db.obtener_examen_por_id(id)

            if examen:
                question_text = ("""
                                Asignatura:{0}\n
                                Examen:{1}\n
                                Fecha:{2}\n
                                Categoria:{3}\n
                                Detalles:{4}\n
                                """.format(examen[0],examen[1],examen[2],examen[3],examen[4],examen[5]))
                question = QMessageBox.information(self, "Informacion", question_text, QMessageBox.Ok)

    

        
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
                                CREATE TABLE IF NOT EXISTS Examen(
                                    IdExamen INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    IdAsignatura INTEGER,
                                    Examen TEXT NOT NULL,
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
        :para examen: Una estructura que contiene
                         los datos del examen.
        :return:
        """
        sqlInsert = """                 
                    INSERT INTO Examen(
                        IdAsignatura, Examen, Fecha,
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

    def update_examen(self, id):
        """
        Query que se encarga de la actualizacion de datos
        """
        sqlUpdate = """
                    UPDATE Examen 
                    SET IdAsignatura = ?,
                        Examen = ? ,
                        Fecha = ?,
                        IdCategoria = ?,
                        Detalles = ?                  
                    WHERE Examen = ?;
                    """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlUpdate,id)
            self.connection.commit()
        except Error as e:
            print(e) 

    def obtener_todos_los_examenes(self):
        """ Obtiene todas las tuplas de la tabla Examen """
        sqlQuery = "SELECT * FROM Examen ORDER BY ROWID ASC;"

        try:
            cursor = self.connection.cursor()
            examenes = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return examenes
        except Error as e:
            print(e)

        return None


    def obtener_solo_la_ultima_examen(self):
        sqlQuery ="SELECT * FROM Examen ORDER BY Idexamen DESC LIMIT 1;"

        try:
            cursor = self.connection.cursor()
            examenes = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return examenes
        except Error as e:
            print(e)

        return None
    
    def obtener_examen_por_id(self,id):
        """
        Busca una asignatura mediante el valor del id.
        param: id: El valor de la asignatura.
        :return
        """
        sqlQuery = " SELECT * FROM Examen WHERE Examen = ?;"

        try:
            cursor = self.connection.cursor()
            examen = cursor.execute(sqlQuery, (id,)).fetchone()

            return examen
        except Error as e:
            print(e)

        return None


    def eliminar_examen_por_id(self, id):
        """
        Elimina un examen mediante el valor del id Examen.
        """
        sqlQuery = " DELETE FROM Examen WHERE Examen = ?;"

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
    window = Exam_interfaz()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    
