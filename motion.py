#Motion Equations
from  sympy import *


delta(x) = v * t  #Basic Distance Travelled
delta(x) = v1 * t + .5 * a * (t**2) #Distance Travelled with Acceleration
v2 = v1 + a * t   #New velocity with time
v2**2 = v1**2 + 2 * a * delta(x) #New Velocity with distance travelled


#Equation input
x = integrate(v,t)
v = diff(x,t) #Velcotiy from Distance
a = diff(v,t) #Acceleration from Velocity
v = integrate(a,t) #Velocity from Acceleration
x = integrate(v,t) #Distance from Velocity
 
  #projectile motion
  
   r = ((v**2) * sin(2*theta))/(2*g) #Max Range
   h = ((v**2) * sin(2*theta))/(2*g) #Max Height
   
   v2y = v1y + a * t #Motion y vectors
   delta(y) = v1 * t + .5 * a * (t**) #Motion y vectors
   v2x = v1x #Motion x vectors
   delta(x) = v1 * t #Motion x vectors
   
   triangle = ((x**2) + (y**2))**.5 #Y vector and X vector for hypotenuse