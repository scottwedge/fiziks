#Force Equations
#m is mass
#a is acceleration
#g is gravity
#mu s the coeficient of kinetic friction
#theta is the angle
#r is the radius between the planetary systems

from sympy import *

forceNet = m * a
forceNormal = m * g * sin(theta)
forceFriction = mu * forceNormal
forceApplied = m * a
forcePlanetary = G * massSmall * massBig / r**2