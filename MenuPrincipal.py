# -*- coding: utf-8 -*-
#Programa: PrimeraPAntalla
#Objetivo: 
# Autor: Nova
# Fecha: 16/Marzo/2020


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon, QRegion, QFontMetrics, QPixmap
import sys
import os
import platform
import sqlite3
import time
from ctypes import Union
from getpass import getuser
from sqlite3 import Error
from PIL import Image

#Necesario para agregar al fondo
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtCore import QSize, Qt, QRect

#Botones

class Main(QWidget):
    """
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lemilion | {0}".format(platform.system()))
        self.setGeometry(450, 80, 457,609)
        
        #Colocar Imagen de fondo
        oImage = QImage("Resource/Lemilion.jpg")
        sImage = oImage.scaled(QSize(457,609))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        #self.layouts()

    def main_design(self):
        """
        Disign principal of aplication
        """

        #BOTON ASIGNATURA
        self.btn_Asignatura = QPushButton(self)
        
        self.btn_Asignatura.setFixedWidth(60)
        self.btn_Asignatura.setFixedHeight(60)
        self.btn_Asignatura.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Asignatura.setStyleSheet("""QPushButton { image :url(Resource/Asignatura.jpg);
                                                        border-radius: 50px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                            """)

         
        self.btn_Asignatura.move(300,300)
        self.label_Asignatura = QLabel("Asignatura",self)
        self.label_Asignatura.setStyleSheet("""font: bold 14px;""")
        self.label_Asignatura.setFixedHeight(20)
        self.label_Asignatura.setFixedWidth(80)
        self.label_Asignatura.move(290,370)

        self.btn_Asignatura.clicked.connect(self.add_Asignatura)
        
        ###
        #A G E N D A
        ###
        
        self.btn_Agenda = QPushButton(self)
        self.btn_Agenda.setFixedWidth(60)
        self.btn_Agenda.setFixedHeight(60)
        self.btn_Agenda.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Agenda.setStyleSheet("""QPushButton { image :url(Resource/Agenda.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                            QLabel 
                                        """)
        self.btn_Agenda.move(100,300)


        self.label_Agenda = QLabel("Agenda",self)
        self.label_Agenda.setStyleSheet("""font: bold 14px;""")
        self.label_Agenda.setFixedHeight(20)
        self.label_Agenda.setFixedWidth(60)
        self.label_Agenda.move(105,370)

        self.btn_Agenda.clicked.connect(self.add_MenuAgenda)
        
        ###
        # L A B E L  U S U A R I O 
        ## 
        self.label_datos_de_sistema = QLabel("{}".format(getuser()),self)
        self.label_datos_de_sistema.move(10,570)
        


        
    def add_MenuAgenda(self):
        self.Menu_Agenda = AgendaMenu()
        self.close()
    def add_Asignatura(self):
        self.asignatura = InterfazAsignatura()
        self.close()

# - - - - - - - - A G E N D A  M E N U - - - - - - - - - -- 

class AgendaMenu(QWidget):
    """
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lemilion")
        self.setGeometry(450, 80, 457,609)
        
        #Colocar Imagen de fondo
        oImage = QImage("Resource/MenuAgenda.jpg")
        sImage = oImage.scaled(QSize(457,609))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()


    def main_design(self):
        """
        Design principal of aplication
        """
        ###
        #T A R E A 
        ###
        #Boton
        self.btn_Tarea = QPushButton()
        self.btn_Tarea.setFixedWidth(60)
        self.btn_Tarea.setFixedHeight(60)
        self.btn_Tarea.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Tarea.setStyleSheet("""QPushButton { image :url(Resource/Tarea_Icon.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
        
        self.btn_Tarea.clicked.connect(self.add_InterfazTarea)

        #Label
        self.label_Tarea = QLabel("Tarea")
        self.label_Tarea.setStyleSheet("""font: bold 14px; color: black;""")
        self.label_Tarea.setFixedHeight(20)
        self.label_Tarea.setFixedWidth(50)
        self.label_Tarea.setAlignment(Qt.AlignCenter)

        ###
        # E X A M E N 
        ###
        self.btn_Examen = QPushButton()
        self.btn_Examen.setFixedWidth(60)
        self.btn_Examen.setFixedHeight(60)
        self.btn_Examen.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Examen.setStyleSheet("""QPushButton { image :url(Resource/Examen_Icon.jpg); 
                                                        border-radius: 30px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
        self.btn_Examen.clicked.connect(self.add_InterfazExamen)
        self.label_Examen = QLabel("Examen")
        self.label_Examen.setStyleSheet("""font: bold 14px; color: black;""")
        self.label_Examen.setFixedHeight(20)
        self.label_Examen.setFixedWidth(60)
        self.label_Examen.setAlignment(Qt.AlignCenter)

        ###
        # E V E N T O 
        ###

        self.btn_Evento = QPushButton()
        self.btn_Evento.setFixedWidth(60)
        self.btn_Evento.setFixedHeight(60)
        self.btn_Evento.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Evento.setStyleSheet("""QPushButton { image :url(Resource/Evento_Icon.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
        self.btn_Evento.clicked.connect(self.add_InterfazEvento)
        self.label_Evento = QLabel("Evento")
        self.label_Evento.setStyleSheet("""font: bold 14px; color: black;""")
        self.label_Evento.setFixedHeight(20)
        self.label_Evento.setFixedWidth(60)
        self.label_Evento.setAlignment(Qt.AlignCenter)
        
        ###
        # R E T O R N O 
        ###
        self.btn_Retorno = QPushButton("⮈")
        self.btn_Retorno.setFixedWidth(60)
        self.btn_Retorno.setFixedHeight(30)
        self.btn_Retorno.setStyleSheet("""  border-style: none;
                                            background-color: yellow;
                                            font: 20px;
                                            border-color: yellow;
                                            background-image: url(Resource/Boton.jpg)
                                            """)
        self.btn_Retorno.clicked.connect(self.Add_MenuPrincipal)
      
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        #Layouts
        self.main_layout = QHBoxLayout()
        self.botones_layout = QVBoxLayout()

        #Agregar layouts a layout
        self.main_layout.addLayout(self.botones_layout)

        #Agregar widgetc a los layouts
        self.botones_layout.addWidget(self.label_Evento)
        self.botones_layout.addWidget(self.btn_Evento)

        self.botones_layout.addWidget(self.label_Examen)
        self.botones_layout.addWidget(self.btn_Examen)

        self.botones_layout.addWidget(self.label_Tarea)
        self.botones_layout.addWidget(self.btn_Tarea)

        self.botones_layout.addWidget(self.btn_Retorno)

        #Colocar el layout priniapl en la ventana principal
        self.setLayout(self.main_layout)

    def Add_MenuPrincipal(self):
        self.menu = Main()
        self.close()

    def add_InterfazTarea(self):
        self.tarea = Interfaz_Tarea()
        self.close()

    def add_InterfazExamen(self):
        self.examen = Interfaz_Examen()
        self.close
    def add_InterfazEvento(self):
        self.examen = Interfaz_Evento()
        self.close


###############################################################
# - - - - - - - -  W I D G E T  A S I G N A T U R A - - - - - - - - - - -

class InterfazAsignatura(QWidget):
    """
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.subject_db = SubjectDB("lemilion.bd")
        self.setWindowTitle("Lemilion")
        self.setGeometry(450, 450, 457, 609)
        self.UI()
        self.show()

    def UI(self):
        self.state = 0
        self.main_design()
        self.layouts()
        self.set_subject_list()

    def main_design(self):
        """
        Menú que añade una asignatura y ve sus detalles
        """
        self.title = QLabel("A s i g n a t u r a", alignment=Qt.AlignCenter)
        self.title.setFixedHeight(70)
        self.title.setFixedWidth(400)
        self.title.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        self.title.adjustSize()
        self.btn_retorno = QPushButton("←")
        self.btn_retorno.setStyleSheet("""
                                        color:white;
                                         border-style: none;
                                         background-image: url(Resource/BoronRetornoInterfaz.jpg)
                                         """)
        self.btn_retorno.setFixedHeight(70)
        self.btn_retorno.setFixedWidth(30)
      
        self.subject_list = QListWidget()
        self.subject_list.itemActivated.connect(self.set_subject_list)
         
        self.btn_new = QPushButton("Agregar")
        self.btn_new.clicked.connect(self.add_subject)
        self.btn_update = QPushButton("Modificar")
        self.btn_update.clicked.connect(self.update_subject)
        self.btn_delete = QPushButton("Eliminar")
        self.btn_delete.clicked.connect(self.delete_subject)
        self.btn_information = QPushButton("Información")
        self.btn_information.clicked.connect(self.show_information_messagebox)
        
        
        # Center Layout Widgets
        self.label_name_subject = QLabel("Nombre Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Programación I")
        self.label_check_in= QLabel("Hora de entrada: ")
        self.input_check_in = QTimeEdit()     
        self.label_check_out= QLabel("Hora de salida: ")
        self.input_check_out = QTimeEdit()
        self.label_day = QLabel("Día: ")
        self.cbdays = QComboBox()
        self.cbdays.addItem('Lunes')
        self.cbdays.addItem('Lunes, Martes')
        self.cbdays.addItem('Lunes, Martes, Miércoles')
        self.cbdays.addItem('Lunes, Martes, Miércoles, Jueves')
        self.cbdays.addItem('Lunes, Martes, Miércoles, Jueves, Viernes')
        self.cbdays.addItem('Sábado')
        self.cbdays.addItem('Sábado, Domingo')
        self.label_professor = QLabel("Catedrático: ")
        self.input_professor = QLineEdit()
        self.input_professor.setPlaceholderText("Wade Winston Wilson")
        self.label_classroom = QLabel("Aula: ")
        self.input_classroom = QLineEdit()
        self.input_classroom.setPlaceholderText("A-101") 
    
    def layouts(self):
        """ Layouts que compone el menu principal"""
        # Layouts
        # Layout principal 
        self.main_layout = QVBoxLayout()
        
         # Layout de titulo
        self.title_layout = QHBoxLayout()
        
        # Layout contenerdor de la información sobre la asignatura
        self.content_layout = QFormLayout()
              
        # Layout que contiene botones 
        self.button_layout = QHBoxLayout()
    
        # Layout que contiene la lista de asignaturas
        self.list_layout = QVBoxLayout()

        # Agregar los layouts hijos al layout padre
        # Layout fondo
        self.main_layout.addLayout(self.title_layout, 15)
        self.main_layout.addLayout(self.content_layout, 35)
        self.main_layout.addLayout(self.button_layout, 5)
        self.main_layout.addLayout(self.list_layout, 40)
        
        # Agregar widgets a los layouts
        
        # Titulo 
        self.title_layout.addWidget(self.title)
        self.title_layout.addWidget(self.btn_retorno)
        
        # funciones de escribir datos lado izquierdo central
        self.content_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.content_layout.addRow(self.label_check_in , self.input_check_in )
        self.content_layout.addRow(self.label_check_out , self.input_check_out )
        self.content_layout.addRow(self.label_day , self.cbdays )
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
        if (self.input_name_subject.text() or self.input_day.text() or
            self.input_professor.text() or self.input_classroom.text() != "" ):
            subject = (self.input_name_subject.text(), self.input_check_in.text(),
                       self.input_check_out.text(), str(self.cbdays.currentText()),
                       self.input_professor.text(), self.input_classroom.text())
            try:
                self.subject_db.add_subject(subject)
                if (self.input_check_out.time() > self.input_check_in.time()):
                    QMessageBox.information(
                        self, "Información", "Asignatura agregada correctamente")
                    self.close()
                    self.main = Main()       
                else:
                     QMessageBox.information(
                        self, "Información", "Hora de salida mayor o igual a la de entrada")                                
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
                    "{0} --- Asignatura: {1} --- Aula: {2} --- Hora entrada: {3}".format(subject[0], subject[1], subject[6], subject[2]))
    
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
                    self.subject_db.delete_subject_by_id(subject[0])
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
                                <b>
                                   <br>
                                   <font size="5">
                                        <FONT COLOR='#000000'>{0}</FONT> 
                                  </br>
                                  <br>
                                    <font size="4">
                                        <FONT COLOR='#c7a500'>{1}</FONT>  
                                <font size="3">
                                    <br>
                                        {2}
                                    </br>
                                    <br>
                                        {3}
                                    </br>
                                    <br>
                                        {4}
                                    </br> 
                                    <br>
                                        {5}
                                    </br>
                                    <br>
                                        {6}
                                    </br> 
                                </font>
                                """.format(subject[0], subject[1],subject[2],subject[3],subject[4],subject[5],subject[6]))
                question = QMessageBox.information(self, "Informacion", question_text, QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar la asignatura que desea a mostrar")
    
    def update_subject(self):
        if self.state == 0:
            if self.subject_list.selectedItems():
                subject = self.subject_list.currentItem().text()
                id = subject.split(" --- ")[0]
                    
                subject = self.subject_db.get_subjects_by_id(id)

                if subject:
                    self.input_name_subject.setText("{0}".format(subject[1]))
                    #self.input_check_in.displayFormat(subject[2])
                    #self.input_day.setText("{0}".format(subject[4]))
                    self.input_professor.setText("{0}".format(subject[5]))
                    self.input_classroom.setText("{0}".format(subject[6]))
                    self.btn_update.setText("Guardar")
                    self.btn_new.setVisible(False)
                    self.btn_information.setVisible(False)
                    self.btn_delete.setVisible(False)
                    
                    self.state = 1
            else:
                QMessageBox.information(self, "Advertencia", "Favor seleccionar la asignatura que desea a actualizar")

        else:  
            #Obtengo el id de la selccion
            if self.subject_list.selectedItems() and self.input_name_subject.text() != "":
                subject = self.subject_list.currentItem().text()
                id = subject.split(" --- ")[0]
                subject = self.subject_db.get_subjects_by_id(id)
                
                try:
                    self.subject_db.update_subject_by_id((
                                                self.input_name_subject.text(), 
                                                self.input_check_in.text(),
                                                self.input_check_out.text(), 
                                                str(self.cbdays.currentText()), 
                                                self.input_professor.text(),
                                                self.input_classroom.text(),
                                                id
                                                ))
                    QMessageBox.information(self, "Información", "Datos de asignatura actualizadoss")
                    self.subject_list.clear()
                    self.set_subject_list()
                    self.vaciar_inputs()

                except Error as e:
                    QMessageBox.information(
                        self, "Error", "Error al momento de actualizar la asignatura")
            else:
                QMessageBox.information(
                    self, "Advertencia", "Debes ingresar toda la informacion")
            self.btn_update.setText("Modificar")
            self.btn_new.setVisible(True)
            self.btn_information.setVisible(True)
            self.btn_delete.setVisible(True)
            self.state = 0           
            
    def vaciar_inputs(self):
        """
        Deja vacio los inputs sin los valores que le cargue.
        """
        self.input_name_subject.setText("") 
        #self.input_day.setText("")
        self.input_professor.setText("")         
        self.input_classroom.setText("")             
        
            
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
	                                checkIn TIMESTAMP,
	                                checkOut TIMESTAMP,
	                                day TEXT,
	                                professor TEXT,
	                                classroom TEXT,
	                                CONSTRAINT UQ_nameSubject UNIQUE (nameSubject)
                                    CONSTRAINT CK_CheckOut_greater_than_checkIn CHECK (checkOut > checkIn)
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
                        nameSubject, checkIn, checkOut,
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
        sqlQuery = " SELECT * FROM subject WHERE idSubject = ?"

        try:
            cursor = self.connection.cursor()
            # fetchone espera que se retorne una tupla (1,)
            subject = cursor.execute(sqlQuery, (id,)).fetchone()
            
            return subject
        except Error as e:
            print(e)

        return None

    def delete_subject_by_id(self, id):
        """
        Elimina una asignatura mediante el valor del id.
        param: id: El valor de la asignatura.
        :return: True si la asginatura se eliminó. None en caso contrario.
        """
        sqlQuery = "DELETE FROM subject WHERE idSubject = ?;"

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
        sqlUpdate= """
                        UPDATE subject
                        SET nameSubject = ?, 
                          checkIn = ?, 
                          checkOut = ?,
	                      day = ?, 
                          professor = ?, 
                          classroom = ?
                        WHERE idSubject = ?;
                   """

        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlUpdate, id)
            self.connection.commit()
        except Error as e:
            print(e)

        return None
        


# - - - - - - - -  W I D G E T  T A R E A - - - - - - - - - - -
class Interfaz_Tarea(QWidget):
    """
    Ventana princiapal de tarea
    """

    def __init__(self):
        super().__init__()
        self.tarea_db = TareaBd("lemilion.bd")
        self.setWindowTitle("Tarea")
        self.setGeometry(450, 80, 457,609)
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
        self.btn_retorno.clicked.connect(self.add_MenuAgenda)

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
        self.label_Asignatura = QLabel("Asignaura: ")
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
                self.vaciar_inputs()
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
                    
                tarea = self.tarea_db.tarea_por_nombre(id)

                if tarea:
                    self.input_Asignatura.setText("{0}".format(tarea[1]))
                    
                    self.input_Tarea.setText("{0}".format(tarea[2]))

                    self.input_fecha_de_entrega.setText("{0}".format(tarea[3])) 
                    
                    self.input_categria_tarea.setText("{0}".format(tarea[4])) 
                    
                    self.input_detalle.setText("{0}".format(tarea[5]))
                    self.btn_update.setText("Guardar")

                    self.btn_agregar.setVisible(False)
                    self.btn_delete.setVisible(False)
                    self.btn_Mostrar.setVisible(False)
                    self.estado = 1

        else:  
            #Obtengo el id de la selccion
            if self.homework_List.selectedItems() and self.input_Tarea.text() != "":

                #campo = (self.input_Tarea.text())

                tarea = self.homework_List.currentItem().text()
                id = tarea.split(" --- ")[0]
                tarea = self.tarea_db.tarea_por_nombre(id)

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
            self.btn_agregar.setVisible(True)
            self.btn_delete.setVisible(True)
            self.btn_Mostrar.setVisible(True)
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

            tarea = self.tarea_db.tarea_por_nombre(id)

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

            tarea = self.tarea_db.encontrar_tarea_por_nombre(id)

            if tarea:
                question_text = ("""
                                <b>
                                    <br>
                                    <font size="5">
                                        <FONT COLOR='#000000'>{0}</FONT>
                                    </b>
                                </br>

                                <br>
                                    <font size="4">
                                        <FONT COLOR='#c7a500'>{1}</FONT>
                                    </br>
                                    
                                <font size="3">
                                    <br>
                                        {2}
                                    </br>
                                    <br>
                                        {3}
                                    </br>
                                    <br>
                                        {4}
                                    </br> 
                                </font>
                                """.format(tarea[1],tarea[2],tarea[3],tarea[4],tarea[5]))
                question = QMessageBox.about(self,"Tarea","{0}".format(question_text))

    #Metodo para retornar a la ventana anterior
    def add_MenuAgenda(self):
        self.Menu_Agenda = AgendaMenu()
        self.close()

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
                                    idSubject INTEGER,
                                    Tarea TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    IdCategoria INTEGER,
                                    Detalles TEXT,
                                    FOREIGN KEY (IdCategoria) REFERENCES CategoriaTarea (IdCategoria),
                                    FOREIGN KEY (idSubject) REFERENCES subject (idSubject)
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

    def encontrar_tarea_por_nombre(self,id_Tarea):
        """ Busca una tarea mediante el valor del id"""
        sqlQuery = """
                        SELECT A.IdTArea, IdAsignatura, A.Tarea, A.Fecha,B.NombreCategoria, A.Detalles
                        FROM Tarea A INNER JOIN CategoriaTarea B 
                        ON A.IdCategoria = B.IdCategoria WHERE A.Tarea = ?;
                  """

        try:
            cursor = self.connection.cursor()
            tarea = cursor.execute(sqlQuery, (id_Tarea,)).fetchone()

            return tarea
        except Error as e:
            print(e)

        return None

    def tarea_por_nombre(self,id_Tarea):
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

# - - - - - - - -  W I D G E T  E X A M E N - - - - - - - - - - -
class Interfaz_Examen(QWidget):
    """
    Ventana principal de examen.
    """
    def __init__(self):
        super().__init__()
        self.examen_db = examenBd("lemilion.bd")
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
        self.input_Exam.setPlaceholderText("Tema de examen examen")
        self.label_Present = QLabel("Presentacion: ")
        self.input_Present = QLineEdit()
        self.input_Present.setPlaceholderText("dia/mes/año")
        self.label_category = QLabel("Categoria: ")
        self.input_category = QLineEdit()
        self.input_category.setPlaceholderText("1: Escrito, 2: Virtual, 3: Practico")
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
                    #self.close()
                    #self.main = Exam_interfaz()
                    self.exam_list.clear()
                    self.set_exam_list()
                    self.vaciar_inputs()

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
                    """{0} --- {1} Fecha:{2} """.format(examen[0], examen[1], examen[3]))
   
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

            examen = self.examen_db.encontrar_examen_por_id(id)

            if examen:
                question_text = ("""
                                <b>
                                    <br>
                                    <font size="5">
                                        <FONT COLOR='#000000'>{0}</FONT>
                                    </b>
                                </br>

                                <br>
                                    <font size="4">
                                        <FONT COLOR='#c7a500'>{1}</FONT>
                                    </br>
                                    
                                <font size="3">
                                    <br>
                                        {2}
                                    </br>
                                    <br>
                                        {3}
                                    </br>
                                    <br>
                                        {4}
                                    </br> 
                                </font>
                                """.format(examen[1],examen[2],examen[3],examen[4],examen[5]))
                question = QMessageBox.about(self,"examen","{0}".format(question_text))

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
                                    idSubject INTEGER,
                                    Examen TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    IdCategoria INTEGER,
                                    Detalles TEXT,
                                    FOREIGN KEY (IdCategoria) REFERENCES Categoriaexamen (IdCategoria)
                                    FOREIGN KEY (idSubject) REFERENCES subject (idSubject)
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

      
    def encontrar_examen_por_id(self,id):
        """ Busca una examen mediante el valor del id"""
        sqlQuery = """
                        SELECT A.IdExamen, IdAsignatura, A.Examen, A.Fecha,B.NombreCategoria, A.Detalles
                        FROM Examen A INNER JOIN CategoriaExamen B 
                        ON A.IdCategoria = B.IdCategoria WHERE A.IdExamen = ?;
                  """

        try:
            cursor = self.connection.cursor()
            examen = cursor.execute(sqlQuery, (id,)).fetchone()

            return examen
        except Error as e:
            print(e)

        return None
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



# - - - - - - - -  W I D G E T  E V E N T O - - - - - - - - - - -
class Interfaz_Evento(QWidget):
    """
    Ventana Principal del Evento
    """
    def __init__(self):
        super().__init__()
        self.evento_db = EventoBd("lemilion.bd")
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
                    """{0} --- {1} --- {2} """.format(evento[1], evento[2], evento[3]))

    def ultimo_conjunto_eventos(self):
        """
        Ultimo registro de eventos
        """

        eventos = self.evento_db.obtener_ultimo_evento()

        if eventos:
            for evento in eventos:
                self.evento_list.addItem(
                    """{0} --- {1} --- {2} """.format(evento[1], evento[2], evento[3]))

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
                id = evento.split(" --- ")[1]

                evento = self.evento_db.evento_por_id(id)

                if evento:
                    self.input_name_subject.setText("{0}".format(evento[1]))
                    self.input_name_event.setText("{0}".format(evento[2]))
                    self.input_name_date.setText("{0}".format(evento[3]))
                    self.input_name_location.setText("{0}".format(evento[4]))
                    self.input_name_detail.setText("{0}".format(evento[5]))
                    self.btn_update.setText("Guardar")
                    self.btn_new.setVisible(False)
                    self.btn_view.setVisible(False)
                    self.btn_delete.setVisible(False)
                    self.estado = 1
            else:
                QMessageBox.information(self, "Advertencia", "Favor seleccionar el evento que desea a actualizar")

        else:
            #Obteniendo el id seleccionado
            if self.evento_list.selectedItems() and self.input_name_event.text() != "":
                evento = self.evento_list.currentItem().text()
                id = evento.split(" --- ")[1]
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
            self.btn_new.setVisible(True)
            self.btn_view.setVisible(True)
            self.btn_delete.setVisible(True)
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
            id = evento.split(" --- ")[1]

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
            id = evento.split(" --- ")[1]

            evento = self.evento_db.evento_por_id(id)

            if evento:
                question_text = ("""
                                <b>
                                    <br>
                                    <font size="5">
                                        <FONT COLOR='#000000'>{0}</FONT>
                                    </b>
                                </br>

                                <br>
                                    <font size="4">
                                        <FONT COLOR='#c7a500'>{1}</FONT>
                                    </br>
                                    
                                <font size="3">
                                    <br>
                                        {2}
                                    </br>
                                    <br>
                                        {3}
                                    </br>
                                    <br>
                                        {4}
                                    </br> 
                                </font>
                                """.format(evento[1],evento[2],evento[3],evento[4],evento[5]))
                question = QMessageBox.about(self,"evento","{0}".format(question_text))


        else:
            QMessageBox.information(self, "Advertencia", "Favor seleccionar el evento que desea a mostrar")
    


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
                                    idSubject INTEGER,
                                    Evento TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    Ubicacion TEXT NOT NULL,
                                    Detalle TEXT,
                                    FOREIGN KEY (IdAsignatura) REFERENCES AsignaturaEvento (IdAsignatura)
                                    FOREIGN KEY (idSubject) REFERENCES subject (idSubject)
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
                        Detalle = ?
                    WHERE IdEvento = ?;
                    """
        try:
            cursor = self.connection.cursor()
            cursor.execute(sqlUpdate, EventoT)
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
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    


        