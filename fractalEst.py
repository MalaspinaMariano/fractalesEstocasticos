import re, random, pygame, math



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


pila=[]
posicion=[400, 599]
angulo=math.pi
tamanioRef=4

class Segmento:
    def __init__(self, posicion , angulo):
        self.posicion = posicion
        self.angulo = angulo


def getLargoSegmento():
    random.seed()
    return random.uniform(0.7,3.3)*tamanioRef

def getDesplazamientoX(x , largo, angulo):
    return x+math.sin(angulo)*largo

def getDesplazamientoY(y , largo, angulo):
    return y+math.cos(angulo)*largo

def dibujarSegmento(pantalla):
    #print("estoy dibujando")
    #posicion[:]
    largo = getLargoSegmento()
    posicionFinal = [getDesplazamientoX(posicion[:][0] , largo, angulo),getDesplazamientoY( posicion[:][1] , largo, angulo)]
    pygame.draw.line(pantalla,(0,0,0), posicion[:], posicionFinal, 2)
    posicion[:]=posicionFinal
    pygame.display.flip()
    #pygame.time.delay(20)

def guardar(pantalla):
    #print("estoy apilando")
    global angulo
    segmento = Segmento(posicion[:],angulo)
    #print(segmento)
    pilaInterna = pila[:] 
    pilaInterna.append(segmento)
    #print(len(pilaInterna))
    pila[:]=pilaInterna
    #print(pila[:])
    """pila[:].append(posicion[:])
    pila[:].append(posicion[:])
    pila[:].append(angulo)
    print (posicion[:], angulo)
    print (pila[:])"""



def restaurar(pantalla):
    #print("estoy desapilando")
    global angulo
    pilaInterna=pila[:]
    segmento= pilaInterna.pop()
    angulo = segmento.angulo
    posicion[:] = segmento.posicion
    pila[:]=pilaInterna

def girarIzq(pantalla):
    #print("estoy girando izq")
    global angulo
    random.seed()
    angulo+=random.uniform(0.0,math.pi/6)
    if (angulo>2*math.pi):
        angulo= angulo - 2*math.pi

def girarDer(pantalla):
    #print("estoy girando der")
    global angulo
    random.seed()
    angulo-=random.uniform(0.0,math.pi/6)
    if (angulo<0):
        angulo= 2*math.pi + angulo




operacion={ 'F' : dibujarSegmento, '[' : guardar, ']': restaurar, '+':girarIzq, '-' :girarDer}

def dibujarCadena(cadena, pantalla):
    for char in cadena:
        #print(char)
        operacion[char](pantalla)
    print("termine de dibujar")
        










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
  
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
niveles = 6

cadena="[F][F][F]"
    
for n in range(niveles):        
    cadena=generarCadena(cadena, reglaEstocastica(33,34,33))
pantalla.fill(BLANCO)
dibujarCadena(cadena, pantalla)
    #pygame.time.delay(100)
pygame.display.flip()
    #print("-------------------------")
posicion=[400,599]
angulo = math.pi    
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO
      
    # # Avancemos y actualicemos la pantalla con lo que hemos dibujado.
 
    # Limitamos a 20 fotogramas por segundo
reloj.tick(20)
while not hecho:
    for evento in pygame.event.get():  # El usuario hizo algo
        if evento.type == pygame.QUIT: # Si el usuario hace click sobre cerrar
            hecho = True               # Marca que ya lo hemos hecho, de forma que abandonamos el bucle
      
# Pórtate bien con el IDLE. Si nos olvidamos de esta línea, el programa se 'colgará'
# en la salida.
pygame.quit()