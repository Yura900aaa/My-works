#!/usr/bin/env python
# coding: utf-8

# In[417]:


# Элементы генетических алгоритмов
# За основу взяты алгоортмы из книги 

# Подключение использования библиотеки случайных функций и построения графиков

import random
import matplotlib.pyplot as plt
import networkx as nx

# Количество генов в хромосоме 
n=12

# Создание случайной хромосомы, состоящей из бинарных генов (0 или 1).
# Создание списка для хранения генов 


# В цикле от 0 до n-1 (особенность Python) создается случайное число (ген) 
#и прикрепляется к уже имеющемуся списку генов (хромосома)

def генерация_хромосомы_2(n):
    хромосома= []
    for i in range(0,n):
        ген = random.randint(0,1)
        хромосома.append(ген)
    return хромосома

хромосома=генерация_хромосомы_2(12)
#Для контроля получившаяся хромосома выводится на экран
print(хромосома)

# Отображение хромосомы в виде диаграммы

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()

# Определение функции для отрисовки маршрутов
def city(x):
    if len(x)==12:
        G = nx.DiGraph()
        for i in range(0, 4):
            for j in range(0, 3):
                if (x[3*i+j]==1):
                    if (j>=i):
                        G.add_edge(i, j+1)
                    else:
                        G.add_edge(i, j)
        nx.draw_circular(G,
         node_color='#aaaaff',
         node_size=1200,
         arrowsize=30,
         with_labels=True)
        
# Отображение хромосомы в виде маршрутов. Обратите внимание, что стрелки могут быть направлены в обе стороны
city(хромосома)


# In[418]:


def бинарная_приспособленность(x):
    return sum(x)
def вещественная_приспособленность(x):
    return sum(x)


# In[419]:


вещественная_приспособленность(хромосома)


# In[420]:


# Аналогичное создание хромосомы их списка возможных генов, с дополнительным условием на то, 
# чтобы два соседних гена не повторялись.

гены=['Москва','Лондон','Киото', 'Каир', 'Осло']
хромосома = []

ген=random.choice(гены)
хромосома.append(ген)
for i in range(1,n):
    гены_без_последнего=гены.copy()
    гены_без_последнего.remove(ген)
    ген = random.choice(гены_без_последнего)
    хромосома.append(ген)
print(хромосома)


# In[421]:


# Аналогичное создание хромосомы из вещественных чисел

n=10
хромосома = []
for i in range(0,n):
    s = random.random()
    хромосома.append(s)

# Отображение хромосомы в виде графика
fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,n),хромосома, 'b--') 
plt.xticks(range(0,n))
plt.show()


fig, ax = plt.subplots(figsize=(20, 1))
# Отображение хромосомы в виде диаграммы
plt.bar(range(0,n),хромосома)
plt.show()


# In[422]:


# Генерация хромосомы из бинарных генов для дальнейшего использования с дискретными алгоритмами мутации

n=12
хромосома= []
for i in range(0,n):
    ген = random.randint(0,1)
    хромосома.append(ген)
print(хромосома)


# In[423]:


# Пример кодирования целых чисел кодом Грея. 
# В отличие от классического представления в виде перехода их десятичной системы счисления в двоичную
# соседние целые числа в коде Грея отличаются только одним знаком.

# Использование библиотеки
from sympy.combinatorics.graycode import bin_to_gray

# Длина двоичной последовательности 
m=15
# Число x
x=8

print('x равен: '+ str(x))

print('Двоичное представление x: '+bin(x)[3:].zfill(m))
print('Двоичное представление соседа x: '+bin(x-1)[3:].zfill(m))
print('Представление x кодом Грея: '+ bin_to_gray(bin(x)[3:].zfill(m)))
print('Представление соседа x кодом Грея: '+bin_to_gray(bin(x-1)[3:].zfill(m)))


# In[424]:


# Мутация 1: равномерная мутация 
# Определение функции
def мутация_1(хромосома2, порог2):
    хромосома3=хромосома2.copy()
    L=len(хромосома2)
    if (random.random()>порог2):
        номер_гена=random.randint(0,L-1)
        #print('Мутировал ген номер '+str(номер_гена))
        хромосома3[номер_гена]=1-хромосома3[номер_гена]  
    #else:
        #print('Мутации не было')
    return хромосома3
#Применение мутации

хромосома=генерация_хромосомы_2(12)

print('Xромосома до: '+str(хромосома))
порог=0.5
хромосома2=мутация_1(хромосома, порог)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()
city(хромосома)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()
city(хромосома2)


# In[425]:


# Мутация 2: равномерная плотная мутация 
# Определение функции

