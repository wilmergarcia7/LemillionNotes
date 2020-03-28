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



        self.btn_Agenda = QPushButton()
        self.btn_Agenda.setFixedWidth(60)
        self.btn_Agenda.setFixedHeight(60)
        self.btn_Agenda.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Agenda.setStyleSheet("""QPushButton { image :url(Resource/Agenda.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
        self.btn_Agenda.clicked.connect(self.add_MenuAgenda)
        
        #self.btn_Agenda.move(171,80)
    def layouts(self):
        """ Layouts que compone el menu principal"""
        #Layouts
        self.main_layout = QHBoxLayout()
        self.boton1_layout = QHBoxLayout()
        self.boton2_layout = QHBoxLayout()

        #Agregar layouts a layout
        self.main_layout.addLayout(self.boton1_layout)
        self.main_layout.addLayout(self.boton2_layout)

        #Agregar widgetc a los layouts
        self.boton1_layout.addWidget(self.btn_Agenda)
        self.boton2_layout.addWidget(self.btn_Asignatura)

        #Colocar el layout priniapl en la ventana principal
        self.setLayout(self.main_layout)

    def add_MenuAgenda(self):
        self.Menu_Agenda = AgendaMenu()
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

        #Botones
        self.btn_Tarea = QPushButton()
        self.btn_Tarea.setFixedWidth(60)
        self.btn_Tarea.setFixedHeight(60)
        self.btn_Tarea.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Tarea.setStyleSheet("""QPushButton { image :url(Resource/Tarea_Icon.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)



        self.btn_Examen = QPushButton()
        self.btn_Examen.setFixedWidth(60)
        self.btn_Examen.setFixedHeight(60)
        self.btn_Examen.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Examen.setStyleSheet("""QPushButton { image :url(Resource/Examen_Icon.jpg); 
                                                        border-radius: 30px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
  


        self.btn_Evento = QPushButton()
        self.btn_Evento.setFixedWidth(60)
        self.btn_Evento.setFixedHeight(60)
        self.btn_Evento.setMask(QRegion(QRect(-1,-1,60,60), QRegion.Ellipse))
        self.btn_Evento.setStyleSheet("""QPushButton { image :url(Resource/Evento_Icon.jpg);
                                                        border-radius: 29.4px} 
                                            QPushButton:pressed {background-color: #D5939C;}
                                        """)
      
        
    def layouts(self):
        """ Layouts que compone el menu principal"""
        #Layouts
        self.main_layout = QHBoxLayout()
        self.botones_layout = QVBoxLayout()

        #Agregar layouts a layout
        self.main_layout.addLayout(self.botones_layout)

        #Agregar widgetc a los layouts
        self.botones_layout.addWidget(self.btn_Evento)
        self.botones_layout.addWidget(self.btn_Examen)
        self.botones_layout.addWidget(self.btn_Tarea)

        #Colocar el layout priniapl en la ventana principal
        self.setLayout(self.main_layout)





def main():
    app = QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()    


        