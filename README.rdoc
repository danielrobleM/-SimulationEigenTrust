#UDP Modelos Estocasticos 2013 

#### Simulación de EigenTrust Simple non-distributed V 0.1

<p>Guillermo Labra - Daniel Roble </p>
memolabra@me.com - daniel12dar@gmail.com

#####Descripción

SimulationEigenTrust.py permite generar una simulación del metodo de Eigentrust Simple y no distribuida ( Simple non-distributed) descrito en <em>The EigenTrust Algorithm For Reputation Management in P2P Networks</em>.
##### Consideraciones
En esta primera versión se ha utilizado una matriz 4x4 predefinida,que representa un total de 4 peers en la simulación. 
##### Outputs
<ul>
<li>Matriz S,j</li>
<li>Vector de confianza e</li>
<li>Matriz Ci,j o Matriz Normalizada</li>
<li>Vector Trapuesto t</li>
<li>Matriz Ct resprentala matriz Ci,j Tranpuesta</li> 
</ul>
<ul>
<p>Finalmente se presentan solo dos tipos de Outputs</p>
<li><em>Suma vector t2</em> representa la suma de los valores del nuevo vector t en cada iteración</li>
<li>El valor de <em>Delta</em> en cada iteracion</li>
</ul>
##### Lenguaje y Complementos
<ul>
<li>Python 2.7</li>
<li>Complemento NumPy (*)</li>
<p>(*) Disponible en:  <a href="https://pypi.python.org/pypi/numpy">python.org/numpy</a><p>
</ul>
##### Instrucciones 

 * Version de Python 2,7
 * Compilar utilizando:
 <pre><code> > python SimulationEigenTrust.py  
</code></pre>
 



