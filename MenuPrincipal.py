# -*- coding: utf-8 -*-
#Programa: PrimeraPAntalla
#Objetivo: 
# Autor: Nova
# Fecha: 16/Marzo/2020


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon, QRegion
import sys
import os
import platform
import sqlite3
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
        self.setWindowTitle("Lemilion?")
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
# - - - - - - - -  W I D G E T  T A R E A - - - - - - - - - - -

class InterfazAsignatura(QWidget):
    """
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Asignatura")
        self.setGeometry(450, 450, 457, 609)
        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        """
        Menú que añade una asignatura y ve sus detalles
        """
        self.title = QLabel("Agregar Asignatura")
        self.image = QLabel()        
        self.image.setPixmap(QPixmap("Resource/Asignatura_Banner.jpg"))
        
        self.asignature_list = QListWidget()     
        self.btn_new = QPushButton("Agregar")
      # self.btn_new.clicked.connect(self.add_subject)
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")
        
        # Center Layout Widgets
        self.label_name_subject = QLabel("Nombre Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Cálculo")
        self.label_time_in= QLabel("Hora de entrada: ")
        self.input_time_in = QLineEdit()
        self.input_time_in.setPlaceholderText("12:00 p.m.")
        self.label_time_out= QLabel("Hora de salida: ")
        self.input_time_out = QLineEdit()
        self.input_time_out.setPlaceholderText("1:00 p.m.")
        self.label_day = QLabel("Día: ")
        self.input_day = QLineEdit()
        self.input_day.setPlaceholderText("Lunes")
        self.label_professor = QLabel("Catedrático: ")
        self.input_professor = QLineEdit()
        self.input_professor.setPlaceholderText("Wade Wilson")
        self.label_classroom = QLabel("Aula: ")
        self.input_classroom = QLineEdit()
        self.input_classroom.setPlaceholderText("125") 
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        # Layouts
        
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
        self.bottom_main_layout = QVBoxLayout()
        self.bottom_central_layout = QHBoxLayout()
        
        # Agregar los layouts hijos al layout padre
        # Layout fondo
        self.All_layout.addLayout(self.main_title, 10)
        self.All_layout.addLayout(self.main_layout, 90)
        
         # Layout titulo
        self.main_title.addWidget(self.image)
        # alignment=Qt.AlignHCenter
        # Layout principal
        self.main_layout.addLayout(self.central_main_layout, 40)
        self.main_layout.addLayout(self.bottom_main_layout, 60)
              
        # Layout central
        self.central_main_layout.addLayout(self.central_center_layout, 90)
        self.central_main_layout.addLayout(self.central_bottom_layout, 10)
                       
        # funciones de escribir datos layout central
        self.central_center_layout.addRow(self.label_name_subject , self.input_name_subject)
        self.central_center_layout.addRow(self.label_time_in , self.input_time_in )
        self.central_center_layout.addRow(self.label_time_out , self.input_time_out )
        self.central_center_layout.addRow(self.label_day , self.input_day )
        self.central_center_layout.addRow(self.label_professor , self.input_professor )
        self.central_center_layout.addRow(self.label_classroom , self.input_classroom )
        
        # Botones layout central inferior
        self.central_bottom_layout.addWidget(self.btn_new)
        self.central_bottom_layout.addWidget(self.btn_update)
        self.central_bottom_layout.addWidget(self.btn_delete)
        
         # Layout inferior
        self.bottom_main_layout.addLayout(self.bottom_central_layout)
        
         # Agregar widgets a los layouts
        # Lista de asignaturas lado inferior
        self.bottom_central_layout.addWidget(self.asignature_list)
        
        #Colocar el layout principal en la ventana principal
        self.setLayout(self.All_layout)

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
                                    IdAsignatura INTEGER,
                                    Tarea TEXT NOT NULL,
                                    Fecha TEXT NOT NULL,
                                    IdCategoria INTEGER,
                                    Detalles TEXT,
                                    FOREIGN KEY (IdCategoria) REFERENCES CategoriaTarea (IdCategoria)
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
    Ventana principal de la aplicacion.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen")
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
        self.tittle = QLabel("E X A M E N ")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(457)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)
        
        self.tittle.adjustSize()

        self.exam_list = QListWidget()   
        self.btn_new = QPushButton("Agregar")
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
        self.input_Present.setPlaceholderText("Fecha de presentacion")

        self.label_category = QLabel("Categoria: ")
        self.input_category = QLineEdit()
        self.input_category.setPlaceholderText("Añadir una categoria")

        self.label_detail = QLabel("Detalle : ")
        self.input_detail = QLineEdit()
        self.input_detail.setPlaceholderText("Agregar un detalle")
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        self.main_layout = QVBoxLayout()
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.botones_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()
    
      # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.down_layout.addWidget(self.exam_list)

        # Agregar los widgets (childrens) al main_layout
        self.main_layout.addLayout(self.top_layout,30)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.botones_layout,10)
        self.main_layout.addLayout(self.down_layout)
        
        #bottom
        self.bottom_layout.addRow(self.label_Asignature, self.input_Asignature)
        self.bottom_layout.addRow(self.label_Exam, self.input_Exam)
        self.bottom_layout.addRow(self.label_Present, self.input_Present)
        self.bottom_layout.addRow(self.label_category, self.input_category)
        self.bottom_layout.addRow(self.label_detail, self.input_detail)

        self.botones_layout.addWidget(self.btn_new)
        self.botones_layout.addWidget(self.btn_update)
        self.botones_layout.addWidget(self.btn_delete)
        
        self.setLayout(self.main_layout)

# - - - - - - - -  W I D G E T  E V E N T O - - - - - - - - - - -
class Interfaz_Evento(QWidget):
    """
    Ventana Principal de la Aplicacion
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Evento")
        self.setGeometry(450, 450, 457,609)
        self.UI()
        self.show()

    def UI(self):
        self.main_design()
        self.layouts()

    def main_design(self):
        """
        Menu que contendra un evento y muestra sus detalles
        """
        self.tittle = QLabel("E V E N T O")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(457)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)

        self.tittle.adjustSize()

        self.evento_list = QListWidget()
        self.btn_new = QPushButton("Agregar")
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")

        self.label_name_subject = QLabel("Asignatura: ")
        self.input_name_subject = QLineEdit()
        self.input_name_subject.setPlaceholderText("Agregar una asignatura")

        self.label_name_event = QLabel("Evento: ")
        self.input_name_event = QLineEdit()
        self.input_name_event.setPlaceholderText("Agregar un evento")
        
        self.label_name_date = QLabel("Fecha: ")
        self.input_name_date = QLineEdit()
        self.input_name_date.setPlaceholderText("Agregar fecha")
        
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
        self.top_layout = QVBoxLayout()
        self.button_layout = QFormLayout()
        self.boton_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()

        # Agregar los widgets al top_layout
        self.top_layout.addWidget(self.tittle)
        self.down_layout.addWidget(self.evento_list)

        # Agregando los layouts hijos al layout padre
        self.main_layout.addLayout(self.top_layout, 30)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addLayout(self.boton_layout, 10)
        self.main_layout.addLayout(self.down_layout)

        self.button_layout.addRow(self.label_name_subject, self.input_name_subject)
        self.button_layout.addRow(self.label_name_event, self.input_name_event)
        self.button_layout.addRow(self.label_name_date, self.input_name_date)
        self.button_layout.addRow(self.label_name_location, self.input_name_location)
        self.button_layout.addRow(self.label_name_detail, self.input_name_detail)


        # Los botones que se posicionaran en la parte inferior
        self.boton_layout.addWidget(self.btn_new)
        self.boton_layout.addWidget(self.btn_update)
        self.boton_layout.addWidget(self.btn_delete)

        self.setLayout(self.main_layout)


def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    


        