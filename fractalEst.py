import re, random, pygame, math



def reglaEstocastica(peso1, peso2, peso3):
    gramatica={

    'F1' : 'F[+F]F[-F]F',
    'F2' : 'F[+F]F',
    'F3' : 'F[-F]F'
    }

    opciones=['F1', 'F2', 'F3']

    selected=(random.choices(opciones, weights=(peso1, peso2, peso3), k=1)[0])
    
    return gramatica[selected]

def generarCadena( cadenaInicial , regla):
    produccion = re.compile(r'F')
    return re.sub( produccion , regla , cadenaInicial)
"""
listaChoices=[]
for x in range(1000):
    listaChoices.append(reglaEstocastica(33,34,33))


print("F[+F]F[-F]F: "+str(listaChoices.count('F[+F]F[-F]F')))
print("F[+F]F: "+str(listaChoices.count('F[+F]F')))
print("F→F[-F]F: "+str(listaChoices.count('F→F[-F]F')))"""



"""cadena='F'
for i in range (14):
    cadena=generarCadena(cadena, reglaEstocastica(33,34,33))

print(cadena)"""


def dibujarSegmento():
    print("estoy dibujando")

def guardar():
    print("estoy apilando")

def restaurar():
    print("estoy desapilando")

def girarIzq():
    print("estoy girando izq")

def girarDer():
    print("estoy girando der")





operacion={ 'F' : dibujarSegmento, '[' : guardar, ']': restaurar, '+':girarIzq, '-' :girarDer}

def dibujarCadena(cadena, pantalla):
    for char in cadena:
        print(char)
        operacion[char]()






pila=[]
posicion=[900, 500]
angulo=90
tamañoRef=15







#--------------------------pantalla----------------------
    
BLANCO = (255, 255, 255)
pygame.init()
 
# Establecemos el alto y largo de la pantalla
dimensiones = [1000, 1000]
pantalla = pygame.display.set_mode(dimensiones)
  
pygame.display.set_caption("Fractales Estocasticos")
  
#Iteramos hasta que el usuario haga click sobre el botón de cerrar
hecho = False
  
# Usado para gestionar cuán rápido se actualiza la pantalla
reloj = pygame.time.Clock()
 
# -------- Bucle Principal del Programa  -----------
while not hecho:
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
             
             
    # Limpia la pantalla y establece su color de fondo
    pantalla.fill(BLANCO)
  
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    niveles = 3
    cadena="F"
    for n in range(niveles):
        pantalla.fill(BLANCO)
        dibujarCadena(cadena, pantalla)
        cadena=generarCadena(cadena, reglaEstocastica(33,34,33))
        pygame.time.delay(1000)
        pygame.display.flip()
        print("-------------------------")
        

    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
      
    # # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
 
    # Limitamos a 20 fotogramas por segundo
    reloj.tick(60)
      
# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit()