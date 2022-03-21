# 19/03/2021
#Autor: Emiliano Álvarez Ruiz

import pandas as pd
import numpy as np
from math import sqrt
from statistics import stdev
from statistics import mean

class Ensayo():

  def __init__(self, ubicacion, columna, exactitud, exactitud2, resolucion, unidad, limite, expansion, tStudent):
    try:
      self.Tabla = pd.read_csv(ubicacion,sep=',')
    except:
      self.Tabla = ubicacion
    self.Data = self.Tabla[columna]
    self.mediciones = len(self.Data)
    self.media = mean(self.Data)
    self.stDev = stdev(self.Data)
    self.expansion = expansion
    self.Urep = self.stDev/sqrt(self.mediciones)
    self.Ucal = 2*(((self.media*self.exactitud)+self.exactitud2)/sqrt(3))
    self.Ur = self.resolucion/sqrt(3)
    self.Ic = sqrt(self.Urep**2+self.Ucal**2+tStudent*self.Ur**2)
    self.Iexpandida = self.Ic*self.expansion 
  
  def Resultado(self):
    if self.expansion == 1: 
      return f"El valor obtenido de la medición es {self.media: .2f} ± {self.Iexpandida: .2f} {self.unidad}, con una confiabilidad del 68.2%"
    elif self.expansion == 2:
      return f"El valor obtenido de la medición es {self.media: .2f} ± {self.Iexpandida: .2f} {self.unidad}, con una confiabilidad del 95.4%"
    elif self.expansion == 3:
      return f"El valor obtenido de la medición es {self.media: .2f} ± {self.Iexpandida: .2f} {self.unidad}, con una confiabilidad del 99.2%"
    else:
      return f"La expansión solo está habilitada para los valores 1, 2 o 3"

  def Limite(self):
    if self.limite == 0: 
      pass
    else:
      if (self.media+self.Iexpandida) > self.limite:
        if (self.media-self.Iexpandida) > self.limite:
          return f"El valor real sobrepasa totalmente el limite de {self.limite} {self.unidad}."
        if (self.media-self.Iexpandida) < self.limite:
          return f"El valor real puede sobrepasar los {self.limite} {self.unidad}."
      if (self.media+self.Iexpandida) < self.limite:
        return f"El valor real no sobrepasa los {self.limite} {self.unidad}."

class Energia(Ensayo):

  def __init__(self, ubicacion, columna, expansion, energia, tStudent):
    self.unidad = 'J'
    self.limite = 3
    self.exactitud = 0.01
    self.resolucion = 0.1
    self.exactitud2 = 0.1
    self.energia = energia
    super().__init__(ubicacion, columna, self.exactitud, self.exactitud2, self.resolucion, self.unidad, self.limite, expansion, tStudent)

  def verificacion(self):
    for i in self.Data:
      if (self.energia*0.15 < 3):
        if ((i <= self.energia-3) or (i >= self.energia+3)):
          return "Los niveles de energía superan los permitidos de ± 3 J o 15 % la energía seteada"
        else:
          return "Los niveles de energía son acordes a la energía seteada"
      else:
        if ((i <= self.energia-self.energia*0.15) or (i >= self.energia+self.energia*0.15)):
          return "Los niveles de energía superan los permitidos de ± 3 J o 15 % la energía seteada"
        else:
          return "Los niveles de energía son acordes a la energía seteada"

class Sincronizacion(Ensayo):

  def __init__(self, ubicacion, columna, expansion, tStudent):
    self.unidad = 'ms'
    self.limite = 60    
    self.exactitud = 0
    self.resolucion = 0.001
    self.exactitud2 = 0.001
    super().__init__(ubicacion, columna, self.exactitud, self.exactitud2, self.resolucion, self.unidad, self.limite, expansion, tStudent)

class tiempoCarga(Ensayo):

  def __init__(self, ubicacion, columna, expansion, DEA, frecuente, tStudent):
    self.DEA = DEA
    self.frecuente = frecuente
    self.unidad = 's'
    self.limiteMNF = 20
    self.limiteMF = 15
    self.limiteDNF = 35
    self.limiteDF = 30
    self.exactitud = 0
    self.resolucion = 0.1
    self.exactitud2 = 0.05
    super().__init__(ubicacion, columna, self.exactitud, self.exactitud2, self.resolucion, self.unidad, self.limiteMF, expansion, tStudent)

  def verificacion(self):
    if self.frecuente:
      if self.DEA:
        if (self.media+self.Iexpandida) > self.limiteDF:
          if (self.media-self.Iexpandida) > self.limiteDF:
            return f"El valor real sobrepasa totalmente el limite de {self.limiteDF} {self.unidad} dado por la norma de tipo para DEA de uso frecuente."
          else:
            return f"El valor real puede sobrepasar los {self.limiteDF} {self.unidad} dado por la norma de tipo para DEA de uso frecuente."
        else:
          return f"El valor real no sobrepasa los {self.limiteDF} {self.unidad} dado por la norma de tipo para DEA de uso frecuente."

      else:
          if (self.media+self.Iexpandida) > self.limiteMF:
            if (self.media-self.Iexpandida) > self.limiteMF:
              return f"El valor real sobrepasa totalmente el limite de {self.limiteMF} {self.unidad} dado por la norma de tipo para desfibriladores manuales de uso frecuente."
            else:
              return f"El valor real puede sobrepasar los {self.limiteMF} {self.unidad} dado por la norma de tipo para desfibriladores manuales de uso frecuente."
          else:
            return f"El valor real no sobrepasa los {self.limiteMF} {self.unidad} dado por la norma de tipo para desfibriladores manuales de uso frecuente."
    
    else:
      if self.DEA:
        if (self.media+self.Iexpandida) > self.limiteDNF:
          if (self.media-self.Iexpandida) > self.limiteDNF:
            return f"El valor real sobrepasa totalmente el limite de {self.limiteDNF} {self.unidad} dado por la norma de tipo para DEA de uso no frecuente."
          else:
            return f"El valor real puede sobrepasar los {self.limiteDNF} {self.unidad} dado por la norma de tipo para DEA de uso no frecuente."
        else:
          return f"El valor real no sobrepasa los {self.limiteDNF} {self.unidad} dado por la norma de tipo para DEA de uso no frecuente."

      else:
          if (self.media+self.Iexpandida) > self.limiteMNF:
            if (self.media-self.Iexpandida) > self.limiteMNF:
              return f"El valor real sobrepasa totalmente el limite de {self.limiteMNF} {self.unidad} dado por la norma de tipo para desfibriladores manuales de uso no frecuente."
            else:
              return f"El valor real puede sobrepasar los {self.limiteMNF} {self.unidad} dado por la norma de tipo para desfibriladores manuales de uso frecuente."
          else:
            return f"El valor real no sobrepasa los {self.limiteMNF} {self.unidad} dado por la norma de tipo para desfibriladores manuales de uso no frecuente."