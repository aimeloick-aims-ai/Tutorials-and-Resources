# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 08:29:29 2023

@author: HOME
"""


#library
import numpy as np 
from scipy import integrate
#Condition initiale
nt=10  
dt=1
# Condition initiale
zo=0
uo=2
vo=3
#Definir C 
C=1


def det(x1,y1,x2,y2,x3,y3):
    detJ=(x2-x1)*(y3-y1)-(y2-y1)*(x3-x1)
    return abs(detJ)

def Jaco(x1,y1,x2,y2,x3,y3):
    Jaco=np.matrix([[x2-x1,y2-y1],[x3-x1 ,y3-y1]])
    return Jaco
def AR(x1,y1,x2,y2,x3,y3):
    Jp=Jaco(x1,y1,x2,y2,x3,y3)
    k=np.matrix([[-1,1,0],[1,0,1]])
    Jk=np.dot(Jp,k)
    return Jk
MH= np.matrix([[-1/6,-1/12, -1/12],[-1/12 ,1/3,1/4],[-1/12 ,1/4,1/3]])
#Calcule de Me
def Me(x1,y1,x2,y2,x3,y3):
    dets=det(x1,y1,x2,y2,x3,y3)
    Me1=1/dt*(dets)*MH
    return Me1
dN=np.matrix([0,1/2,1/2])
def Rex(x1,y1,x2,y2,x3,y3):
    dets=det(x1,y1,x2,y2,x3,y3)
    ARc=AR(x1,y1,x2,y2,x3,y3)
    Re1=dets*np.dot(dN.T,ARc[0])
    return Re1
def Rey(x1,y1,x2,y2,x3,y3):
    dets=det(x1,y1,x2,y2,x3,y3)
    ARc=AR(x1,y1,x2,y2,x3,y3)
    Re2=dets*np.dot(dN.T,ARc[1])
    return Re2
#f(x,y)=1
def Fe(x1,y1,x2,y2,x3,y3):
    dets=det(x1,y1,x2,y2,x3,y3)
    Fe1=(dets)*MH
    return Fe1
#La grande matrice élémentaire 

def matrice(x1,y1,x2,y2,x3,y3):
    Mee1=Me(x1,y1,x2,y2,x3,y3)
    Ree1=Rex(x1,y1,x2,y2,x3,y3)
    Ree2=Rey(x1,y1,x2,y2,x3,y3)
    Fee1=Fe(x1,y1,x2,y2,x3,y3)
    matrice_ele = np.block([[Mee1, Ree1,Ree2 ],
                               [Ree1,Mee1,-(C^2)*Fee1],
                               [ Ree2,(C^2)*Fee1,Mee1]])
    return matrice_ele
#Premier second membre 
#Vecteur inital V(z1_0,z2_0,z3_0,u1_0,u2_0,u3_0,v1_0,v2_0,v3_0)
#ici on va supposer que c'est la meme chose pour chaque élément
V=np.matrix([[zo,zo,zo],[uo,uo,uo],[vo,vo,vo]])
def secondm(x1,y1,x2,y2,x3,y3,V):
    Mee1=Me(x1,y1,x2,y2,x3,y3)
     
    
    Fi = np.zeros((9))
    Fi[0:3]= np.dot(Mee1,V[0].T).flatten()
    Fi[3:6]= np.dot(Mee1,V[1].T).flatten()
    Fi[6:9]= np.dot(Mee1,V[2].T).flatten()
    return Fi
    
def element(x1,y1,x2,y2,x3,y3):
    Fini=np.zeros((nt,9))
   
    premier=matrice(x1,y1,x2,y2,x3,y3)
    V=np.matrix([[0,0,0],[2,2,2],[3,3,3]])
    Fini[0]=V.reshape(1,9)
    for i in range(nt-1):
        k=np.linalg.inv(premier)
        V=secondm(x1,y1,x2,y2,x3,y3,V)
        kd=np.dot(k,V)
        Fini[i+1]=kd
        # Conversion en matrice 3x3
        V=V.reshape(3, 3)
        
    return Fini


###################################  Maillage   ###############################

import matplotlib.tri as tri
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
N=7
Ny=9

Nx=N+1
Xn=np.linspace(0,Nx-1,Nx)
Xt=np.linspace(0,Nx-1,Nx)
Yt=np.zeros(Nx)
Yc=np.ones(Nx)
for i in range(Ny):
    Xt=np.concatenate((Xt, Xn))
    b=(i+1)*Yc
    Yt=np.concatenate((Yt, b))
    
#Yt=np.linspace(0,Ny,1)
# Index des triangles, chaque ligne représente les indices des nœuds formant un triangle
Nxy=int((Nx*Ny))
triangles=np.array([[0,1,Nx],[Nx+1, Nx, 1]])
for i in range(Nxy-2):
    I=i+1
    if((I+1)%Nx!=0):
       I=i+1
       new_lines = np.array([
       [0+I,1+I,Nx+I],  
       [1+I, Nx+1+I, Nx+I]  ])
       triangles = np.vstack((triangles, new_lines))  
#print('Elements ')
#print(triangles)

# Représentation du maillage
plt.figure()
plt.gca().set_aspect('equal')
plt.triplot(Xt, Yt, triangles, 'b-', lw=0.5)
plt.title('Maillage avec éléments finis en triangle')
plt.show()

#Matrice des x

# Accès aux coordonnées de chaque triangle
Z=np.zeros(((N+1)*(Ny+1),nt))
U=np.zeros(((N+1)*(Ny+1),nt))
V=np.zeros(((N+1)*(Ny+1),nt))
for tr in triangles:
    tc = np.array([[Xt[i], Yt[i]] for i in tr])
    #print(tc)
    ele=element(tc[0,0],tc[0,1],tc[1,0],tc[1,1],tc[2,0],tc[2,1])
    print(ele)
    #print(tr)
    for t in range(nt):
      Z[tr,t]+=ele[t,0:3]
      U[tr,t]+=ele[t,3:6]
      V[tr,t]+=ele[t,6:9]
###################################### Representation Z #####################################"
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Pour Z
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Tracer les points
ax.scatter(Xt, Yt,Z[:,8] , c='r', marker='o')
# Relier les points pour former une surface
trid = Delaunay(np.array([Xt, Yt]).T)
ax.plot_trisurf(np.array(Xt), np.array(Yt), np.array(Z[:,8]), triangles=trid.simplices, cmap='viridis')
# Étiqueter les axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
###################################### Representation U #####################################"


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Tracer les points
ax.scatter(Xt, Yt,U[:,8] , c='r', marker='o')
# Relier les points pour former une surface
trid = Delaunay(np.array([Xt, Yt]).T)
ax.plot_trisurf(np.array(Xt), np.array(Yt), np.array(U[:,8]), triangles=trid.simplices, cmap='viridis')
# Étiqueter les axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('U')

plt.show()
###################################### Representation V #####################################"

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Tracer les points
ax.scatter(Xt, Yt,V[:,8] , c='r', marker='o')
# Relier les points pour former une surface
trid = Delaunay(np.array([Xt, Yt]).T)
ax.plot_trisurf(np.array(Xt), np.array(Yt), np.array(V[:,8]), triangles=trid.simplices, cmap='viridis')
# Étiqueter les axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('V')

plt.show()

###################################### Animation #####################################"
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import os
X=Xt
Y=Yt

# Fonction pour mettre à jour le graphique pour chaque trame (frame)
def update(frame):
    ax.clear()
    ax.scatter(X, Y, Z[:, frame], c='r', marker='o')  # Utilisation de Z[:, frame] pour spécifier la colonne correspondant à la trame actuelle
    trid = Delaunay(np.array([X, Y]).T)
    ax.plot_trisurf(np.array(X), np.array(Y), np.array(Z[:, frame]), triangles=trid.simplices, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Frame {}'.format(frame))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Création de l'animation
ani = FuncAnimation(fig, update, frames=range(10), interval=2000)  # 10 trames, intervalle de 200ms entre chaque trame

# Sauvegarde de l'animation en tant que fichier GIF
ani.save('animation.gif', writer='pillow')
plt.show()
os.startfile("animation.gif")  # Ouvre le fichier avec le programme par défaut (Windows)

        
        
