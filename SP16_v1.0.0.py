# PPCA - UNB
# Mestrado em Computação Aplicada
# Disciplina: Algoritmo e Estruturas de Dados (AED)
# Programa para tratamento do problema SP16

import numpy as np
import pandas as pd
from random import sample
import time
import os
from itertools import combinations  # obter combinações de um dado conjunto
from itertools import permutations
from itertools import combinations_with_replacement

def gera_combinacoes():
    print("======================================================================")
    print("         2. Gera combinações")
    print("======================================================================\n")
    comb = list(combinations(S, 3)) # gera combinações de 3 elementos para S
    print("Tempo até gerar combinações", lenA," 3 a 3:", round(time.time() - t0,6), "segundos.")
    comb2=[]
    comb2soma=[]
    for item in list(comb):
        if (item[0] in W and item[1] in X and item[2] in Y) and (set(item) not in comb2):
             comb2.append(set(item))
             comb2soma.append(sum(item))
    print("Espaço Amostral - Cardinalidade: ",len(comb2))
    print("Espaço Amostral - Elementos: ",comb2[:5],"...")
    print("Espaço Amostral - Soma: ",comb2soma[:5],"...", "\n")
    df = pd.DataFrame(comb2soma, columns= ['total'])

    # Avalia Existência de Soma B
    dicionario=df['total'].value_counts().to_dict()
    SolucaoB=[]
    for chave, valor in dicionario.items():
      if valor==m:
        SolucaoB.append(chave)
    if SolucaoB != []:
        print("Conjunto solução para B:",SolucaoB)
    else:
        print("O conjunto de entrada não pode ser particionado em",m, "subconjuntos de mesma soma.")
    return comb, SolucaoB

def obtem_particoes(listaB):
  if listaB==[]:
    return print("Não foram encontrados valores para B")
  else:
    for B in listaB:
      print("======================================================================")
      print("         3. Obtendo Partições com soma", B)
      print("======================================================================")
      print("Número de combinações de",lenA, "tomados 3 a 3:", len(comb))

      # Imprime combinações em que a soma é igual a B
      comb2=[]
      comb3=[]
      comb2soma=[]
      S2=set()
      for item2 in list(comb):
          if (item2[0] in W and item2[1] in X and item2[2] in Y) and (set(item2) not in comb2):
 
              comb2.append(set(item2))
              comb2soma.append(sum(item2))
              if sum(item2)==B:
                comb3.append(set(item2))
                S2.update(set(item2))
      if set(W)|set(X)|set(Y)==S2:
        print("Espaço Amostral - Cardinalidade: ",len(comb2))
        print("Conjunto Alvo - Cardinalidade: ",len(comb3))
        print("Conjunto Alvo - Elementos de soma", B,": ",comb3)
      else:
        print("O conjunto não pode ser particionado em", m, "subconjuntos de soma", B, ".")

# Execução do programa
x=int(input("Informe gerador de S: 1 -Sequência, 2 - Aleatório, 3 - Entre com seu conjunto: "))
if x==3:
  listainput=input("Informe um conjunto de números separado por espaço: ").split()
  listainput=[int(string) for string in listainput]
  m=len(listainput) // 3
  S=listainput[:m*3]
  lenA=len(S)

else:
  # número de elementos de cada um dos conjuntos W, X e Y.
  m=int(input("Informe o valor m, número de elementos de cada um dos conjuntos W, X e Y: "))
  lenA=3*m # define comprimento do conjunto A
  if x==1:
    S=list(range(1,lenA+1))
  else: # aleatório
    aleatorio=np.unique(np.random.randint(1, lenA*200, lenA*100))
    S= aleatorio.tolist()[:lenA]
W, X, Y = S[:m], S[m:2*m], S[2*m:3*m] # avalia comprimento de W, X e Y:
print("Conjunto A: ",S[:20])
print("Subconjuntos: \n W=",W[:10],"... \n X=", X[:10],"... \n Y=", Y[:10],"... ")

t0 = time.time()
comb, SolucaoB=gera_combinacoes()
obtem_particoes(SolucaoB)
print("Tempo estimado de execução:", round(time.time() - t0,6), "segundos")