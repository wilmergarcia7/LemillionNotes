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
import calendar
from sqlite3 import Error

#clase de examen
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
        self.set_exam_list()

    #Interfaz de ventana botones margenes e imagenes
    def Exam_interfaz_design(self):
        """
        Funcion que contine los widgets de la ventana botones imagenes
        """
        #Titulo de la ventana examen
        self.tittle = QLabel("E X A M E N ", alignment=Qt.AlignCenter)
        self.label_ver_examen = QLabel("  ")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(457)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        
        #Lista de la ventana de examn
        self.exam_list = QListWidget()
        self.exam_list.itemActivated.connect(self.set_exam_list)
        self.exam_list.setStyleSheet("""
                                        background-image: url(Resource/List.jpg);
                                        font-size: 20px;
                                        """)

        #boton de retorno 
        self.btn_retorno = QPushButton("←")
        self.btn_retorno.setFixedHeight(70)
        self.btn_retorno.setFixedWidth(40)   
        self.btn_retorno.setStyleSheet("""
                                        color:white;
                                         border-style: none;
                                         background-image: url(Resource/BoronRetornoInterfaz.jpg)
                                         """)   
         
        #botones de la interfaz
        self.btn_new = QPushButton("Agregar")
        self.btn_new.clicked.connect(self.insert_exam)
        self.btn_update = QPushButton("Modificar")
        self.btn_update.clicked.connect(self.modificar_examen)
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.eliminar_examen)
        self.btn_Mostrar = QPushButton("Informacion")
        self.btn_Mostrar.clicked.connect(self.mostrar_informacion_messagebox)
        
        #label de la interfax  y txt
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
        self.input_category.setPlaceholderText("Escrito, Virtual, Documento, Ensayo, Practico")
        self.label_detail = QLabel("Detalle : ")
        self.input_detail = QLineEdit()
        self.input_detail.setPlaceholderText("Agregar un detalle")
        
    #Distribucion del formulario botones  contenedores label
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

    #Funcion de insetar examen
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
                    self, "Información", "Examen agregado correctamente")
                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de agregar la examen")
            else:
                QMessageBox.information(
                    self, "Advertencia", "Debes ingresar toda la informacion")


     #Funcion  para obtener los examenes de la lista   
    def set_exam_list(self):
        """ 
        Obtiene todos los registros en la tabla examen
        """

        examenes = self.examen_db.obtener_todos_los_examenes()

        if examenes:
            for examen in examenes:
                self.exam_list.addItem(
                    """{0} --- {1} Fecha:{2} """.format(examen[2], examen[1], examen[3]))
   
   #Funcion para modificar el examen 
    def modificar_examen(self):
        """Obtiene el id seleccionado del examen y mediante este modifica el campo o campos con el id seleccionado
        """
        if self.estado == 0:
            if self.exam_list.selectedItems():
                examen = self.exam_list.currentItem().text()
                id = examen.split(" --- ")[0]

                examen = self.examen_db.obtener_examen_por_id(id)

                if examen:
                    self.input_Asignature.setText("{0}".format(examen[1]))
                    self.input_Exam.setText("{0}".format(examen[2]))
                    self.input_Present.setText("{0}".format(examen[3])) 
                    self.input_category.setText("{0}".format(examen[4])) 
                    self.input_detail.setText("{0}".format(examen[5]))
                    self.btn_update.setText("Guardar")
                    self.btn_new.setVisible(False)
                    self.btn_Mostrar.setVisible(False)
                    self.btn_delete.setVisible(False)
                    self.estado = 1
            else:
                QMessageBox.information(self, "Advertencia", "Favor seleccionar el examen que desea a actualizar")
        else:  
            #Obtengo el id de la selccion
            if self.exam_list.selectedItems() and self.input_Exam.text() != "":

                #campo = (self.input_Exam.text())

                examen = self.exam_list.currentItem().text()
                id = examen.split(" --- ")[0]
                examen = self.examen_db.obtener_examen_por_id(id)

               # id_para_consulta = int(examen[0])

                #datos = (id_para_consulta,campo)
                try:
                    self.examen_db.update_examen((self.input_Asignature.text(), 
                                                self.input_Exam.text(),
                                                self.input_Present.text(), 
                                                self.input_category.text(), 
                                                self.input_detail.text(),
                                                id))
                    QMessageBox.information(self, "Información", "Examen actulizada correctamente")
                    self.exam_list.clear()
                    self.set_exam_list()
                    self.vaciar_inputs()

                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de actualizar la examen")
            else:
                QMessageBox.information(
                    self, "Advertencia", "Debes ingresar toda la informacion")
            self.btn_update.setText("Modificar")
            self.btn_new.setVisible(True)
            self.btn_Mostrar.setVisible(True)
            self.btn_delete.setVisible(True)
            self.estado = 0

    #Funcion para limpiar los text
    def vaciar_inputs(self):
        """
        Me deja vacio los inputs sin los valores que le cargue.
        """
        self.input_Asignature.setText("") 
        self.input_Exam.setText("")
        self.input_Present.setText("")         
        self.input_category.setText("")             
        self.input_detail.setText("")

    #Funcion pata  eliminar examen
    def eliminar_examen(self):
        """ ELimina el examen seleccionado mediante el id """
        if self.exam_list.selectedItems():
            examen = self.exam_list.currentItem().text()
            id = examen.split(" --- ")[0]

            examen = self.examen_db.obtener_examen_por_id(id)

            yes = QMessageBox.Yes

            if examen:
                question_text = ("¿Está seguro de eliminar el examen {0}?".format(examen[1]))
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.examen_db.eliminar_examen_por_id(examen[0])
                    QMessageBox.information(self, "Información", "¡Examen eliminado satisfactoriamente!")
                    self.exam_list.clear()
                    self.set_exam_list()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un examen a eliminar")

    #Funcion para mostrar la informacion del examen un messagebox
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
                                Numero De Examen:{0}\n
                                Asignatura:{1}\n
                                Examen:{2}\n
                                Fecha:{3}\n
                                Categoria:{4}\n
                                Detalles:{5}\n
                                """.format(examen[0],examen[1],examen[2],examen[3],examen[4],examen[5]))
                question = QMessageBox.information(self, "Informacion", question_text, QMessageBox.Ok)

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar el examen que desea a mostrar")
    

#Clase examen 
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
    
    #Funcion para la base de datos
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

    #Funcion que crea tablas
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

    #Funcion para insertar en categoria
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

    #Funcion para agregar un examen
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

    #Funcion para actualizar un examen por su id
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
                    WHERE IdExamen = ?;
                    """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlUpdate,id)
            self.connection.commit()
        except Error as e:
            print(e) 

    #Funcion para obtener las tuplas de examenes
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

    #Funcion para buscar un examen por su id unico
    def obtener_examen_por_id(self,id):
        """
        Busca una asignatura mediante el valor del id.
        param: id: El valor de la asignatura.
        :return
        """
        sqlQuery = " SELECT * FROM Examen WHERE IdExamen = ?;"

        try:
            cursor = self.connection.cursor()
            examen = cursor.execute(sqlQuery, (id,)).fetchone()

            return examen
        except Error as e:
            print(e)

        return None

    #Funcion para eliminar un examen por  su id
    def eliminar_examen_por_id(self, id):
        """
        Elimina un examen mediante el valor del id Examen.
        """
        sqlQuery = " DELETE FROM Examen WHERE IdExamen = ?;"

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
