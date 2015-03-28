#Motion Equations
from  sympy import *


delta(x) = v * t
delta(x) = v1 * t + .5 * a * (t**2)
v2 = v1 + a * t
v2**2 = v1**2 + 2 * a * delta(x)
v = diff(x,t)
a = diff(v,t)
v = integrate(a,t)
x = integrate(v,t)

 
  #projectile motion
  
   r = ((v**2) * sin(2*theta))/(2*g)
   h = ((v**2) * sin(2*theta))/(2*g)
   
   v2y = v1y + a * t
   delta(y) = v1 * t + .5 * a * (t**)
   v2x = v1x
   delta(x) = v1 * t
   
   triangle = ((x**2) + (y**2))**.5