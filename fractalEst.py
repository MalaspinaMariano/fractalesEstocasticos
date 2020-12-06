#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, random, math, sys
from math import log


try:
    import pygame
except:
    print("EL MODULO PYGAME NO ESTA INSTALADO, NO GARANTIZAMOS EL BUEN FUNCIONAMIENTO DEL SCRIPT")


from sys import argv



def reglaEstocastica(peso1, peso2, peso3):
    gramatica={

   

    'F1' : 'F[+F]F[-F]F',
    'F2' : 'F[+F]F',
    'F3' : 'F[-F]F'
    }

    opciones=['F1', 'F2', 'F3']
    random.seed()
    selected=(random.choices(opciones, weights=(peso1, peso2, peso3), k=1)[0])
    
    return gramatica[selected]

def generarCadena(cadenaInicial, prob1, prob2, prob3):
    produccion = re.compile(r'F')
    return re.sub( produccion , reglaEstocastica(prob1, prob2, prob3) , cadenaInicial)




pila=[]
posicion=[400, 599]
angulo=math.pi

def tamanioRef(niv):
    return 1

class Segmento:
    def __init__(self, posicion , angulo):
        self.posicion = posicion
        self.angulo = angulo


def getLargoSegmento():
    
    return random.uniform(0.7,3.3)*tamanioRef(niveles)

def getDesplazamientoX(x , largo, angulo):
    return x+math.sin(angulo)*largo

def getDesplazamientoY(y , largo, angulo):
    return y+math.cos(angulo)*largo

def dibujarSegmento(pantalla):

    largo = getLargoSegmento()
    posicionFinal = [getDesplazamientoX(posicion[:][0] , largo, angulo),getDesplazamientoY( posicion[:][1] , largo, angulo)]
    pygame.draw.line(pantalla,(0,0,0), posicion[:], posicionFinal, 2)
    
    posicion[:]=posicionFinal
    pygame.display.flip()
    
    
    

def guardar(pantalla):
    
    global angulo
    segmento = Segmento(posicion[:],angulo)
    
    pilaInterna = pila[:] 
    pilaInterna.append(segmento)
    
    pila[:]=pilaInterna
  
    



def restaurar(pantalla):
    
    global angulo
    pilaInterna=pila[:]
    segmento= pilaInterna.pop()
    angulo = segmento.angulo
    posicion[:] = segmento.posicion
    pila[:]=pilaInterna

def girarIzq(pantalla):
    
    global angulo
    
    angulo+=random.uniform(0.0,math.pi/6)
    if (angulo>2*math.pi):
        angulo= angulo - 2*math.pi

def girarDer(pantalla):
    
    global angulo
    
    angulo-=random.uniform(0.0,math.pi/6)
    if (angulo<0):
        angulo= 2*math.pi + angulo




operacion={ 'F' : dibujarSegmento, '[' : guardar, ']': restaurar, '+':girarIzq, '-' :girarDer}

def dibujarCadena(cadena, pantalla):
    for char in cadena:
        
        operacion[char](pantalla)
    print("termine de dibujar")
        


niveles = 5
prob1=25
prob2=25
prob3=50

llamadaIncorrecta=True




    
if (len(argv)==3):
    if(argv[1]=="-n"):
        try:
            niveles= int(argv[2])
        except ValueError:
            print("Los valores ingresados como parametros deben ser numeros")
        llamadaIncorrecta=False

if (len(argv)==7):
    if((argv[1]=="-n") and (argv[3]=="-p") ):
        try:
            niveles= int(argv[2])
            prob1=int(argv[4])
            prob2=int(argv[5])
            prob3=int(argv[6])
        
            if((prob1+prob2+prob3)==100):
                llamadaIncorrecta=False    
        except ValueError:
            print("Los valores ingresados como parametros deben ser numeros")

if(llamadaIncorrecta):
    sys.exit("llamada incorrecta, por favor ingrese -n para la cantidad de niveles, y tambien se pueden personalizar agregando las probabilidades -p prob1, prob1, y prob2")



#--------------------------pantalla----------------------
    
BLANCO = (255, 255, 255)
pygame.init()
 
# Establecemos el alto y largo de la pantalla
dimensiones = [800, 600] #old school
pantalla = pygame.display.set_mode(dimensiones)
  
pygame.display.set_caption("Fractales Estocasticos")
  
#Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False
  
# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# -------- Bucle Principal del Programa  -----------
             
             
    # Limpia la pantalla y establece su color de fondo
pantalla.fill(BLANCO)
  





cadena="F"
    
for n in range(niveles):        
    cadena=generarCadena(cadena, prob1, prob2, prob3)
pantalla.fill(BLANCO)
dibujarCadena(cadena, pantalla)
  
pygame.display.flip()

posicion=[400,599]
angulo = math.pi    
  
      

reloj.tick(20)
while not hecho:
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True              
      

pygame.quit()