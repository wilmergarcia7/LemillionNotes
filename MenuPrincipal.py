# -*- coding: utf-8 -*-
#Programa: PrimeraPAntalla
#Objetivo: 
# Autor: Nova
# Fecha: 16/Marzo/2020


from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QFont, QIcon, QRegion
import sys
import os

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
        self.setWindowTitle("Lemilion")
        self.setGeometry(450, 450, 457,609)
        
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
        self.layouts()

    def main_design(self):
        """
        Disign principal of aplication
        """
        self.btn_Asignatura = QPushButton()
        self.btn_Asignatura.setFixedWidth(60)
        self.btn_Asignatura.setFixedHeight(60)
        self.btn_Asignatura.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Asignatura.setStyleSheet("""QPushButton { image :url(Resource/Asignatura.jpg);
                                                        border-radius: 100px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                            """)
        self.label_Asignatura = QLabel("Asignatura")
        self.label_Asignatura.setStyleSheet("""font: bold 14px;""")
        self.label_Asignatura.setFixedHeight(20)
        self.label_Asignatura.setFixedWidth(80)



        self.btn_Agenda = QPushButton()
        self.btn_Agenda.setFixedWidth(60)
        self.btn_Agenda.setFixedHeight(60)
        self.btn_Agenda.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Agenda.setStyleSheet("""QPushButton { image :url(Resource/Agenda.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                            QLabel 
                                        """)
        self.label_Agenda = QLabel("Agenda")
        self.label_Agenda.setStyleSheet("""font: bold 14px;""")
        self.label_Agenda.setFixedHeight(20)
        self.label_Agenda.setFixedWidth(60)
        self.btn_Agenda.clicked.connect(self.add_MenuAgenda)
        
        #self.btn_Agenda.move(171,80)
    def layouts(self):
        """ Layouts que compone el menu principal"""
        #Layouts
        self.main_layout = QVBoxLayout()
        self.boton_layout = QHBoxLayout()
      

        #Agregar layouts a layout
        self.main_layout.addLayout(self.boton_layout)


        #Agregar widgetc a los layouts
        self.boton_layout.addWidget(self.label_Agenda) 
        self.boton_layout.addWidget(self.btn_Agenda)
        self.boton_layout.addWidget(self.label_Asignatura)
        self.boton_layout.addWidget(self.btn_Asignatura)


        
        #Colocar el layout priniapl en la ventana principal
        self.setLayout(self.main_layout)

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
        self.setGeometry(450, 450, 457,609)
        
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
        Disign principal of aplication
        """

        #Botones
        self.btn_Tarea = QPushButton()
        self.btn_Tarea.setFixedWidth(60)
        self.btn_Tarea.setFixedHeight(60)
        self.btn_Tarea.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Tarea.setStyleSheet("""QPushButton { image :url(Resource/Tarea_Icon.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
        self.btn_Tarea.clicked.connect(self.add_InterfazTarea)
        self.label_Tarea = QLabel("Tarea")
        self.label_Tarea.setStyleSheet("""font: bold 14px;""")
        self.label_Tarea.setFixedHeight(20)
        self.label_Tarea.setFixedWidth(50)
        self.label_Tarea.setAlignment(Qt.AlignCenter)


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
        self.label_Examen.setStyleSheet("""font: bold 14px;""")
        self.label_Examen.setFixedHeight(20)
        self.label_Examen.setFixedWidth(60)
        self.label_Examen.setAlignment(Qt.AlignCenter)


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
        self.label_Evento.setStyleSheet("""font: bold 14px;""")
        self.label_Evento.setFixedHeight(20)
        self.label_Evento.setFixedWidth(60)
        self.label_Evento.setAlignment(Qt.AlignCenter)
        
        
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
        self.setWindowTitle("Tarea")
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
        self.tittle = QLabel("T A R E A ")
        self.tittle.setFixedHeight(70)
        self.tittle.setFixedWidth(457)
        self.tittle.setStyleSheet("""color: white;
                                    font-size: 30px;
                                    background-image: url(Resource/Banner.jpg);
                                    """)


        self.label_agregar_tarea = QLabel("  ")
        self.label_ver_tareas = QLabel("  ")
        self.tittle.adjustSize()
        self.homework_List = QListWidget()
        self.btn_agregar = QPushButton("Agregar")
        self.btn_update = QPushButton("Modificar")
        self.btn_delete = QPushButton("Eliminar")

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
        self.top_layout = QVBoxLayout()
        self.bottom_layout = QFormLayout()
        self.botones_layout = QHBoxLayout()
        self.down_layout = QVBoxLayout()

        # Agregar los widgets al top layout
        self.top_layout.addWidget(self.tittle)
        self.down_layout.addWidget(self.label_ver_tareas)
        self.down_layout.addWidget(self.homework_List)

        # Agregar los widgets (childrens) al main_layout
        self.main_layout.addLayout(self.top_layout,30)
        self.main_layout.addLayout(self.bottom_layout)
        self.main_layout.addLayout(self.botones_layout,10)
        self.main_layout.addLayout(self.down_layout)
        
        #bottom
        self.bottom_layout.addRow(self.label_agregar_tarea)
        self.bottom_layout.addRow(self.label_Asignatura, self.input_Asignatura)
        self.bottom_layout.addRow(self.label_Tarea, self.input_Tarea)
        self.bottom_layout.addRow(self.label_fecha_de_entrega, self.input_fecha_de_entrega)
        self.bottom_layout.addRow(self.label_categoria_tarea, self.input_categria_tarea)
        self.bottom_layout.addRow(self.label_detalle, self.input_detalle)

        self.botones_layout.addWidget(self.btn_agregar)
        self.botones_layout.addWidget(self.btn_update)
        self.botones_layout.addWidget(self.btn_delete)
        
        self.setLayout(self.main_layout)

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


        