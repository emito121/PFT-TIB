# 19/03/2021
#Autor: Emiliano Álvarez Ruiz
#Créditos a https://www.youtube.com/c/ManuelJDávilaGonz

import sys, time
from PyQt5.QtWidgets import QApplication, QDialog, QTreeWidgetItem
from PyQt5 import uic
from ensayos import *
import os
from os import listdir, path, startfile, stat
from mimetypes import MimeTypes
import io
from datetime import date

class Resultados(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("resultados.ui", self)
        self.btnRehacer.clicked.connect(self.Close)
        self.btnMainMenu.clicked.connect(self.MenuPrincipal)
    
    def Close(self):
        self.close()
        Analisis().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class Contacto(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("contacto.ui", self)
        self.btnRegresar.clicked.connect(self.InfoApp)
        self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
    
    def InfoApp(self):
        self.close()
        Informacion().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class codigosCalc(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("codigosCalc.ui", self)
        self.btnRegresar.clicked.connect(self.Regresar)
        self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
    
    def Regresar(self):
        self.close()
        Codigos().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class codigosInterfaz(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("codigosInterfaz.ui", self)
        self.btnRegresar.clicked.connect(self.Regresar)
        self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
    
    def Regresar(self):
        self.close()
        Codigos().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class Versiones(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("versiones.ui", self)
        self.btnRegresar.clicked.connect(self.InfoApp)
        self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
    
    def InfoApp(self):
        self.close()
        Informacion().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class Codigos(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("codigos.ui", self)
        self.btnCodigosCalc.clicked.connect(self.CodigosCalc)
        self.btnCodigosInterfaz.clicked.connect(self.CodigosInterfaz)
        self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
        self.btnRegresar.clicked.connect(self.Regresar)
        
    def Regresar(self):
        self.close()
        Informacion().exec_()

    def CodigosCalc(self):
        self.close()
        codigosCalc().exec_()

    def CodigosInterfaz(self):
        self.close()
        codigosInterfaz().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class InformacionApp(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("infoApp.ui", self)
        self.btnRegresar.clicked.connect(self.InfoApp)
        self.btnMenuPrincipal.clicked.connect(self.MenuPrincipal)
    
    def InfoApp(self):
        self.close()
        Informacion().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

class Informacion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("informacion.ui", self)
        self.btnInfoApp.clicked.connect(self.InfoApp)
        self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
        self.btnContacto.clicked.connect(self.Contacto)
        self.btnVersiones.clicked.connect(self.ventanaVersiones)
        self.btnCodigos.clicked.connect(self.codigos)
    
    def codigos(self):
        self.close()
        Codigos().exec_()

    def InfoApp(self):
        self.close()
        InformacionApp().exec_()
    
    def MenuPrincipal(self):
        self.close()
        Ventana().exec_()

    def Contacto(self):
        self.close()
        Contacto().exec_()
    
    def ventanaVersiones(self):
        self.close()
        Versiones().exec_()
        
class Analisis(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("analisis.ui", self)
        self.ventanaResultados = Resultados()
        self.ventanaExplorador = Explorador()
        self.btnIniciarTratamiento.clicked.connect(self.abrirResultados)
        self.boxEnsayo.currentTextChanged.connect(self.desactivarEnergia)
        self.btnMenuPrincipal.clicked.connect(self.abrirMenuPrincipal)
        self.editArchivo.textChanged.connect(self.elegirColumna)
        self.btnExplorador.clicked.connect(self.abrirExplorador)
        self.ventanaExplorador.treeArchivos.itemDoubleClicked.connect(self.seleccionarArchivo)
        try:
            directorioo = os.getcwd()
            archivo = io.open(f'{directorioo}/cache.txt', 'r')
            texto = archivo.read()
            self.editArchivo.setText(texto)
        except:
            pass
    
    def abrirExplorador(self):
        #self.setEnabled(False)
        self.ventanaExplorador.exec_()
    
    def seleccionarArchivo(self):
        self.editArchivo.setText(self.ventanaExplorador.openElement())
        #self.setEnabled(True)
        self.ventanaExplorador.close()

    def elegirColumna(self):
        # self.boxColumnas.setEnabled(True)
        # path = str(self.editArchivo.text())
        # datos = os.path.join(path)
        # directorioo = os.getcwd()
        
        # tabla = pd.read_csv(datos)
        # for i in tabla.columns:
        #     self.boxColumnas.addItem(i)
        # self.editArchivo.setStyleSheet("border: 1px solid green;")
        # archivo = io.open(f'{directorioo}/cache.txt', 'w')
        # archivo.write(datos)
        # archivo.close()
        try:
            self.boxColumnas.setEnabled(True)
            path = str(self.editArchivo.text())
            datos = os.path.join(path)
            directorioo = os.getcwd()
            tabla = pd.read_csv(datos)
            for i in tabla.columns:
                self.boxColumnas.addItem(i)
            self.editArchivo.setStyleSheet("border: 1px solid green;")
            archivo = io.open(f'{directorioo}/cache.txt', 'w')
            archivo.write(datos)
            archivo.close()
        except:
            self.boxColumnas.setEnabled(False)
            self.editArchivo.setStyleSheet("border: 1px solid red;")
        
        return datos

    def abrirMenuPrincipal(self):
        self.close()
        Ventana().exec_()

    def abrirResultados(self):
        if self.boxDEA.currentText() == 'Si':
            DEA = True
        else:
            DEA = False

        if self.boxFrecuente.currentText() == 'Si':
            Frecuente = True
        else:
            Frecuente = False

        ensayoSelected = str(self.boxEnsayo.currentText())   
        tStudent = float(self.editStudent.text())    
        columna = str(self.boxColumnas.currentText())
        expansion = int(self.spinExpansion.value())
        datos = self.elegirColumna()

        if ensayoSelected == 'Energía':
            try:
                energia = int(self.editEnergia.text())
                ensayo = Energia(datos, columna, expansion, energia, tStudent)
                self.ventanaResultados.labelResultado.setText(ensayo.Resultado())
                self.ventanaResultados.labelJuicio.setText(ensayo.verificacion())
                self.ventanaResultados.labelMedia.setText(f"La media de las muestras es {ensayo.media: .2f} {ensayo.unidad}")
                self.ventanaResultados.labelDesviacion.setText(f"La desviación estándar de las muestras es {ensayo.stDev: .2f} {ensayo.unidad}")
                contador = 0
                while True:
                    if f'E{contador}_{date.today()}.txt' in listdir(f'{path.abspath(os.getcwd())}\ensayos'):
                        contador += 1
                    else:    
                        archivo = io.open(f'ensayos\E{contador}_{date.today()}.txt', 'w')
                        archivo.write(f'{ensayo.Resultado()} \n{ensayo.verificacion()} \nLa media de las muestras es {ensayo.media: .2f} {ensayo.unidad} \nLa desviación estándar de las muestras es {ensayo.stDev: .2f} {ensayo.unidad}')
                        archivo.close()
                        break
                self.close()
                self.ventanaResultados.exec_()
            except:
                self.labelAdvertencia.setText('Algún valor ingresado es incorrecto')  
            #     #C:\Users\enfil\Documents\UTEC\Semestre 6\PFT\Datos ensayo prueba.txt

        if ensayoSelected == 'Tiempo de sincronización':
            try:
                ensayo = Sincronizacion(datos, columna, expansion, tStudent)
                self.ventanaResultados.labelResultado.setText(ensayo.Resultado())
                self.ventanaResultados.labelJuicio.setText(ensayo.Limite())
                self.ventanaResultados.labelMedia.setText(f"La media de las muestras es {ensayo.media: .2f} {ensayo.unidad}")
                self.ventanaResultados.labelDesviacion.setText(f"La desviación estándar de las muestras es {ensayo.stDev: .2f} {ensayo.unidad}")
                contador = 0
                while True:
                    if f'S{contador}_{date.today()}.txt' in listdir(f'{path.abspath(os.getcwd())}\ensayos'):
                        contador += 1
                    else:    
                        archivo = io.open(f'ensayos\S{contador}_{date.today()}.txt', 'w')
                        archivo.write(f'{ensayo.Resultado()} \n{ensayo.Limite()} \nLa media de las muestras es {ensayo.media: .2f} {ensayo.unidad} \nLa desviación estándar de las muestras es {ensayo.stDev: .2f} {ensayo.unidad}')
                        archivo.close()
                        break
                self.close()
                self.ventanaResultados.exec_()
            except:
                self.labelAdvertencia.setText('Algún valor ingresado es incorrecto')

        if ensayoSelected == 'Tiempo de carga':
            try:
                ensayo = tiempoCarga(datos, columna, expansion, DEA, Frecuente, tStudent)
                self.ventanaResultados.labelResultado.setText(ensayo.Resultado())
                self.ventanaResultados.labelJuicio.setText(ensayo.verificacion())
                self.ventanaResultados.labelMedia.setText(f"La media de las muestras es {ensayo.media: .2f} {ensayo.unidad}")
                self.ventanaResultados.labelDesviacion.setText(f"La desviación estándar de las muestras es {ensayo.stDev: .2f} {ensayo.unidad}")
                contador = 0
                while True:
                    if f'C{contador}_{date.today()}.txt' in listdir(f'{path.abspath(os.getcwd())}\ensayos'):
                        contador += 1
                    else:    
                        archivo = io.open(f'ensayos\C{contador}_{date.today()}.txt', 'w')
                        archivo.write(f'{ensayo.Resultado()} \n{ensayo.verificacion()} \nLa media de las muestras es {ensayo.media: .2f} {ensayo.unidad} \nLa desviación estándar de las muestras es {ensayo.stDev: .2f} {ensayo.unidad}')
                        archivo.close()
                        break
                self.close()
                self.ventanaResultados.exec_()
            except:
                self.labelAdvertencia.setText('Algún valor ingresado es incorrecto')
    
    def desactivarEnergia(self):
        ensayoSel = str(self.boxEnsayo.currentText())

        if ensayoSel != 'Energía':
            self.editEnergia.setEnabled(False)

        else:
            self.editEnergia.setEnabled(True)

class Explorador(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  uic.loadUi("directorio.ui", self)
  self.btnBuscar.clicked.connect(self.getDir)
  self.treeArchivos.itemClicked.connect(self.openElement)
  
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
  else: #Si es un archivo retornar su ruta
   return elemento

class EnsayosAnteriores(QDialog):
 def __init__(self):
  QDialog.__init__(self)
  uic.loadUi("ensayosAnteriores.ui", self)
  self.btnMenuPpl.clicked.connect(self.MenuPrincipal)
  self.getDir()
  self.treeArchivos.itemDoubleClicked.connect(self.openElement)

 def MenuPrincipal(self):
  self.close()
  Ventana().exec_()

 def getDir(self):
  #Eliminar todas las filas de la búsqueda anterior
  self.treeArchivos.clear()
  #Ruta indicada por el usuario
  dir = f'{path.abspath(os.getcwd())}\ensayos'
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
  elemento = f'{path.abspath(os.getcwd())}\ensayos' + "\\" + item.text(0)
  texto = open(elemento, 'r').read()
  self.textAnteriores.setText(texto)
  #startfile(elemento)

class Ventana(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("mainWindow.ui", self)
        self.ventanaAnalisis = Analisis()
        self.ventanaInformacion = Informacion()
        self.btnInitEnsayo.clicked.connect(self.abrirAnalisis)
        self.btnCerrar.clicked.connect(self.Cerrar)
        self.btnInfo.clicked.connect(self.abrirInfo)
        self.btnPrevEnsayos.clicked.connect(self.EnsayosPrevios)

    def abrirAnalisis(self):
        self.close()
        self.ventanaAnalisis.exec_()

    def Cerrar(self):
        self.close()
    
    def abrirInfo(self):
        self.close()
        self.ventanaInformacion.exec_()
    
    def EnsayosPrevios(self):
        self.close()
        EnsayosAnteriores().exec_()

app = QApplication(sys.argv)
_ventana = Ventana()
_ventana.show()
app.exec_()