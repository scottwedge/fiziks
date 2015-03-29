 # force others
 
from sympy import *
from abc import *
f = Symbol("f")
a = Symbol("a")
m = Symbol("m")
mu = Symbol("mu")
g = Symbol("g")
theta = Symbol("theta")
forceFriction = Symbol("Ff")
forceNormal = Symbol("Fn")

m = f / a # solve mass
a = f / m # solve acceeration with force and mass
mu = forceFriction / forceNormal  # solve for mu
mu = forceFriction / m / g / sin(theta) # solve for mu with no normal force
