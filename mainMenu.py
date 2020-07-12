import sqlite3
import sys 

from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QApplication 
from UI_Menu import * 
class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()        
        self.ui.setupUi(self)                  
        self.ui.btn_clear.clicked.connect(self.reset) 
        self.ui.btn_tambah.clicked.connect(self.addData)    
        self.ui.btn_delete.clicked.connect(self.deleteData)
        self.ui.btn_view.clicked.connect(self.viewData)
             
        self.show()

    def showMessage(self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    
        
    def viewData(self):
         connection = sqlite3.connect("databasenya.db")
         query="SELECT * FROM pengunjung"
         result=connection.execute(query)
         self.ui.tableWidget.setRowCount(0)
         for row_number,row_data in enumerate(result):
             self.ui.tableWidget.insertRow(row_number)
             for column_number,data in enumerate(row_data):
                 self.ui.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
         connection.close()
         
    def addData(self):
        nomor_pengunjung= self.ui.txtnp.text()
        nama = self.ui.txtnm.text()
        alamat= self.ui.txtal.text()
        jenis_kelamin= self.ui.txtjk.text()
        no_tlp = self.ui.txtnt.text()
        email= self.ui.txtem.text()
        tgl_kunjungan=self.ui.txttgl.text()
        status=self.ui.txtst.text()
        connection  = sqlite3.connect("databasenya.db")
        
        if nomor_pengunjung == "" or nama == "" or alamat == "" or jenis_kelamin == "" or no_tlp == "" or email == "":
            self.showMessage('Pesan','Field tidak boleh kosong')
        else:
            connection.execute("INSERT INTO pengunjung VALUES(?,?,?,?,?,?,?,?)",
            (nomor_pengunjung,nama,alamat,jenis_kelamin,no_tlp,email,tgl_kunjungan,status))
            connection.commit()
            connection.close()
            self.showMessage('Pesan','berhasil ditambahkan')
        
    def reset(self):
        nomor_pengunjung= self.ui.txtnp.text()
        nama = self.ui.txtnm.text()
        alamat= self.ui.txtal.text()
        jenis_kelamin= self.ui.txtjk.text()
        no_tlp = self.ui.txtnt.text()
        email= self.ui.txtem.text()
        tgl_kunjungan=self.ui.txttgl.text()
        status=self.ui.txtst.text()
        
        if nomor_pengunjung == "" and nama == "" and alamat == "" and jenis_kelamin == "" and no_tlp == "" and email == "":
            self.showMessage('Pesan','Field  kosong')
        else:
            self.ui.txtnp.setText("")
            self.ui.txtnm.setText("")
            self.ui.txtal.setText("")
            self.ui.txtjk.setText("")
            self.ui.txtnt.setText("")
            self.ui.txtem.setText("")
            self.ui.txttgl.setText("")
            self.ui.txtst.setText("")
            
    def deleteData(self):
        nomor_pengunjung= self.ui.txtnp.text()
        if nomor_pengunjung == "":
            self.showMessage('Pesan','masukan no pengunjung')
            
        else:
            connection = sqlite3.connect("databasenya.db")
            connection.execute("DELETE FROM pengunjung WHERE nomor_pengunjung="+str(nomor_pengunjung))
            self.showMessage('Pesan','berhasil dihapus')
            connection.commit()
            connection.close()
      
        
     
if __name__=="__main__":
    app = QApplication(sys.argv)    
    w = MyForm()    
    w.show()    
    sys.exit(app.exec_())
