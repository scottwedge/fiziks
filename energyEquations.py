#Energy equations
#m is mass
#v is velocity
#h is height
#g is gravity
#k is k value of spring
#x is spring compression 

from sympy import *

ke = (0.5) * m * (v**2) #kinetic energy
peGravitational = m * g * h #Gravitational Potential Energy
peSpring =  (0.5) * k * (x**2) #Spring Potential Energy