def мутация_2(хромосома2, порог2):
    s=[]
    хромосома3=хромосома2.copy()
    L=len(хромосома3)
    for номер_гена in range(0,L):
        if (random.random()>порог2):
            s.append(номер_гена)
            хромосома3[номер_гена]=1-хромосома3[номер_гена]  
    #if (len(s)>0):
       # print('Мутировали гены с номерами '+ str(s))
    return хромосома3
#Применение мутации

хромосома=генерация_хромосомы_2(12)

print('Xромосома до: '+str(хромосома))
порог=0.5
хромосома2=мутация_2(хромосома, порог)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()
city(хромосома)
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()
city(хромосома2)


# In[426]:


# Мутация 3: оператор обменнной мутации
# Определение функции

def мутация_3(хромосома2):
    хромосома3=хромосома2.copy()
    L=len(хромосома3)
    
    номер_одного_гена=random.randint(0,L-1)
    номер_другого_гена=random.randint(0,L-1)
    
   # print ('Обмен генов с номерами: ' + str(номер_одного_гена) + ' и ' + str(номер_другого_гена) )
    s=хромосома[номер_другого_гена]

    хромосома3[номер_другого_гена]=хромосома3[номер_одного_гена]
    хромосома3[номер_одного_гена]=s
    return хромосома3 

хромосома=генерация_хромосомы_2(12)

print('Xромосома до: '+str(хромосома))
хромосома2=хромосома.copy()
for i in range(0,4):
    хромосома2=мутация_3(хромосома2)
    print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()
city(хромосома)
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()
city(хромосома2)


# In[ ]:





# In[427]:


# Мутация 4. оператор зеркальной мутации

def мутация_4(хромосома2):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    начало_фрагмента=random.randint(0,L-2)
    конец_фрагмента=random.randint(начало_фрагмента+1,L-1)
    фрагмент=хромосома3[начало_фрагмента:конец_фрагмента]
    #print ('Зеркально повернуты гены с номера '+ str(начало_фрагмента)+' до '+str(конец_фрагмента-1))
    фрагмент.reverse()
    хромосома3[начало_фрагмента:конец_фрагмента]=фрагмент
    return хромосома3
хромосома=генерация_хромосомы_2(12)

print('Xромосома до: '+str(хромосома))
хромосома2=мутация_4(хромосома)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()
city(хромосома)
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()
city(хромосома2)


# In[428]:


# Мутация_5  оператор транспозиции
def мутация_5(хромосома2):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    
    начало_первого_фрагмента=random.randint(0,L-2)
    начало_первого_фрагмента=3
    начало_второго_фрагмента=random.randint(начало_первого_фрагмента+1,L-1)
    начало_второго_фрагмента=6
    первый_фрагмент=хромосома3[начало_первого_фрагмента:начало_второго_фрагмента]
    конец_второго_фрагмента=random.randint(начало_второго_фрагмента,L)
    конец_второго_фрагмента=10
    второй_фрагмент=хромосома3[начало_второго_фрагмента:(конец_второго_фрагмента)]
    хвост=хромосома3[(конец_второго_фрагмента):L]
    второй_фрагмент.reverse()
    хромосома3=хромосома3[0:начало_первого_фрагмента]+второй_фрагмент+первый_фрагмент+хвост
    #print('Точки разреза: '+str(начало_первого_фрагмента)+' , ' +str(начало_второго_фрагмента) +' , '+ str(конец_второго_фрагмента-1))
    return хромосома3
хромосома=генерация_хромосомы_2(12)

print('Xромосома до: '+str(хромосома))
хромосома2=мутация_5(хромосома)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()
city(хромосома)
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()
city(хромосома2)


# In[429]:


# Мутация_6  случайной мутации
def мутация_6(хромосома2, x1, x2, k):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    s=random.sample(range(0,L),k)
    for i in s:
        хромосома3[i]=random.uniform(x1,x2)
    return хромосома3

print('Xромосома до: '+str(хромосома))
хромосома2=мутация_6(хромосома,0,1,2)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,len(хромосома)),хромосома, 'bo--')  # 
ax.plot(range(0,len(хромосома2)),хромосома2, 'bo-')

plt.show()  


# In[430]:


# Мутация_7  оператор гаусовой мутации
def мутация_7(хромосома2,d, k):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    s=random.sample(range(0,L),k)
    d=1
    for i in s:
        хромосома3[i]=random.gauss(m,d)
    return хромосома3

print('Xромосома до: '+str(хромосома))
хромосома2=мутация_7(хромосома,1,2)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,n),хромосома, 'bo--') 
ax.plot(range(0,n),хромосома2, 'bo-')
plt.xticks(range(0,len(хромосома)))
plt.show()  

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()


# In[431]:


# Мутация_8  #арифметический оператор вещественного сдвига
def мутация_8(хромосома2, b, k):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    хромосома1=хромосома.copy()
    s=random.sample(range(0,L),2)
    for i in s:
        хромосома3[i]=хромосома3[i]-b*(2*random.random()-1)
    return хромосома3 


