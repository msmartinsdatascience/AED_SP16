#!/usr/bin/env python
# coding: utf-8

# # UNB - PPCA
# ## Disciplina: Algoritmos e Estruturas de Dados (AED) - 2021.1 <br>

# ### Problema SP16 - Numerical 3-Dimensional Matching<br> 
# $Instance$: Disjoint sets $W$, $X$ and $Y$, each cotaining $m$ elements, a size $s(a) \in  Z^+$ for each element $ a \in W \cup X \cup Y$, and a bound $ B \in Z^+$.<br>
# $Question$: Can $W \cup X \cup Y$  be partitioned into $m$ disjoint sets $A_1, A_2, ..., A_m$ such that each $A_i$, contains exactly one element from each of $W$, $X$ and $Y$ and such that, for $1 \le i \le m$, $\sum_{a \in A_i}s(a)=B$?<br>
# $Reference:$ [Garey and Jonhson, ----]. Transformation from 3DM <br><br>
# Fonte: Computers and Intractability: A Guide to the Theory of NP-Completeness, página 224.
# 

# ### Abordagem III: geração dos conjuntos mutuamento exclusivos de soma constante via aleatoriedade

# In[1]:


import pandas as pd
import numpy as np
from random import sample
import time
from collections import Counter


# ##### 1. Define funções de Inserção de Dados e outras funções auxiliares

# In[12]:


# Define a função do size
def peso(x):
    return x
    
def DefineConjunto():
    # Especifica conjunto de entrada
    x=int(input("Informe gerador de A:     1 - Aleatório, 2 - Entre com seu conjunto: "))
    if x==2:
        listainput=input("Informe um conjunto de números separado por espaço: ").split()
        listainput=[int(string) for string in listainput]
        m=len(listainput) // 3
        A=listainput[:m*3]
        lenA=len(A)

    else:
        # número de elementos de cada um dos conjuntos W, X e Y.
        m=int(input("Informe o valor m, número de elementos de cada um dos conjuntos W, X e Y: "))
        lenA=3*m # define comprimento do conjunto A
        aleatorio=np.unique(np.random.randint(1, lenA*200, lenA*100))
        A= aleatorio.tolist()[:lenA]

    W, X, Y = A[:m], A[m:2*m], A[2*m:3*m] # avalia comprimento de W, X e Y:
    print("Conjunto A: ",A[:20],"...")
    if sum(A) % m ==0:
        print (m, "é divisor de",sum(A), "soma dos elementos de A")
    else: 
        print (m, "NÃO é divisor de",sum(A), "da soma dos elementos de A")
    print("Subconjuntos: \n W=",W[:10],"... \n X=", X[:10],"... \n Y=", Y[:10],"... ")

    return W, X, Y, m

def DefineConjuntoAleatorio(m=3):
    lenA=3*m
    aleatorio=np.unique(np.random.randint(1, lenA*200, lenA*100))
    A= aleatorio.tolist()[:lenA]
    W, X, Y = A[:m], A[m:2*m], A[2*m:3*m] # avalia comprimento de W, X e Y:
    print("Conjunto A: ",A[:20])
    if sum(A) % m ==0:
        print (m, "é divisor de",sum(A), "soma dos elementos de A")
    else: 
        print (m, "NÃO é divisor de",sum(A), "da soma dos elementos de A")
    return W, X, Y, m


# ##### 2. Define função de busca de conjuntos mutuamente exclusivos, tipo 3-tupla, de mesma soma, para um dado conjunto particionado 

# In[18]:


def geradorSP16_v2(W, X, Y):
    A=set(W)|set(X)|set(Y)
    k=100*len(W)**3

    s=[]
    m=len(W)
    if sum(A) % m != 0:
        return print("Conjunto não pode ser particionado nas condições do problema SP16")
    else:
        B=int(sum(A)/m)
        remanescenteA=[len(A)]
        for i in range(k):
            if len(set(W)|set(X)|set(Y))==0:
                break
            else:
                #print(i)
                w=int(pd.Series(W).sample(n=1,replace=True))
                x=int(pd.Series(X).sample(n=1,replace=True))
                y=int(pd.Series(Y).sample(n=1,replace=True))
                evento=[w,x,y]
                if sum(evento)==B :
                    #print(evento)
                    s.append(evento)
                    W.remove(w)
                    X.remove(x)
                    Y.remove(y)
                    remanescenteA.append(len(set(W)|set(X)|set(Y)))

        if A==set(np.unique(s)):
            print("O conjunto pode ser particionado em ",m, "subconjuntos de soma ",B, ".")
        else:
            #print("A:", A)
            print("Não foram encontrados subconjuntos de A que atendam aos critérios do problema, para o número de iterações aplicado.")
            print("Quantidade de elementos remanescentes em A:",remanescenteA)
            print("Número de elementos cobertos pela extração:", len(np.unique(s)))

    print(s)


# ##### 3. Execução caso a caso

# In[28]:


# Chama funções
print("="*80)
cW, cX, cY, m = DefineConjunto()
t0 = time.time()
geradorSP16_v2(cW, cX, cY)
tempo=round(time.time() - t0,4)
print("Tempo estimado de execução:", round(time.time() - t0,6), "segundos")


# ##### 4. Executar série de casos aleatórios

# In[51]:


hst_tempo=[]
for i in range(15):
    print("="*80)
    cW, cX, cY, m = DefineConjuntoAleatorio(m=3)
    t0 = time.time()
    geradorSP16_v2(cW, cX, cY)
    tempo=round(time.time() - t0,4)
    hst_tempo.append(tempo)
    print("Tempo estimado de execução:", tempo, "segundos")
print(hst_tempo)


# In[ ]:




