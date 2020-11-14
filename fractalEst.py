import re, random, pygame



def reglaEstocastica(peso1, peso2, peso3):
    gramatica={

    'F1' : 'F[+F]F[-F]F',
    'F2' : 'F[+F]F',
    'F3' : 'F→F[-F]F'
    }

    opciones=['F1', 'F2', 'F3']

    selected=(random.choices(opciones, weights=(peso1, peso2, peso3), k=1))
    
    return gramatica[selected[0]]






listaChoices=[]
for x in range(100):
    listaChoices.append(reglaEstocastica(33,33,33))

print("F[+F]F[-F]F: "+str(listaChoices.count('F[+F]F[-F]F')))
print("F[+F]F: "+str(listaChoices.count('F[+F]F')))
print("F→F[-F]F: "+str(listaChoices.count('F→F[-F]F')))