print('Xромосома до: '+str(хромосома))
хромосома2=мутация_8(хромосома,4,2)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,n),хромосома, 'bo--') 
ax.plot(range(0,n),хромосома2, 'bo-')
plt.xticks(range(0,len(хромосома)))
plt.show()  

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()


# In[432]:


# Мутация_9  геометрический оператор вещественного сдвига
def мутация_9(хромосома2, b, k):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    s=random.sample(range(0,L),k)
    for i in s:
        хромосома3[i]=хромосома3[i]-хромосома3[i]*b*(2*random.random()-1)+1
    return хромосома3 


print('Xромосома до: '+str(хромосома))
хромосома2=мутация_9(хромосома,4,2)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,n),хромосома, 'bo--') 
ax.plot(range(0,n),хромосома2, 'bo-')
plt.xticks(range(0,len(хромосома)))
plt.show()  

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()


# In[433]:


# Мутация_10  BGA -оператор мутации
def мутация_10(хромосома2, b, x1, x2, k, m):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    
    s=random.sample(range(0,L),m)
    for i in s:
        if random.random()>0.5:
            хромосома3[i]=хромосома3[i]- b*(x2-x1)*2**(-k*random.random())
        else:
            хромосома3[i]=хромосома3[i]+ b*(x2-x1)*2**(-k*random.random())
    return хромосома3


print('Xромосома до: '+str(хромосома))
хромосома2=мутация_10(хромосома,4,-1, 1, 2, 4)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,n),хромосома, 'bo--') 
ax.plot(range(0,n),хромосома2, 'bo-')
plt.xticks(range(0,len(хромосома)))
plt.show()  

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()


# In[434]:


# Мутация_11  стеменной оператор мутации
def мутация_11(хромосома2, b, x1, x2, u, m):
    хромосома3= хромосома2.copy() 
    L=len(хромосома3)
    s=random.sample(range(0,L),m)
    for i in s:
        u=b*random.random()**(b-1)
        if (x2-хромосома3[i])!=0:
            if ((хромосома3[i]-x1)/(x2-хромосома3[i]))>u:
                хромосома3[i]=хромосома3[i]- u*(x2-хромосома3[i])
            else:
                хромосома3[i]=хромосома3[i]+ u*(хромосома3[i]-x1)
    return хромосома3


print('Xромосома до: '+str(хромосома))
хромосома2=мутация_11(хромосома,2,0, 2, 0.5, 4)
print('Xромосома после: '+str(хромосома2))

fig, ax = plt.subplots(figsize=(20, 5))
ax.plot(range(0,n),хромосома, 'bo--') 
ax.plot(range(0,n),хромосома2, 'bo-')
plt.xticks(range(0,len(хромосома)))
plt.show()  

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома)),хромосома)
plt.show()

fig, ax = plt.subplots(figsize=(20, 1))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()


# In[435]:


#Скрещивание 

def предок(n):
    хромосома= []
    for i in range(0,n):
        ген = random.randint(0,1)
        хромосома.append(ген)
    return хромосома

хромосома1=предок(12)
хромосома2=предок(12)
хромосома3=предок(12)
хромосома4=предок(12)

print(хромосома1)
print(хромосома2)
print(хромосома3)
print(хромосома4)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома4)),хромосома4)
plt.show()

city(хромосома4)


# In[436]:


#Кроссовер 1. одноточечный кроссовер
def кроссовер_1(хромосома1,хромосома2):
    i=random.randint(0,len(хромосома1))
    хромосома3=хромосома1[0:i]+хромосома2[i:n]
    return хромосома3


