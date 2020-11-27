import re, random, pygame, math, sys
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

def generarCadena( cadenaInicial , regla):
    produccion = re.compile(r'F')
    return re.sub( produccion , regla , cadenaInicial)



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
    random.seed()
    angulo+=random.uniform(0.0,math.pi/6)
    if (angulo>2*math.pi):
        angulo= angulo - 2*math.pi

def girarDer(pantalla):
    
    global angulo
    random.seed()
    angulo-=random.uniform(0.0,math.pi/6)
    if (angulo<0):
        angulo= 2*math.pi + angulo




operacion={ 'F' : dibujarSegmento, '[' : guardar, ']': restaurar, '+':girarIzq, '-' :girarDer}

def dibujarCadena(cadena, pantalla):
    for char in cadena:
        
        operacion[char](pantalla)
    print("termine de dibujar")
        







niveles = 6
prob1=33
prob2=34
prob3=33

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
  
    # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO




cadena="F"
    
for n in range(niveles):        
    cadena=generarCadena(cadena, reglaEstocastica(prob1,prob2,prob3))
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
      

pygame.quit()