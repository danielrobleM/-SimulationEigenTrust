from __future__ import division
import numpy as np
from numpy import matrix
from numpy import linalg as LA
print 'Escoge a simular '
print '0 EigenTrust Simple non-distributed '
print '1 EigenTrust Basic non-distributed '

TipoDeSimulacion=int(raw_input("Inserte el numero de la simulacion:"))
if(TipoDeSimulacion==0):
 	
#Numero Total de peers a simular 
 NumeroDePeers =4
#NumeroDePeers =int(raw_input("Inserte el numero de peers para la Simulacion :"))
#Generar Matriz Sij

 A = matrix( [[0,3,1,0],[1,0,4,7],[2,-1,0,-1],[-5,4,3,0]]) 
 B= np.matrix('0 3 1 0; 1 0 4 7; 2 -1 0 -1 ;-5 4 3 0')
 MatrixNormal=np.matrix('0.1 3 1 0; 1 0 4 7; 2 -1 0 -1 ;-5 4 3 0')
 #print MatrixNormal.reshape(2,2)
 AS=np.identity(NumeroDePeers)
 a = np.empty(4)
 a.fill(3)
 print 'nuevo memo',a
 print 'AS',AS
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
 e=np.matrix([1/NumeroDePeers,1/NumeroDePeers,1/NumeroDePeers,1/NumeroDePeers])
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
   	
#Numero Total de peers a simular 
 NumeroDePeers =4
#NumeroDePeers =int(raw_input("Inserte el numero de peers para la Simulacion :"))
#Generar Matriz Sij

 A = matrix( [[0,3,1,0],[1,0,4,7],[2,-1,0,-1],[-5,4,3,0]]) 
 B= np.matrix('0 3 1 0; 1 0 4 7; 2 -1 0 -1 ;-5 4 3 0')
 MatrixNormal=np.matrix('0.1 3 1 0; 1 0 4 7; 2 -1 0 -1 ;-5 4 3 0')
 #print MatrixNormal.reshape(2,2)
 AS=np.identity(NumeroDePeers)
 a = np.empty(4)
 a.fill(3)
 print 'nuevo memo',a
 print 'AS',AS
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
 e=np.matrix([1/NumeroDePeers,1/NumeroDePeers,1/NumeroDePeers,1/NumeroDePeers])
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
 
 

 	    










