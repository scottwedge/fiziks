#Force Equations
from sympy import *





forceNet = m * a
forceNormal = m * g * sin(theta)
forceFriction = mu * forceNormal
forceApplied = m * a
forcePlanetary = G * massSmall * massBig / r**2
