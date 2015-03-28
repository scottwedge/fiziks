#integrated Calculus aka Physics C

from sympy import *



#work
w = Integrate(forceNet * delta(x), t)

#power
p = diff(w, t)