import numpy as np
from geneticalgorithm import geneticalgorithm as ga


def restriction(A, x):
    n=len(A)
    h=0
    v=0
    a=[]
    for i in range(0,n):
        sh=0
        sv=0

        d=0
        for j in range(0,n):
            sh=sh+A[i][j]
            sv=sv+A[j][i]
            if A[i][j]==1:
                d=j
        if (sh!=1):
            h=h+1

        if (sv!=1):
            v=v+1
        a.append(d)

    e=0
    if (h+v==0):
        t=0
        ef=np.zeros(n)
        for i in range(0,n):
            t=a[t]
            ef[t]=1

        if np.product(ef)==0:
            e=1

    return h+v+e


N
def f(x):
    B=[1000,8,16,24,15,20,8,1000,10,13,15,14,16,10,1000,20,18,15,24,13,20,1000,8,9,15,15,18,8,1000,16,20,14,15,9,16,1000]
    n=len(x)
    h=0
    for i in range(0,n):
        h=h+B[i]*x[i]

    L=int(np.sqrt(n))
    t=0
    A=[]
    for i in range(0,L):
        B=[]
        for j in range(0, L):
            B.append(x[t])
            t=t+1
        A.append(B)
    pen=100*restriction(A, 2)
    return h + pen

varbound=np.array([[0,1]]*N*N)

algorithm_param = {'max_num_iteration': 3000,\
                   'population_size':150,\
                   'mutation_probability':0.1,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.9,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

model=ga(function=f,\
            dimension=N*N,\
            variable_type='int',\
            variable_boundaries=varbound,\
            algorithm_parameters=algorithm_param)

model.run()
