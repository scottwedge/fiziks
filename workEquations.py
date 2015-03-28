#work equations
#w is work

from sympy import *
import energyEquations

w = delta(energyEquations.ke) + delta(energyEquations.peGravitational) + delta(energyEquations.peSpring)