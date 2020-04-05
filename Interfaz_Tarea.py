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
        self.tarea_db = TareaBd("lemilion.bd")
        self.setWindowTitle("Tarea")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

    def UI(self):
        self.estado = 0
        self.main_design()
        self.layouts()
        self.conjunto_de_tareas()

    def main_design(self):
        """
        Funcion que contine los widgets de la ventana
        """
        self.tittle = QLabel("T A R E A ")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(417)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        self.label_ver_tareas = QLabel("  ")
        self.tittle.adjustSize()

        #Lista
        self.homework_List = QListWidget()
        self.homework_List.setStyleSheet("""
                                        
                                        background-image: url(Resource/list.jpg);
                                        font-size: 20px;
                                        color: white;
                                        """)
        
        self.btn_retorno = QPushButton("←")
        self.btn_retorno.setStyleSheet("""
                                        color:white;
                                         border-style: none;
                                         background-image: url(Resource/BoronRetornoInterfaz.jpg)
                                         """)
        self.btn_retorno.setFixedHeight(70)
        self.btn_retorno.setFixedWidth(40)

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.insert)
        self.btn_agregar.clicked.connect(self.ultimo_conjunto_de_tareas)
        self.btn_update = QPushButton("Modificar")
        self.btn_update.clicked.connect(self.modificar_datos)
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.eliminar_tarea)
        self.btn_Mostrar = QPushButton("Informacion")
        self.btn_Mostrar.clicked.connect(self.mostrar_informacion_messagebox)

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
        self.top_layout = QHBoxLayout()
        self.bottom_layout = QFormLayout()
        self.botones_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()

        # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.top_layout.addWidget(self.btn_retorno)

        self.down_layout.addWidget(self.label_ver_tareas)
        self.down_layout.addWidget(self.homework_List)

        # Agregar los widgets (childrens) al main_layout
        self.main_layout.addLayout(self.top_layout,30)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.botones_layout,10)
        self.main_layout.addLayout(self.down_layout)
        
        #bottom
        #self.bottom_layout.addRow(self.btn_retorno)
        self.bottom_layout.addRow(self.label_Asignatura, self.input_Asignatura)
        self.bottom_layout.addRow(self.label_Tarea, self.input_Tarea)
        self.bottom_layout.addRow(self.label_fecha_de_entrega, self.input_fecha_de_entrega)
        self.bottom_layout.addRow(self.label_categoria_tarea, self.input_categria_tarea)
        self.bottom_layout.addRow(self.label_detalle, self.input_detalle)

        self.botones_layout.addWidget(self.btn_agregar)
        self.botones_layout.addWidget(self.btn_update)
        self.botones_layout.addWidget(self.btn_delete)
        self.botones_layout.addWidget(self.btn_Mostrar)
        
        self.setLayout(self.main_layout)


    def conjunto_de_tareas(self):
        """ 
        Obtiene todos los registros en la tabla tarea
        """
        tareas = self.tarea_db.obtener_todas_las_tareas()

        if tareas:
            for tarea in tareas:
                self.homework_List.addItem(
                    """{0} --- {1} Fecha:{2} """.format(tarea[2], tarea[1], tarea[3]))

    def ultimo_conjunto_de_tareas(self):
        """
        Ultimo dato de los registros
        """
        tareas = self.tarea_db.obtener_solo_la_ultima_tarea()

        if tareas:
            for tarea in tareas:
                self.homework_List.addItem(
                    """{0} --- {1} Fecha:{2} """.format(tarea[2], tarea[1], tarea[3]))



    def insert(self):
        """ Inserta los valores del fomulario a la tabla trarea"""
        if(self.input_Asignatura.text() or self.input_Tarea.text() or self.input_fecha_de_entrega.text()
            or self.input_categria_tarea.text() or self.input_detalle.text() != ""):

            tarea = (   self.input_Asignatura.text(), self.input_Tarea.text(),
                        self.input_fecha_de_entrega.text(), self.input_categria_tarea.text(), 
                        self.input_detalle.text()
                        )
            try:
                self.tarea_db.add_Tarea(tarea)
                QMessageBox.information(
                    self, "Información", "Tarea agregado correctamente")
                #self.close()
                #self.main = Main()
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error al momento de agregar la tarea")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar toda la informacion")

    def modificar_datos(self):

        if self.estado == 0:
            if self.homework_List.selectedItems():
                tarea = self.homework_List.currentItem().text()
                id = tarea.split(" --- ")[0]
                    
                tarea = self.tarea_db.obtener_tarea_por_id(id)

                if tarea:
                    self.input_Asignatura.setText("{0}".format(tarea[1]))
                    
                    self.input_Tarea.setText("{0}".format(tarea[2]))

                    self.input_fecha_de_entrega.setText("{0}".format(tarea[3])) 
                    
                    self.input_categria_tarea.setText("{0}".format(tarea[4])) 
                    
                    self.input_detalle.setText("{0}".format(tarea[5]))
                    self.btn_update.setText("Guardar")
                    self.estado = 1

        else:  
            #Obtengo el id de la selccion
            if self.homework_List.selectedItems() and self.input_Tarea.text() != "":

                #campo = (self.input_Tarea.text())

                tarea = self.homework_List.currentItem().text()
                id = tarea.split(" --- ")[0]
                tarea = self.tarea_db.obtener_tarea_por_id(id)

                id_para_consulta = int(tarea[0])

                #datos = (id_para_consulta,campo)
                try:
                    self.tarea_db.update_Tarea((self.input_Asignatura.text(), 
                                                self.input_Tarea.text(),
                                                self.input_fecha_de_entrega.text(), 
                                                self.input_categria_tarea.text(), 
                                                self.input_detalle.text(),
                                                id_para_consulta))
                    QMessageBox.information(self, "Información", "Tarea actulizada correctamente")
                    self.homework_List.clear()
                    self.conjunto_de_tareas()
                    self.vaciar_inputs()

                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de actualizar la tarea")
            else:
                QMessageBox.information(
                    self, "Advertencia", "Debes ingresar toda la informacion")
            self.btn_update.setText("Modificar")
            self.estado = 0

    def vaciar_inputs(self):
        """
        Me deja vacio los inputs sin los valores que le cargue.
        """
        self.input_Asignatura.setText("") 
        self.input_Tarea.setText("")
        self.input_fecha_de_entrega.setText("")         
        self.input_categria_tarea.setText("")             
        self.input_detalle.setText("")

    def eliminar_tarea(self):
        """ ELimina la tarea seleccionada"""
        if self.homework_List.selectedItems():
            tarea = self.homework_List.currentItem().text()
            id = tarea.split(" --- ")[0]

            tarea = self.tarea_db.obtener_tarea_por_id(id)

            yes = QMessageBox.Yes

            if tarea:
                question_text = ("¿Está seguro de eliminar la tarea {0}?".format(tarea[2]))
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.tarea_db.eliminar_tarea_por_id(tarea[2])
                    QMessageBox.information(self, "Información", "¡Tarea eliminada satisfactoriamente!")
                    self.homework_List.clear()
                    self.conjunto_de_tareas()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un Tarea a eliminar")

    def mostrar_informacion_messagebox(self):
        """ Muestra todos los datos de un registro
            en un messagebox
        """
        if self.homework_List.selectedItems():
            tarea = self.homework_List.currentItem().text()
            id = tarea.split(" --- ")[0]

            tarea = self.tarea_db.obtener_tarea_por_id(id)

            if tarea:
                question_text = ("""
                                NumeroDeTarea:{0}\n
                                Asignatura:{1}\n
                                Tarea:{2}\n
                                Fecha:{3}\n
                                Categoria:{4}\n
                                Detalles:{5}\n
                                """.format(tarea[0],tarea[1],tarea[2],tarea[3],tarea[4],tarea[5]))
                question = QMessageBox.information(self, "Informacion", question_text, QMessageBox.Ok)

    



