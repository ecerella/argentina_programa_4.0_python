"""
Escribir una clase Cuenta que tenga el siguiente comportamiento:

c = Cuenta('Pérez')   
d = Cuenta('López')            
c.acreditar(100, 'Sueldo') 
c.transferir(30, d)      
c.extraer(60, 'Shopping')        
c.saldo() ==> 10
d.saldo() ==> 40 
print(c) Cuenta de Pérez (10)
c.movimientos() ==> [('acreditación',100,'Sueldo'),('extracción',60,'Shopping'), ('extracción',30,'Cuenta de López')]
d.movimientos() ==> [('acreditación',30,'Cuenta de Pérez')]
d.extraer(100, 'Deudas') ==> ERROR ValueError: Fondos Insuficientes
"""