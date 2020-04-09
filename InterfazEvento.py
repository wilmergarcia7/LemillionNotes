# -*- coding: utf-8 -*-
#Programa: InterfazEvento.py
#Objetivo: Mostrar los elementos y funciones 
#          de la pantalla de Eventos
# Autor: Nova
# Fecha: 27/Marzo/2020

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QRegion, QFontMetrics, QPixmap
import sys
import os
import sqlite3
from sqlite3 import Error
from PIL import Image

class Interfaz_Evento(QWidget):
    """
    Ventana Principal del Evento
    """
    def __init__(self):
        super().__init__()
        self.evento_db = EventoBd("event.bd")
        self.setWindowTitle("Evento")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

    def UI(self):
        self.estado = 0
        self.main_design()
        self.layouts()
        self.conjunto_de_eventos()

    def main_design(self):
        """
        Menu que contiene los widgets de dicha ventana
        """
        self.tittle = QLabel("E V E N T O", alignment=Qt.AlignCenter)
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(417)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        self.label_ver_eventos = QLabel(" ")
        self.tittle.adjustSize()

        #list
        self.evento_list = QListWidget()
        self.evento_list.setStyleSheet("""
                                        background-image: url(Resource/list.jpg);
                                        font-size: 20px;
                                        color: White;
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
        self.btn_new.clicked.connect(self.insert)
        self.btn_new.clicked.connect(self.ultimo_conjunto_eventos)
        self.btn_update = QPushButton("Modificar")
        self.btn_update.clicked.connect(self.modificar_evento)
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.eliminar_evento)
        self.btn_view = QPushButton("Informacion")
        self.btn_view.clicked.connect(self.mostrar_informacion)

        #Widgets
        self.label_name_subject = QLabel("Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Agregar una asignatura")

        self.label_name_event = QLabel("Evento: ")
        self.input_name_event = QLineEdit()
        self.input_name_event.setPlaceholderText("Agregar un evento")
        
        self.label_name_date = QLabel("Fecha: ")
        self.input_name_date = QLineEdit()
        self.input_name_date.setPlaceholderText("day/mounth/year")
        
        self.label_name_location = QLabel("Ubicacion: ")
        self.input_name_location = QLineEdit()
        self.input_name_location.setPlaceholderText("Agregar ubicación")
        
        self.label_name_detail = QLabel("Detalles: ")
        self.input_name_detail = QLineEdit()
        self.input_name_detail.setPlaceholderText("Agregar detalle")

    def layouts(self):
        """
        Layouts que compone el menu principal
        """
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.button_layout = QFormLayout()
        self.boton_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()

        # Agregar los widgets al top_layout
        self.top_layout.addWidget(self.tittle)
        self.top_layout.addWidget(self.btn_retorno)
        self.down_layout.addWidget(self.label_ver_eventos)
        self.down_layout.addWidget(self.evento_list)

        # Agregando los layouts hijos al layout padre
        self.main_layout.addLayout(self.top_layout, 30)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.boton_layout, 10)
        self.main_layout.addLayout(self.down_layout)

        #button
        #self.button_layout.addRow(self.btn_retorno)
        self.button_layout.addRow(self.label_name_subject, self.input_name_subject)
        self.button_layout.addRow(self.label_name_event, self.input_name_event)
        self.button_layout.addRow(self.label_name_date, self.input_name_date)
        self.button_layout.addRow(self.label_name_location, self.input_name_location)
        self.button_layout.addRow(self.label_name_detail, self.input_name_detail)


        # Los botones que se posicionaran en la parte inferior
        self.boton_layout.addWidget(self.btn_new)
        self.boton_layout.addWidget(self.btn_update)
        self.boton_layout.addWidget(self.btn_delete)
        self.boton_layout.addWidget(self.btn_view)

        self.setLayout(self.main_layout)


    def conjunto_de_eventos(self):
        """
        Obtiene todos los registros de la tabla eventos
        """
        eventos = self.evento_db.obtener_todos_los_eventos()

        if eventos:
            for evento in eventos:
                self.evento_list.addItem(
                    """ • {0} }} {1} }} {2} """.format(evento[1], evento[2], evento[3]))

    def ultimo_conjunto_eventos(self):
        """
        Ultimo registro de eventos
        """

        eventos = self.evento_db.obtener_ultimo_evento()

        if eventos:
            for evento in eventos:
                self.evento_list.addItem(
                    """ • {0} }} {1} }} {2} """.format(evento[1], evento[2], evento[3]))

    def insert(self):
        """
        Inserta los registros del formulario a la tabla evento
        """
        if(self.input_name_subject.text() or self.input_name_event.text()
            or self.input_name_date.text() or self.input_name_location.text()
            or self.input_name_detail.text() != ""):

            evento = (  self.input_name_subject.text(), self.input_name_event.text(),
                        self.input_name_date.text(), self.input_name_location.text(),
                        self.input_name_detail.text()
                        )
            try:
                self.evento_db.add_Evento(evento)
                QMessageBox.information(
                    self, "Información", "Evento agregado correctamente")
                #self.close()
                #self.main = Main()    
            except Error as e:
                QMessageBox.information(
                    self, "Error", "Error en el proceso de agregar evento")
        else:
            QMessageBox.information(
                self, "Advertencia", "Debes ingresar todos los datos")


    def modificar_evento(self):
        if self.estado == 0:
            if self.evento_list.selectedItems():
                evento = self.evento_list.currentItem().text()
                id = evento.split("---")[0]

                evento = self.evento_db.evento_por_id(id)

                if evento:
                    self.input_name_subject.setText("{0}".format(evento[1]))
                    self.input_name_event.setText("{0}".format(evento[2]))
                    self.input_name_date.setText("{0}".format(evento[3]))
                    self.input_name_location.setText("{0}".format(evento[4]))
                    self.input_name_detail.setText("{0}".format(evento[5]))
                    self.btn_update.setText("Guardar")
                    self.estado = 1

        else:
            #Obteniendo el id seleccionado
            if self.evento_list.selectedItems() and self.input_name_event.text() != "":
                evento = self.evento_list.currentItem().text()
                id = evento.split(" --- ")[0]
                evento = self.evento_db.evento_por_id(id)

                id_consulta = int(evento[0])

                try:
                    self.evento_db.update_evento((self.input_name_subject.text(),
                                                  self.input_name_event.text(),
                                                  self.input_name_date.text(),
                                                  self.input_name_location.text(),
                                                  self.input_name_detail.text(),
                                                  id_consulta))
                    QMessageBox.information(self, "Información", "Evento actulizado correctamente")
                    self.evento_list.clear()
                    self.conjunto_de_eventos()
                    self.vaciar_inputs()

                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de actualizar el Evento")
            else:
                QMessageBox.information(
                    self, "Advertencia", "Debes ingresar toda la informacion")
            self.btn_update.setText("Modificar")
            self.estado = 0      

    def vaciar_inputs(self):
        """
        Deja vacio los inputs de los valores cargados anteriormente
        """
        self.input_name_subject.setText("") 
        self.input_name_event.setText("")
        self.input_name_date.setText("")         
        self.input_name_location.setText("")             
        self.input_name_detail.setText("")    


    def eliminar_evento(self):
        """ 
        ELimina el evento seleccionado
        """
        if self.evento_list.selectedItems():
            evento = self.evento_list.currentItem().text()
            id = evento.split(" --- ")[0]

            evento = self.evento_db.evento_por_id(id)

            yes = QMessageBox.Yes

            if evento:
                question_text = ("¿Esta seguro de eliminar el evento {0}?".format(evento[2]))
                question = QMessageBox.question(self, "Advertencia", question_text,
                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if question == QMessageBox.Yes:
                    self.evento_db.eliminar_evento(evento[2])
                    QMessageBox.information(self, "Información", "Evento eliminado satisfactoriamente")
                    self.evento_list.clear()
                    self.conjunto_de_eventos()

            else:
                QMessageBox.information(self, "Advertencia", "Ha ocurrido un error. Reintente nuevamente")

        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar un Evento a eliminar")  


    def mostrar_informacion(self):
        """
        Muestra la informacion de un evento
        """
        if self.evento_list.selectedItems():
            evento = self.evento_list.currentItem().text()
            id = evento.split(" --- ")[0]

            evento = self.evento_db.evento_por_id(id)

            if evento:
                question_text = ("""
                                NoEvento:{0}\n
                                Asignatura:{1}\n
                                Evento:{2}\n
                                Fecha:{3}\n
                                Ubicacion:{4}\n
                                Detalle:{5}\n
                                """.format(evento[0],evento[1],evento[2],evento[3],evento[4],evento[5]))
                question = QMessageBox.information(self, "Informacion", question_text, QMessageBox.Ok)


class EventoBd:
    """
    Base de datos para el evento
    """
    def __init__(self,db_filename):
        """
        Incializador de la clase
        """
        self.connection = self.create_connection(db_filename)

        self.asignatura_evento  = """
                                    CREATE TABLE IF NOT EXISTS AsignaturaEvento(
                                        IdAsignatura INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                        NombreAsignatura NVARCHAR(10)
                                    );
                                  """
       
        self.evento_query = """
                                CREATE TABLE IF NOT EXISTS EventoT(
                                    IdEvento INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    IdAsignatura INTEGER,
                                    Evento TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    Ubicacion TEXT NOT NULL,
                                    Detalle TEXT,
                                    FOREIGN KEY (IdAsignatura)
                                        REFERENCES AsignaturaEvento (IdAsignatura)
                                );
                            """
        self.create_table(self.connection,self.asignatura_evento)
        #self.insert_asignatura_evento()
        self.create_table(self.connection ,self.evento_query)

    def create_connection(self, db_filename):
        """ Crear una conexión a la base de datos SQLite """
        conn = None

        try:
            conn = sqlite3.connect(db_filename)
            print("Conexión realizada. Version {}".format(sqlite3.version))
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
    
   

    

    def add_Evento(self, EventoT):
        """
        Insertar en la tabla evento
        :param Evento: Una estructura que contiene los datos del evento
        :return:
        """
        sqlInsert = """
                    INSERT INTO EventoT(
                        IdAsignatura, Evento, Fecha, Ubicacion,
                        Detalle)
                    VALUES(?, ?, ?, ?, ?)
                    """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlInsert, EventoT)
            # Indicarle al motor de base de datos
            # que los cambios sean persistentes
            self.connection.commit()
        except Error as e:
            print(e)

    def update_evento(self, EventoT):
        """
        Modificar los datos
        """
        sqlUpdate = """
                    UPDATE EventoT
                    SET IdAsignatura = ?,
                        Evento = ?,
                        Fecha = ?,
                        Ubicacion = ?,
                        Detalle = ?,
                    WHERE IdEvento = ?;
                    """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlUpdate,EventoT)
            self.connection.commit()
        except Error as e:
            print(e)
    
    def obtener_todos_los_eventos(self):
        """
        Obtiene todos los datos de eventos
        """
        sqlQuery = "SELECT * FROM EventoT ORDER BY ROWID ASC;"

        try:
            cursor = self.connection.cursor()
            eventos = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return eventos
        except Error as e:
            print(e)

        return None
    
    def obtener_ultimo_evento(self):
        sqlQuery ="SELECT * FROM EventoT ORDER BY IdEvento DESC LIMIT 1;" 

        try:
            cursor = self.connection.cursor()
            eventos = cursor.execute(sqlQuery).fetchall()
            self.connection.commit()
            return eventos
        except Error as e:
            print(e)

        return None
    

    def evento_por_id(self, id_Evento):
        """ 
        Busca un evento mediante el valor del id
        """
        sqlQuery = " SELECT * FROM EventoT WHERE Evento = ?;"

        try:
            cursor = self.connection.cursor()
            evento = cursor.execute(sqlQuery, (id_Evento,)).fetchone()

            return evento

        except Error as e:
            print(e)

        return None


    def eliminar_evento(self, id_Evento):
        """
        Elimina un evento por el valor del id
        """
        sqlQuery = " DELETE FROM EventoT WHERE Evento = ?;"

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlQuery, (id_Evento,))
            self.connection.commit()

            return True
        except Error as e:
            print(e)

        return None



def main():
    app = QApplication(sys.argv)
    window = Interfaz_Evento()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
