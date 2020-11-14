import re, random, pygame



def reglaEstocastica(peso1, peso2, peso3):
    gramatica={

    'F1' : 'F[+F]F[-F]F',
    'F2' : 'F[+F]F',
    'F3' : 'F→F[-F]F'
    }

    opciones=['F1', 'F2', 'F3']

    selected=(random.choices(opciones, weights=(peso1, peso2, peso3), k=1)[0])
    
    return gramatica[selected]






listaChoices=[]
for x in range(1000):
    listaChoices.append(reglaEstocastica(33,34,33))

print("F[+F]F[-F]F: "+str(listaChoices.count('F[+F]F[-F]F')))
print("F[+F]F: "+str(listaChoices.count('F[+F]F')))
print("F→F[-F]F: "+str(listaChoices.count('F→F[-F]F')))