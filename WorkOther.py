#Work Other

 from sympy import *
 
 f = w/delta(x) # force solving with work
 delta(x) = work / f # displacement solving with work
 ke = w - peGravitational - peSpring # ke solving with work
 peGravitational = w - ke - peSpring # peGravitational solving with work
 peSpring = w - ke - peGravitational # peSpring solving with work
 
 