хромосома1=предок(12)
хромосома2=предок(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_1(хромосома1,хромосома2)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

print ("Потомок")
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()


# In[437]:


#Кроссовер 2. двухоточечный кроссовер


def кроссовер_2(хромосома1,хромосома2):
    i1=random.randint(0,n-1)
    i2=random.randint(i1,n)
    хромосома=хромосома1[0:i1]+хромосома2[i1:i2]+хромосома1[i2:n]
    return(хромосома)


хромосома1=предок(12)
хромосома2=предок(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_2(хромосома1,хромосома2)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

print ("Потомок")
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()


# In[438]:


#Кроссовер 3. #однородный кроссовер

def кроссовер_3(хромосома1,хромосома2):
    хромосома=хромосома2.copy()
    for i in range(0,n):
        if (random.random()>0.5):
            хромосома[i]=хромосома1[i]
    return(хромосома)

хромосома1=предок(12)
хромосома2=предок(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_3(хромосома1,хромосома2)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

print ("Потомок")
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()


# In[439]:


#Кроссовер 4. полуоднородный кроссовер
def кроссовер_4(хромосома1,хромосома2):
    хромосома=хромосома2.copy()
    s=random.sample(range(0,n),int(n/2))
    for i in s:
        хромосома[i]=хромосома1[i]
    return(хромосома)

хромосома1=предок(12)
хромосома2=предок(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_4(хромосома1,хромосома2)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

print ("Потомок")
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()


# In[440]:


#Кроссовер 5. Триадный
def кроссовер_5(хромосома1,хромосома2, хромосома3, d):
    s=random.sample(range(0,n),int(len(хромосома1)*d))
    маска=хромосома3.copy()
    for i in s:
        маска[i]=1-маска[i]
    хромосома=хромосома2.copy()
    for i in range(0,n):
        if (маска[i]==хромосома[1]):
            хромосома[i]=хромосома[1]
    return хромосома 

хромосома1=предок(12)
хромосома2=предок(12)
хромосома3=предок(12)

print(хромосома1)
print(хромосома2)
print(хромосома3)

хромосома4=кроссовер_5(хромосома1,хромосома2, хромосома3, 0.1)

print ("Потомок")
print(хромосома4)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()

print ("Потомок")
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома4)),хромосома4)
plt.show()


# In[441]:


#Кроссовер 6. оператор сегрегации  (для четырех)

def кроссовер_6(хромосома1,хромосома2, хромосома3, хромосома4):
    n=len(хромосома1)
    начало_первого_фрагмента=random.randint(0,n-3)
    начало_первого_фрагмента=3

    начало_второго_фрагмента=random.randint(начало_первого_фрагмента+1,n-2)
    начало_второго_фрагмента=6
    первый_фрагмент=хромосома2[начало_первого_фрагмента:начало_второго_фрагмента]

    конец_второго_фрагмента=random.randint(начало_второго_фрагмента,n-1)
    конец_второго_фрагмента=10

    второй_фрагмент=хромосома3[начало_второго_фрагмента:(конец_второго_фрагмента)]

    хвост=хромосома4[(конец_второго_фрагмента):n]

    хромосома=хромосома1[0:начало_первого_фрагмента]
    хромосома=хромосома+первый_фрагмент+второй_фрагмент+хвост    
    return хромосома 

хромосома1=предок(12)
хромосома2=предок(12)
хромосома3=предок(12)
хромосома4=предок(12)

print(хромосома1)
print(хромосома2)
print(хромосома3)
print(хромосома4)

хромосома5=кроссовер_6(хромосома1,хромосома2, хромосома3, хромосома4)

print ("Потомок")
print(хромосома5)

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома1)),хромосома1)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома2)),хромосома2)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома3)),хромосома3)
plt.show()

fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома4)),хромосома4)
plt.show()

print ("Потомок")
fig, ax = plt.subplots(figsize=(20, 0.5))
plt.bar(range(0,len(хромосома5)),хромосома5)
plt.show()



# In[442]:


def предок2(n):
    хромосома= []
    for i in range(0,n):
        ген = random.random()
        хромосома.append(ген)
    return хромосома
    
#вещественные кроссоверы

fig, ax = plt.subplots(figsize=(20, 5))
предок=предок2(n)
ax.plot(range(0,len(предок)),предок, 'bo--')  # 
plt.show()
print(предок)


# In[443]:


#Кроссовер 7. плоский кроссовер
def кроссовер_7(хромосома1,хромосома2):
    хромосома=[]
    for i in range(0,n):
        xm=min(хромосома1[i], хромосома2[i])
        xM=max(хромосома1[i], хромосома2[i])
        хромосома.append(random.uniform(xm,xM))
    return хромосома

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_7(хромосома1,хромосома2)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома3)),хромосома2,'go--')
plt.plot(range(0,len(хромосома2)),хромосома3, 'ro-')
plt.show()


# In[444]:


#Кроссовер 8. эвристический (вариант арифметического)

def кроссовер_8(хромосома1,хромосома2):
    хромосома=[]
    L=len(хромосома1)
    for i in range(0,L):
        u=random.random();
        хромосома.append(u*хромосома1[i]+(1-u)*хромосома2[i])
    return хромосома

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_8(хромосома1,хромосома2)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома3)),хромосома2,'go--')
plt.plot(range(0,len(хромосома2)),хромосома3, 'ro-')
plt.show()


# In[445]:


#Кроссовер 9. расширенный линейный кроссовер

