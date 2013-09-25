from __future__ import division
import numpy as np
from numpy import matrix
from numpy import linalg as LA


print 'Escoge a simular '
print '0 EigenTrust Simple non-distributed '
print '1 EigenTrust Basic non-distributed '

TipoDeSimulacion=int(raw_input(""))
if(TipoDeSimulacion==0):
    #Numero Total de peers a simular
    Dimension=int(raw_input("Ingresar dimension matriz"))
    B =np.random.randint(5, size=(Dimension, Dimension))
    print B


    #A = matrix( [[0,3,1,0],[1,0,4,7],[2,-1,0,-1],[-5,4,3,0]])
    #B= np.matrix('0 3 1 0; 1 0 4 7; 2 -1 0 -1 ;-5 4 3 0')
    MatrixNormal=np.identity(Dimension)
    print 'Matriz Sij ='
    print MatrixNormal

    # Normalizing Local Trust Values

    for i in range(len(B)):
        for j in range(len(B)):
            value=max((B[i,j]),0)
            B[i,j]=value
    	 #print B

    for i in range(len(B)):
        for j in range(len(B)):
            C=B.sum(axis=1) # suma de la fila
    	#print C
            SumaDeLaFila=int(C[i])
    	#print 'la fila suma ',SumaDeLaFila
            if C[i]==0:
                print ' Simple no funca'
            else:
                #print 'aca voy a dividir ',B[i,j],'/',SumaDeLaFila
                value=int(B[i,j])
                valueForNormalMatrix=value/SumaDeLaFila
                #print valueForNormalMatrix
            MatrixNormal[i,j]= float(valueForNormalMatrix)


    #Generando el Vecto de Confianza e
    e= np.empty(Dimension)
    matrix(e.fill(1/Dimension))

    print 'Vecto de Confianza e =',e
    print "Matrix Normal "
    print MatrixNormal

    #Comienza iteracion
    Delta=1
    t=e.T
    print 'Vector Trapuesto t',t
    Ct=MatrixNormal.transpose()
    print 'Matriz Ct'
    print Ct
    while (Delta>0.0000001):
     	t2=np.dot(Ct,t)
     	#print'Vector t multiplicado =' , t2
     	print 'Suma vector t2 =',t2.sum(axis=0)
     	RestaVectores=t2-t
     	Delta=LA.norm(RestaVectores)
     	print'Delta=',Delta
     	t=t2

    print 'Ultimo Delta',Delta
    print 'Vector t2 final', t2.sum(axis=0)

if (TipoDeSimulacion==1):
    print 'Aca va el codigo 2'











