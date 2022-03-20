import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from os import listdir, path, stat, startfile
from mimetypes import MimeTypes

class Dialogo(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  uic.loadUi("directorio.ui", self)
  self.btnBuscar.clicked.connect(self.getDir)
  self.treeArchivos.itemDoubleClicked.connect(self.openElement)
  
 def getDir(self):
  #Eliminar todas las filas de la búsqueda anterior
  self.treeArchivos.clear()
  #Ruta indicada por el usuario
  dir = self.lineDirectorio.text()
  #Si es un directorio
  if path.isdir(dir):
   #Recorrer sus elementos
   for element in listdir(dir):
    name = element
    pathinfo = dir + "\\" + name
    informacion = stat(pathinfo)
    #Si es un directorio
    if path.isdir(pathinfo):
     type = "Carpeta de archivos"
     size = ""
    else:
     mime = MimeTypes()
     type = mime.guess_type(pathinfo)[0]
     size = str(informacion.st_size) + " bytes"
    #Fecha de modificación
    date = str(time.ctime(informacion.st_mtime))
    #Crear un array para crear la fila con los items
    row = [name, date, type, size]
    #Insertar la fila
    self.treeArchivos.insertTopLevelItems(0, [QTreeWidgetItem(self.treeArchivos, row)])

 def openElement(self):
  #Obtener el item seleccionado por el usuario
  item = self.treeArchivos.currentItem()
  #Crear la ruta accediendo al nombre del elemento (carpeta o archivo)
  elemento = self.lineDirectorio.text() + "\\" + item.text(0)
  #Si es un directorio navegar a su interior
  if path.isdir(elemento):
   self.lineDirectorio.setText(elemento)
   self.getDir()
  else: #Si es un archivo abrirlo con el programa que lo abre por defecto en Windows
   startfile(elemento)
  
app = QApplication(sys.argv)
dialogo = Dialogo()
dialogo.show()
app.exec_()