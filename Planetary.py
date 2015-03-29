 #planetary
 # f = force
 # G = universal gravitational constant
 # M = mass 1
 # m = mass 2
 # r = radius
 # kc = keplers constant
 # T = period
 from sympy import *
 
 f = (G * M * m) / (r**2)
 g = G * m /(r**2)
 
 kc = (K**3)/(T**2)