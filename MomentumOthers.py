# Momentum Others

 from sympy import *
 
 t = (m * v) / f # time using mass, velocity and force
 t = delta(p) / f # t using change in momentum and force
 t = I / t # time using impulse and force
  f = (m * v) / t # force using mass, velocity and force
 f = delta(p) / t # force using change in momentum and time
 f = I / t # force using impulse and time
 m1 = (-m2* v2 + m2 *v4) /(v1 - v3) # solve m1 in hit and seperate
 m2 = (-m1 * v1 + m1 *v3) / (v2 - v4) # solve m2 in hit and seperate
 v1 = (m1 * v3 + m2 * v4 - m2 * v2) / m1 # solve v1 in hit and seperate
 v2 = (m1 * v3 + m2 * v4 - m1 * v1) / m2 # solve v2 in hit and seperate
 v3 = (m1 * v3 + m2 * v4 - m2 * v2) / m1 # solve v3 in hit and seperate
  v4 = (m1 * v3 + m2 * v4 - m1 * v1) / m2 # solve v4 in hit and seperate
  v1 = (((m1 + m2) * v3) - (m2 * v2))/m1 # solve v1 in hit and stick
  v2 = (((m1 + m2) * v3) - (m1 * v1))/m2 # solve v2 in hit and stick
  v3 = (m1 * v1  + m2*v2) / (m1 + m2) # solve v3 in hit and stick
  m1 = ((m2 * v3) - ( m2 * v2)) / (v1 - v3) # m1 for hit and stick
  m2 = ((m1 * v3) - ( m1 * v1)) / (v2 - v3) #m2 for hit and stick