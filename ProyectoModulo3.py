import numpy as np
import matplotlib.pyplot as plt
from random import randint
import seaborn as sns 

Casilleros  = [1,2,3,4,5,6,7,8,9,10,11,12]
Casilleros_llenos = [0,0,0,0,0,0,0,0,0,0,0,0]
Canicas = 3000
saltos = 0
    
def Calculo_Galton():       
    for i in range(Canicas):
        saltos = -1
        for j in range(12):#len(Casilleros)
            saltos = saltos + randint(0, 1)
        Casilleros_llenos[saltos] = Casilleros_llenos[saltos] + 1
    return Casilleros_llenos

def Grafica_Galton():
    plt.title('Tablero de Galton - By JuanC')
    plt.xlabel('Casilleros')
    plt.ylabel('Numero de Canicas')
    #plt.bar(Casilleros, Calculo_Galton(),width=-1)
    sns.barplot(x=Casilleros,y=Calculo_Galton(),width=-1)
    plt.show()
    
print (Calculo_Galton())   
Grafica_Galton()
