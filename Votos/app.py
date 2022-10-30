from __future__ import print_function
import os
from pickle import TRUE
from rich import print

#constantes 
VOTOS_BOSONARO = 0
VOTOS_LULA = 0


#RODA VARIAS VEZES 

while TRUE:
    #aprensete os candidatos 
    print('*'*20)
    print(f'[on yellow]TOTAL BOLSONARO:[/]{VOTOS_BOSONARO}{os.linesep}[on red]TOTAL LULA:[/]{VOTOS_LULA}')
    print('*'*20)

    #permita votar 
    try:    
            voto= int(input(f'Para quem gostaria de votar?{os.linesep}22-Bolsonaro{os.linesep}13-Lula{os.linesep}Seu voto: '))
            if voto == 22:
                VOTOS_BOSONARO +=1
            elif voto == 13:
                VOTOS_LULA +=1
            else:
                pass    
    except:
        print('Digite apenas 22 ou 13')

    os.system('clear')