def кроссовер_9(хромосома1,хромосома2, b):
    хромосома=[]
    L=len(хромосома1)
    for i in range(0,L):
        b=0.1 # в общем случае b[i]
        xm=min(хромосома1[i], хромосома2[i])
        xM=max(хромосома1[i], хромосома2[i])
        delta=xM-xm
        хромосома.append(random.uniform(xm-b*delta,xM+b*delta))
    return хромосома

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3=кроссовер_9(хромосома1,хромосома2, 0.1)
print ("Потомок")
print(хромосома3)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома2)),хромосома2,'go--')
plt.plot(range(0,len(хромосома2)),хромосома3, 'ro-')
plt.show()


# In[446]:


#Кроссовер 10. кроссоверы с двумя потомками
#простейший 
def кроссовер_10(хромосома1, хромосома2):
    L=len(хромосома1)
    i=random.randint(0,L)
    потомок1=хромосома1[0:i]+хромосома2[i:L]
    потомок2=хромосома2[0:i]+хромосома1[i:L]
    return потомок1,потомок2

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3,хромосома4 =кроссовер_10(хромосома1,хромосома2)

print ("Потомки")
print(хромосома3)
print(хромосома4)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома2)),хромосома2,'go--')
plt.show()
fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома3)),хромосома3, 'ro-')
plt.plot(range(0,len(хромосома4)),хромосома4, 'ko-')
plt.show()


# In[447]:


#Кроссовер 11. арифметический кроссовер
def кроссовер_11(хромосома1, хромосома2):
    L=len(хромосома1)
    потомок1=[]
    потомок2=[]
    for i in range(0,L):
        u=random.random(); #если u одна и таже, то равномерный арифметический
        потомок1.append(u*хромосома1[i]+(1-u)*хромосома2[i])
        потомок2.append(u*хромосома2[i]+(1-u)*хромосома1[i])
    return потомок1,потомок2

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3,хромосома4 =кроссовер_11(хромосома1,хромосома2)

print ("Потомки")
print(хромосома3)
print(хромосома4)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома2)),хромосома2,'go--')
plt.show()
fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома3)),хромосома3, 'ro-')
plt.plot(range(0,len(хромосома4)),хромосома4, 'ko-')
plt.show()


# In[448]:


#Кроссовер 12. геометрический кроссовер

def кроссовер_12(хромосома1, хромосома2,b):
    L=len(хромосома1)
    потомок1=[]
    потомок2=[]
    for i in range(0,L):
        потомок1.append(pow(хромосома1[i],b)*pow(хромосома2[i],(1-b)))
        потомок2.append(pow(хромосома2[i],b)*pow(хромосома1[i],(1-b)))
    return потомок1,потомок2

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3,хромосома4 =кроссовер_12(хромосома1,хромосома2, 0.2)

print ("Потомки")
print(хромосома3)
print(хромосома4)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома2)),хромосома2,'go--')
plt.show()
fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома3)),хромосома3, 'ro-')
plt.plot(range(0,len(хромосома4)),хромосома4, 'ko-')
plt.show()


# In[449]:


##Кроссовер 13. нечеткий кроссовер
##Кроссовер 14. SBX кроссовер имитирующий бинарный кроссовер


# In[450]:


#Кроссовер 15. кроссоверы с тремя потомками


def кроссовер_15(хромосома1, хромосома2):
    L=len(хромосома1)
    потомок1=[]
    потомок2=[]
    потомок3=[]
    for i in range(0,L):
        u=random.random(); #если u одна и таже, то равномерный арифметический
        потомок1.append(0.5*хромосома1[i]+0.5*хромосома2[i])
        потомок2.append(1.5*хромосома1[i]-0.5*хромосома2[i])  
        потомок3.append(-0.5*хромосома1[i]+1.5*хромосома2[i])
    return потомок1,потомок2,потомок3

хромосома1=предок2(12)
хромосома2=предок2(12)

print(хромосома1)
print(хромосома2)

хромосома3,хромосома4, хромосома5 =кроссовер_15(хромосома1,хромосома2)

print ("Потомки")
print(хромосома3)
print(хромосома4)
print(хромосома5)

fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома1)),хромосома1, 'bo--')
plt.plot(range(0,len(хромосома2)),хромосома2,'go--')
plt.show()
fig, ax = plt.subplots(figsize=(20, 5))
plt.plot(range(0,len(хромосома3)),хромосома3, 'co-')
plt.plot(range(0,len(хромосома4)),хромосома4, 'ko-')
plt.plot(range(0,len(хромосома5)),хромосома5, 'ro-')
plt.show()


# In[451]:


#Операторы отбора

n0=20
n=4
хромосомы=[]
for i in range(0,n0):
    хромосома=[]
    for j in range(0,n):
        хромосома.append(random.random()) 
    хромосомы.append(хромосома)
print(хромосомы);
plt.plot(list(zip(*хромосомы)));     


# In[452]:



def f(x):
    return sum(x)

def Ff(x):
    L1,L=np.shape(x)
    s=[]
    for i in range(0,L):
        s.append(f(x[:,i]))
    return s
                     
