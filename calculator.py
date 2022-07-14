import sys#sys kütüphanesi dahil edildi. 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow


class MainForm(QMainWindow):#mainfromdan bir nesne üretince aslında o nesne QMainWindow den üretilmiş olur
    
    def __init__(self):
        super(MainForm,self).__init__()
    
        self.setWindowTitle('Calculator')#başlık ismi
        self.setGeometry(200,200,500,500)#Soldan ve Üstten 200 hizalı, 500x500 lük pencere oluşturur.
        self.initUI()#initUI fonksiyonun çalışması için yazdık

    def initUI(self):#from içindeki tüm kontrolleri burada yapıcağız
       
       self.lbl_sayi1=QtWidgets.QLabel(self)#self diyoruz çünkü nesneyle ilişkilenmesi gerekli
       self.lbl_sayi1.setText('sayi 1: ')
       self.lbl_sayi1.move(50,30)
       
    
       self.txt_sayi1=QtWidgets.QLineEdit(self)
       self.txt_sayi1.move(150,30)
       self.txt_sayi1.resize(200,32)

       self.lbl_sayi2=QtWidgets.QLabel(self)
       self.lbl_sayi2.setText('sayi 2: ')
       self.lbl_sayi2.move(50,80)
 
       self.txt_sayi2=QtWidgets.QLineEdit(self)
       self.txt_sayi2.move(150,80)
       self.txt_sayi2.resize(200,32)

       self.btn_topla=QtWidgets.QPushButton(self)
       self.btn_topla.setText("topla")
       self.btn_topla.move(150,130)
       self.btn_topla.clicked.connect(self.hesaplama)#topla butonuna tıklandığında hesaplama fonksiyonu çalışacak


       self.btn_cikar=QtWidgets.QPushButton(self)
       self.btn_cikar.setText("çıkar")
       self.btn_cikar.move(150,170)
       self.btn_cikar.clicked.connect(self.hesaplama)

       self.btn_carpma=QtWidgets.QPushButton(self)
       self.btn_carpma.setText("çarpma")
       self.btn_carpma.move(150,210)
       self.btn_carpma.clicked.connect(self.hesaplama)
 
       self.btn_bolme=QtWidgets.QPushButton(self)
       self.btn_bolme.setText("bölme")
       self.btn_bolme.move(150,250)
       self.btn_bolme.clicked.connect(self.hesaplama)
      
       self.lbl_sonuc=QtWidgets.QLineEdit(self)
       self.lbl_sonuc.setText("sonuç: ")
       self.lbl_sonuc.move(150,290)


    def hesaplama(self):
       sender=self.sender().text()#hangi butona tıklandğını anlamak içindir
       result=0
       if sender=="topla":
         result=int(self.txt_sayi1.text())+int(self.txt_sayi2.text() ) 
       elif sender=="çıkar":
         result=int(self.txt_sayi1.text())-int(self.txt_sayi2.text() )
       elif sender=="çarpma":
         result=int(self.txt_sayi1.text())*int(self.txt_sayi2.text() )
       elif sender=="bölme":
         result=int(self.txt_sayi1.text())/int(self.txt_sayi2.text() )


       self.lbl_sonuc.setText("sonuç: "+str(result))
    
   
       

def app():#sonucu verir
  app=QApplication(sys.argv)
  win=MainForm()
  win.show()
  sys.exit(app.exec_())#Pencere çalıştığında çarpı tuşuna basılana kadar programın çalışmasını sağlar.
app()

