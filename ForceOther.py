 # force others
 
 from sympy import *
 
 
 m = f / a # solve mass
 a = f / m # solve acceeration with force and mass
 mu = forceFriction / forceNormal  # solve for mu
 mu = forceFriction / m / g / sin(theta) # solve for mu with no normal force
 