from PyQt5 import QtWidgets 
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
from os import path
import os
from PyQt5.uic import loadUiType

#FORM_CLASS,_ = loadUiType(path.join(path.dirname("__file__"),"inventory.ui"))

import sqlite3

#For Installation File 
def resource_path(relative_path):
    base_path = getattr(sys,'METPASS',os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path,relative_path)

FORM_CLASS,_ = loadUiType(resource_path("inventory.ui"))

class Main(QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Navigate()
        self.counter = 1

    def Handel_Buttons(self):
        self.refresh_btn.clicked.connect(self.GET_DATA)
        self.search_btn.clicked.connect(self.SEARCH)
        self.check_btn.clicked.connect(self.LEVEL)
        self.add_btn.clicked.connect(self.ADD)
        self.delete_btn.clicked.connect(self.DELETE)
        self.update_btn.clicked.connect(self.UPDATE)
        self.search_btn_2.clicked.connect(self.SEARCH_RECORD)
    
    def SEARCH_RECORD(self):
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        record_id = self.ID_Input_1.text()
        command = ''' SELECT * FROM parts_table WHERE ID=?'''
        result = db.execute(command,[record_id])
        
        val = result.fetchone()
        
        self.ID_Input_1.setValue(int(val[0]))
        self.Ref_Input.setText(str(val[1]))
        self.Part_Name_Input.setText(str(val[2]))
        self.Min_Area_Input.setText(str(val[3]))
        self.Max_Area_Input.setText(str(val[4]))
        self.Nbr_of_holes_Input.setText(str(val[5]))
        self.Min_Diameter_Input.setText(str(val[6]))
        self.Max_Diameter_Input.setText(str(val[7]))
        self.Count_SPinBOx_input.setValue(int(val[8]))
  
    def PREVIOUS(self):
        if self.counter >=0:
            #db = sqlite3.connect("part.db")
            db = sqlite3.connect(resource_path("part.db"))
            cursor = db.cursor()
           
            command = ''' SELECT * FROM parts_table WHERE ID=?'''
            result = db.execute(command,[self.counter])
            
            val = result.fetchone()
            
            self.ID_Display_label.setText(str(val[0]))
            self.Ref_Input.setText(str(val[1]))
            self.Part_Name_Input.setText(str(val[2]))
            self.Min_Area_Input.setText(str(val[3]))
            self.Max_Area_Input.setText(str(val[4]))
            self.Nbr_of_holes_Input.setText(str(val[5]))
            self.Min_Diameter_Input.setText(str(val[6]))
            self.Max_Diameter_Input.setText(str(val[7]))
            self.Count_SPinBOx_input.setValue(int(val[8]))
            
            self.counter -=1
        else:
            print("Error")
    
    def NEXT(self):
        if self.counter >=0:
            #db = sqlite3.connect("part.db")
            db = sqlite3.connect(resource_path("part.db"))
            cursor = db.cursor()
           
            command = ''' SELECT * FROM parts_table WHERE ID=?'''
            result = db.execute(command,[self.counter])
            
            val = result.fetchone()
            
            self.id_spinbox.setValue(int(val[0]))
            self.Ref_Input.setText(str(val[1]))
            self.Part_Name_Input.setText(str(val[2]))
            self.Min_Area_Input.setText(str(val[3]))
            self.Max_Area_Input.setText(str(val[4]))
            self.Nbr_of_holes_Input.setText(str(val[5]))
            self.Min_Diameter_Input.setText(str(val[6]))
            self.Max_Diameter_Input.setText(str(val[7]))
            self.Count_SPinBOx_input.setValue(int(val[8]))
            
            self.counter +=1
        else:
            print("Error")
    
    def DELETE(self):
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        
        record_id = self.ID_Input_1.text()
        
        command = ''' DELETE FROM parts_table WHERE ID = ?'''
        
        cursor.execute(command,[record_id])
        
        db.commit()
        
    def UPDATE(self):
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        record_id = self.ID_Input_1.text()
        
        reference = self.Ref_Input.text()
        part_name = self.Part_Name_Input.text()
        min_area =  self.Min_Area_Input.text()
        max_area = self.Max_Area_Input.text()
        number_of_holes = self.Nbr_of_holes_Input.text()
        min_diameter = self.Min_Diameter_Input.text()
        max_diameter = self.Max_Diameter_Input.text()
        count_ = self.Count_SPinBOx_input.text()
        
        
        row = (reference,part_name,min_area,max_area,number_of_holes,min_diameter,max_diameter,count_,record_id)
        
        command = ''' UPDATE parts_table SET Reference=?,PartName=?,MinArea=?,MaxArea=?,NumberOfHoles=?,MinDiameter=?,MaxDiameter=?,CounT = ? WHERE ID = ?'''
        cursor.execute(command,row)
        db.commit()
        
        
        
    def ADD(self):
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        
        
        reference = self.Ref_Input.text()
        part_name = self.Part_Name_Input.text()
        min_area =  self.Min_Area_Input.text()
        max_area = self.Max_Area_Input.text()
        number_of_holes = self.Nbr_of_holes_Input.text()
        min_diameter = self.Min_Diameter_Input.text()
        max_diameter = self.Max_Diameter_Input.text()
        count_ = self.Count_SPinBOx_input.text()
        
        
        row = (reference,part_name,min_area,max_area,number_of_holes,min_diameter,max_diameter,count_)
        
        command = ''' INSERT INTO parts_table(Reference,PartName,MinArea,MaxArea,NumberOfHoles,MinDiameter,MaxDiameter,Count) VALUES (?,?,?,?,?,?,?,?)'''
        cursor.execute(command,row)
        db.commit()
    
    def LEVEL(self):
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        
        command = ''' SELECT Reference,PartName,Count FROM parts_table order by Count asc LIMIT 3 '''
        
        result = cursor.execute(command)
        
        self.table2.setRowCount(0)
        
        for row_number , row_data in enumerate(result):
            self.table2.insertRow(row_number)
            for column_number , data in enumerate(row_data):
                self.table2.setItem(row_number,column_number,QTableWidgetItem(str(data)))
    
    def SEARCH(self):
        
       
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        
        command = ''' SELECT * FROM parts_table WHERE Count <=? '''
        nbr = int(self.ref_filter_box.text())
        result = cursor.execute(command,[nbr])
        
        self.Table.setRowCount(0)
        
        for row_number , row_data in enumerate(result):
            self.Table.insertRow(row_number)
            for column_number , data in enumerate(row_data):
                self.Table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        
    def GET_DATA(self):
        
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        
        command = ''' SELECT * FROM parts_table '''
        
        result = cursor.execute(command)
        
        self.Table.setRowCount(0)
        
        for row_number , row_data in enumerate(result):
            self.Table.insertRow(row_number)
            for column_number , data in enumerate(row_data):
                self.Table.setItem(row_number,column_number,QTableWidgetItem(str(data)))
                
                
        cursor2 = db.cursor()
        cursor3 = db.cursor()
        
        parts_nbr = ''' SELECT COUNT (DISTINCT PartName) from parts_table'''
        ref_nbr = ''' SELECT COUNT (DISTINCT Reference) from parts_table'''
        
        result_ref_nbr = cursor2.execute(ref_nbr)
        result_parts_nbr = cursor3.execute(parts_nbr)
        

        self.lbl_chnge_ref.setText(str(result_ref_nbr.fetchone()[0]))
        self.lbl_chnge_part.setText(str(result_parts_nbr.fetchone()[0]))
        
        
        
        cursor4 = db.cursor()
        cursor5 = db.cursor()
        
        min_hole = '''SELECT MIN(NumberOfHoles),Reference from parts_table '''
        max_hole = '''SELECT MAX(NumberOfHoles),Reference from parts_table '''
        
        
        result_min_hole = cursor4.execute(min_hole)
        result_max_hole = cursor5.execute(max_hole)
        
        r1 = result_min_hole.fetchone()
        r2 = result_max_hole.fetchone()   
        
        self.lbl_chnge_min_hole.setText(str(r1[0]))
        self.lbl_chnge_max_hole.setText(str(r2[0]))
        

        self.lbl_hole_ref_1.setText(str(r1[1]))
        self.lbl_hole_ref_2.setText(str(r2[1]))
        
        
        
        
    def Navigate(self):
        #db = sqlite3.connect("part.db")
        db = sqlite3.connect(resource_path("part.db"))
        cursor = db.cursor()
        
        command = ''' SELECT * FROM parts_table'''
        result = db.execute(command)
        
        val = result.fetchone()
        
        self.ID_Input_1.setValue(int(val[0]))
        self.Ref_Input.setText(str(val[1]))
        self.Part_Name_Input.setText(str(val[2]))
        self.Min_Area_Input.setText(str(val[3]))
        self.Max_Area_Input.setText(str(val[4]))
        self.Nbr_of_holes_Input.setText(str(val[5]))
        self.Min_Diameter_Input.setText(str(val[6]))
        self.Max_Diameter_Input.setText(str(val[7]))
        self.Count_SPinBOx_input.setValue(int(val[8]))
        
        
def main():
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()