class TareaBd:
    """ Base de datos para Tarea"""
    def __init__(self,db_filename):
        """Iniciliziador de la clase"""
        self.connection = self.create_connection(db_filename)
        self.categoria_query =  """
                                CREATE TABLE IF NOT EXISTS CategoriaTarea(
                                    IdCategoria INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    NombreCategoria NVARCHAR(8)
                                );
                                """
        self.tarea_query = """
                                CREATE TABLE IF NOT EXISTS Tarea(
                                    IdTArea INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    IdAsignatura INTEGER,
                                    Tarea TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    IdCategoria INTEGER,
                                    Detalles TEXT,
                                    FOREIGN KEY (IdCategoria)
                                        REFERENCES CategoriaTarea (IdCategoria)
                                );
                            """
        self.create_table(self.connection,self.categoria_query)
        self.insert_categoria_tarea()
        self.create_table(self.connection ,self.tarea_query)
    
    
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

    def insert_categoria_tarea(self):
        """ """
        sqlInsert = """
                     
                    INSERT INTO CategoriaTarea (NombreCategoria)
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


    def add_Tarea(self, Tarea):
        """
        Realiza una inserción a la tabla de tarea.
        :param Tarea: Una estructura que contiene
                         los datos del empleado.
        :return:
        """
        sqlInsert = """                 
                    INSERT INTO Tarea(
                        IdAsignatura, Tarea, Fecha,
                        IdCategoria, Detalles)
                     VALUES(?, ?, ?, ?, ?)
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, Tarea)
            # Indicarle al motor de base de datos
            # que los cambios sean persistentes
            self.connection.commit()
        except Error as e:
            print(e)

    def update_Tarea(self, Tarea):
        """
        Query que se encarga de la actulizacion de datos
        """
        sqlUpdate = """
                    UPDATE Tarea 
                    SET IdAsignatura = ?,
                        Tarea = ? ,
                        Fecha = ?,
                        IdCategoria = ?,
                        Detalles = ?                  
                    WHERE IdTarea = ?;
                    """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlUpdate,Tarea)
            self.connection.commit()
        except Error as e:
            print(e)

    def obtener_todas_las_tareas(self):
        """ Obtiene todas las tuplas de la tabla employee """
        sqlQuery = "SELECT * FROM Tarea ORDER BY ROWID ASC;"

        try:
            cursor = self.connection.cursor()
            tareas = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return tareas
        except Error as e:
            print(e)

        return None


    def obtener_solo_la_ultima_tarea(self):
        sqlQuery ="SELECT * FROM Tarea ORDER BY IdTarea DESC LIMIT 1;"

        try:
            cursor = self.connection.cursor()
            tareas = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return tareas
        except Error as e:
            print(e)

        return None

    def obtener_tarea_por_id(self,id_Tarea):
        """ Busca una tarea mediante el valor del id"""
        sqlQuery = " SELECT * FROM Tarea WHERE Tarea = ?;"

        try:
            cursor = self.connection.cursor()
            tarea = cursor.execute(sqlQuery, (id_Tarea,)).fetchone()

            return tarea
        except Error as e:
            print(e)

        return None


    def eliminar_tarea_por_id(self, id_Tarea):
        """
        Elimina una tarea mediante el valor del id Tarea.
        """
        sqlQuery = " DELETE FROM Tarea WHERE Tarea = ?;"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id_Tarea,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None


def main():
    app = QApplication(sys.argv)
    window = Interfaz_Tarea()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    