import numpy as np
import seaborn as sns
популяция = np.random.rand(12, 40)
for i in range(0,12):
    for j in range(0,40):
        популяция[i][j]=random.randint(0,1)
fig, ax = plt.subplots(figsize=(20, 5))
ax = sns.heatmap(популяция, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(15, 5))
L1,L=np.shape(популяция)
plt.plot(range(0,L),Ff(популяция), 'bo--')
plt.xlim(-1,40)
plt.xticks(range(0,len(Ff(популяция))))
plt.show()


# In[ ]:





# In[453]:


##Отбор 1. метод рулетки
популяция2=np.transpose(популяция)
хромосомы = популяция2.tolist()

def отбор_1(хромосомы, k):
    n0=len(хромосомы)
    отбор=[]
    for j in range(0,k):
        h=[f(хромосомы[i]) for i in range(n0)]
        h2=[]
        h2.append(0)
        for i in range(0,n0-1):
            h2.append(h2[len(h2)-1]+h[i])   
        s=sum(h)
        u=random.uniform(0,s)
        q=0
        x=0
        for i in range(0,n0):
            if (u>h2[i]):
                x=i
        отбор.append(x)
    return(отбор)

nk=5
отобранные=популяция[:,отбор_1(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[454]:


##Отбор 2. метод пропорционального с остатком
популяция2=np.transpose(популяция)
хромосомы = популяция2.tolist()

def отбор_2(хромосомы, k):
    n0=len(хромосомы)
    отбор=[]
    for j in range(0,k):
        h1=[f(хромосомы[i]) for i in range(n0)]
        s=sum(h1)
        h=[]
        for i in range(0,n0):
            h.append(h1[i]/s)   

        h2=[]
        h2.append(0)
        for i in range(0,n0-1):
            h2.append(h2[len(h2)-1]+h[i])   
        
        u=random.uniform(0,1)
        #print(u)
        q=0
        x=0
        for i in range(0,n0):
            if (u>h2[i]):
                x=i
        отбор.append(x)
    return(отбор)

nk=5
отобранные=популяция[:,отбор_2(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[455]:


##Отбор 3. метод турнирного отбора
популяция2=np.transpose(популяция)
хромосомы = популяция2.tolist()

def отбор_3(хромосомы, размер_подгруппы):
    n0=len(хромосомы)
    h=[i for i in range(0,n)]
    hk=[]
    for i in range(0,n0):
        hk.append(f(хромосомы[i]))
    h=random.shuffle(h)
    m=int(n0/размер_подгруппы)
    победители=[]
    for i in range(0,m):
        m=f(хромосомы[размер_подгруппы*i]);
        k=размер_подгруппы*i;
        for j in range(1,размер_подгруппы):
            if (f(хромосомы[размер_подгруппы*i+j])>m):
                k=размер_подгруппы*i+j;
                m=f(хромосомы[размер_подгруппы*i+j])
        победители.append(k)
    return(победители)

m=4
отобранные=популяция[:,отбор_3(хромосомы, 4)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[456]:


##Отбор 4.1 метод рангового отбора

def f2(i):
    return f(хромосомы[i])

def dzeta1(j):
    a=-2
    b=1000
    return a*j+b

def отбор_4_1(хромосомы, k):
    n0=len(хромосомы)
    отбор=[]
    for j in range(0,k):
        h1=[f(хромосомы[i]) for i in range(n0)]
        h4=sorted(range(0,n0),reverse=True,key=f2)
        h=[dzeta1(h4.index(i)) for i in range(n0)]

        h2=[]
        h2.append(0)
        for i in range(0,n0-1):
            h2.append(h2[len(h2)-1]+h[i])   

        u=random.uniform(0,h2[len(h2)-1])
        q=0
        for i in range(0,n0):
            if (u>h2[i]):
                x=i
        отбор.append(x)
    return(отбор)

nk=5
отобранные=популяция[:,отбор_4_1(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[457]:


##Отбор 4.2 метод рангового отбора

def dzeta2(j):
    a=2
    b=-1
    c=2
    return a*np.exp(b*j+c)



def отбор_4_2(хромосомы, k):
    n0=len(хромосомы)
    отбор=[]
    for j in range(0,k):
        h1=[f(хромосомы[i]) for i in range(n0)]
        h4=sorted(range(0,n0),reverse=True,key=f2)
        h=[dzeta2(h4.index(i)) for i in range(n0)]

        h2=[]
        h2.append(0)
        for i in range(0,n0-1):
            h2.append(h2[len(h2)-1]+h[i])   

        u=random.uniform(0,h2[len(h2)-1])
        q=0
        for i in range(0,n0):
            if (u>h2[i]):
                x=i
        отбор.append(x)
    return(отбор)

nk=5
отобранные=популяция[:,отбор_4_2(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()



# In[458]:


##Отбор 5. метод на основе элитизма 

def отбор_5(хромосомы, k):
    n0=len(хромосомы)
    h4=sorted(range(0,n0),reverse=True,key=f2)
    return(h4[0:k])

nk=5
отобранные=популяция[:,отбор_5(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[459]:


##Отбор 6. метод отсечения 
def отбор_6(хромосомы, k):
    n0=len(хромосомы) 
    h1=[f(хромосомы[i]) for i in range(0,n0)]
    среднее=sum(h1)/n0

    h=[]
    for i in range(0,n0):
        if (f(хромосомы[i])>среднее):
            h.append(i)
    print(h)
    результат=[random.choice(h) for i in range(0,k)]
    return(результат)

nk=5
отобранные=популяция[:,отбор_6(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[460]:


##Отбор 7. метод отбора вытеснением 


# In[461]:


#Операторы селекции


# In[462]:


#Селекция 1. метод панмиксии

def селекция_1(x):
    L=len(x)
    h=[random.randint(0,L-1), random.randint(0,L-1)]
    return h

x=[]
y=[]

for i in range(0,20):
    s=селекция_1(хромосомы)
    x.append(s[0])
    y.append(s[1])

fig, ax = plt.subplots(figsize=(10, 10))
plt.plot(x,y, 'bo')

h=[]

for i in range(0,20):
    s=селекция_1(хромосомы)
    h.append(distance.hamming(хромосомы[s[0]], хромосомы[s[1]]))

fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(h, 'go')


# In[463]:


#Селекция 2. метод селективного отбора
def селекция_2(хромосомы,k):
    L=len(хромосомы)
    h1=[f(хромосомы[i]) for i in range(0,L)]
    среднее=sum(h1)/L
    h=[]
    for i in range(0,L):
        if (f(хромосомы[i])>среднее):
            h.append(i)
    h2=random.sample(h,k)
    результат=[random.choice(h2),random.choice(h2)]
    return результат
x=[]
y=[]

for i in range(0,20):
    s=селекция_2(хромосомы,3)
    x.append(f(хромосомы[s[0]]))
    y.append(f(хромосомы[s[1]]))
 
fig, ax = plt.subplots(figsize=(10, 10))   
plt.plot(x,y, 'bo')

h=[]

for i in range(0,20):
    s=селекция_2(хромосомы, 3)
    h.append(distance.hamming(хромосомы[s[0]], хромосомы[s[1]]))

fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(h, 'go')


# In[464]:


#Селекция 3. инбридинг

from scipy.spatial import distance

def селекция_3(хромосомы):
    L=len(хромосомы)
    y=random.randint(0,L-1)
    h=[]
    for i in range(0,L):
        if (i!=y):
            h.append(distance.hamming(хромосомы[y], хромосомы[i]))

    h2=[]
    h2.append(0)
    for i in range(0,L-1):
        h2.append(h2[len(h2)-1]+h[i])   
    s=sum(h)

    u=random.uniform(0,s)
    for i in range(0,L):
        if (u>h2[i]):
            x=i
    if (x>=y):
        x=x+1                                
    return [x,y]


x=[]
y=[]

for i in range(0,20):
    s=селекция_3(хромосомы)
    x.append(s[0])
    y.append(s[1])
 
fig, ax = plt.subplots(figsize=(10, 10))   
plt.plot(x,y, 'bo')

h=[]

for i in range(0,20):
    s=селекция_3(хромосомы)
    h.append(distance.hamming(хромосомы[s[0]], хромосомы[s[1]]))

fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(h, 'go')


# In[465]:


#Селекция 4. аутбридинг

def селекция_4(хромосомы):
    L=len(хромосомы)
    y=random.randint(0,L-1)
    h=[]
    for i in range(0,L):
        if (i!=y):
            h.append(1/(distance.hamming(хромосомы[y], хромосомы[i])+1))

    h2=[]
    h2.append(0)
    for i in range(0,L-1):
        h2.append(h2[len(h2)-1]+h[i])   
    s=sum(h)
    
    u=random.uniform(0,s)
    q=0
    for i in range(0,L):
        if (u>h2[i]):
            x=i
    if (x>=y):
        x=x+1                                
    return [x,y]




x=[]
y=[]

for i in range(0,20):
    s=селекция_4(хромосомы)
    x.append(s[0])
    y.append(s[1])
 
fig, ax = plt.subplots(figsize=(10, 10))   
plt.plot(x,y, 'bo')

h=[]

for i in range(0,20):
    s=селекция_4(хромосомы)
    h.append(distance.hamming(хромосомы[s[0]], хромосомы[s[1]]))

fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(h, 'go')


# In[466]:


#Учет ограничений
k0=10
def ограничение(x):
    s=[]
    for i in range (0,k0):
        if (abs(sum(x)-i)<0.2):
            s.append(0)
        else:
            s.append(1)
    return s


# In[467]:


#Ограничение 1. метод смертельных штрафов
h=[]
for i in range(0,n0):
    s=1
    for j in range(0,k0):
        s=s*ограничение(хромосомы[i])[j]
    if (s==1):
        h.append(i)
print(h)
                


# In[468]:


#Ограничение 2. метод статических штрафов


# In[469]:


#Ограничение 3. сегрегированный генетический алгоритм


# In[470]:


#Ограничение 4. метод редукции Орвуша


# In[471]:


#компелекс 1 


# шаг 0 создание популяции

def f(x):
    return sum(x)

def Ff(x):
    L1,L=np.shape(x)
    s=[]
    for i in range(0,L):
        s.append(f(x[:,i]))
    return s
                     
import numpy as np
import seaborn as sns
популяция = np.random.rand(12, 40)
for i in range(0,12):
    for j in range(0,40):
        популяция[i][j]=random.randint(0,1)
fig, ax = plt.subplots(figsize=(20, 5))
ax = sns.heatmap(популяция, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(15, 5))
L1,L=np.shape(популяция)
plt.plot(range(0,L),Ff(популяция), 'bo--')
plt.xlim(-1,40)
plt.xticks(range(0,len(Ff(популяция))))
plt.show()


# In[472]:


#шаг 2. отбор 

nk=10
отобранные=популяция[:,отбор_1(хромосомы, nk)]

fig, ax = plt.subplots(figsize=(nk+2.5, 5))
ax = sns.heatmap(отобранные, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(nk, 5))
L1,L=np.shape(отобранные)
plt.plot(range(0,L),Ff(отобранные), 'bo--')
plt.xlim(0,nk-1)
plt.xticks(range(0,L))
plt.show()


# In[473]:


#шаг 3 селекция

L1,L=np.shape(отобранные)

y=np.transpose(отобранные)
список_отобранных = y.tolist()

сколько_новых=30
план_скрещивания=[]
for i in range (0,сколько_новых):
    план_скрещивания.append(селекция_1(список_отобранных ))
план_скрещивания


# In[474]:


#шаг 4 кроссовер 4, скрещивание
for i in range (0,сколько_новых):
    хромосома1=список_отобранных[план_скрещивания[i][0]]
    хромосома2=список_отобранных[план_скрещивания[i][1]]
    новая=кроссовер_3(хромосома1,хромосома2)
    новая_с_мутацией=мутация_4(новая)
    список_отобранных.append(новая_с_мутацией)
популяция=список_отобранных


# In[475]:


поколений =1000

import numpy as np
import seaborn as sns


популяция = np.random.rand(12, 40)
for i in range(0,12):
    for j in range(0,40):
        популяция[i][j]=random.randint(0,1)
fig, ax = plt.subplots(figsize=(20, 5))
ax = sns.heatmap(популяция, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(15, 5))
L1,L=np.shape(популяция)
plt.plot(range(0,L),Ff(популяция), 'bo--')
plt.xlim(-1,40)
plt.xticks(range(0,len(Ff(популяция))))
plt.show()

начальная_популяция= популяция
популяция2=np.transpose(популяция)
хромосомы = популяция2.tolist()

nk=10
for i in range(0,поколений):
    отобранные_хромосомы=[]
    g=len(отбор_3(хромосомы, nk))
    for i in range(0,g):
        отобранные_хромосомы.append(хромосомы[i])

    план_скрещивания=[]
    
    L=len(отобранные_хромосомы)
    сколько_новых=40-L
    for i in range (0,сколько_новых):
        план_скрещивания.append(селекция_3(отобранные_хромосомы))
    
    for i in range (0,сколько_новых):
        хромосома1=отобранные_хромосомы[план_скрещивания[i][0]]
        хромосома2=отобранные_хромосомы[план_скрещивания[i][1]]
        новая=кроссовер_3(хромосома1,хромосома2)
        новая_с_мутацией=мутация_1(новая,0.8)
        отобранные_хромосомы.append(новая_с_мутацией)
    хромосомы=отобранные_хромосомы

популяция=np.transpose(np.array(хромосомы))
fig, ax = plt.subplots(figsize=(20, 5))
ax = sns.heatmap(популяция, cmap="YlGnBu")
plt.show()

fig, ax = plt.subplots(figsize=(15, 5))
L1,L=np.shape(популяция)
plt.plot(range(0,L),Ff(популяция), 'bo--')
plt.xlim(-1,40)
plt.xticks(range(0,len(Ff(популяция))))
plt.show()


# In[ ]:




