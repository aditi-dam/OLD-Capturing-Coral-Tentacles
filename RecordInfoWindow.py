import sys

from PhotoLabel import PhotoLabel

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import mysql.connector as mc
import os

from PIL import Image, ImageTk
from datetime import date

import cv2 as cv
import numpy as np
from Image import Image


class RecordInfoWindow(QWidget):
    #code = 0
    #id = 1
    submitButton = None
    #today = date.today()
    
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        #self.id = GalleryInfoWindow.code
        
        self.name_of_person_Label = QLabel("Name:")
        self.name_of_person_Display = QLineEdit()
        self.name_of_person_Display.setPlaceholderText("Enter your name here")
        
        self.notes_Label = QLabel("Notes:")
        self.notes_Display = QLineEdit()
        self.notes_Display.setPlaceholderText("Enter any notes you have")
        
        self.date_Label = QLabel("Date Added:")
        self.date_Display = QLabel("{0}".format(date.today()))
        
        self.submitButton = None
        self.submitButton = QPushButton("SUBMIT!")
        #self.submitButton.clicked.connect(self.show_line)
        
        layout.addWidget(self.date_Label, 0, 0)
        layout.addWidget(self.date_Display, 0, 1)
        layout.addWidget(self.name_of_person_Label, 1, 0)
        layout.addWidget(self.name_of_person_Display, 1, 1)
        layout.addWidget(self.notes_Label, 2, 0)
        layout.addWidget(self.notes_Display, 2, 1)
        layout.addWidget(self.submitButton, 3, 0)
        
        print(self.name_of_person_Display.text())
        
        #layout.addWidget(self.label)
        self.setLayout(layout)
 
    #def get_id(self):
    #    return self.id  
    
    def get_name(self):
        return self.name_of_person_Display.text()
    
    def get_notes(self):
        return self.notes_Display.text()

    
    # def show_line(self):
    #     #print(Image.path)
    #     #print(self.name_of_person_Display.text())
    #     GalleryInfoWindow.code += 1
        
    #     try:
    #         mydb = mc.connect(
    #             host=os.environ.get('HOST'),
    #             user=os.environ.get('USERNAME'),
    #             password=os.getenv('PASSWORD'), 
    #             database=os.getenv('DATABASE')             
    #         )
                        

    #         mySql_insert_query = """INSERT INTO image_info
    #                                 VALUES (2, "Hi", 2, "Aditi", DATE '2015-12-17') """
            
            
    #                     #"""INSERT INTO image_info (self.id, self.photo_filename, 3, self.name_of_person_Display, date.today()) 
    #                       #              VALUES (%s, %s, %s, %s, %s) """
            

                            
                            
                           
    #         mycursor = mydb.cursor()
            
    #         mycursor.execute(mySql_insert_query)
    #         mydb.commit()

    #         #QMessageBox.about(self, "Connection", "Database Connected Successfully")
    #         print(mydb)
    #         self.close()
    #         mydb.close()
    #     except mydb.Error as e:
    #        print("Failed To Connect to Database")
            
        
    
    
