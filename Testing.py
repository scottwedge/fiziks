from Graphics import *
from sympy import *
import Gtk

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def showEquationBaseMenu(o, e):
    forceNet.draw(win)
    forceNormal.draw(win)
    forceApplied.draw(win)
    forceFriction.draw(win)
    forcePlanetary.draw(win)
    solveVariable.hide(win)
def showVariableMenu(o, e):
    forceNet.draw(win)
    forceNormal.draw(win)
    forceApplied.draw(win)
    forceFriction.draw(win)
    forcePlanetary.draw(win)
    solveVariable.delete(win)
    #.draw(win)

def showVariableBaseMenu(o, e):
    welcome.draw(win)
    #welcome.undraw(win)    
win = Window("Fiziks Mill", 400, 400)

forceNet = Button((150, 150), "Net Force")
forceNormal = Button((150, 170), "Normal Force")
forceApplied = Button((150, 190), "Applied Force")
forceFriction = Button((150, 210), "Force of Friction")
forcePlanetary = Button((150, 230), "Planetary Force")

solveEquations = Button((150, 150), "Solve Equation")
solveEquations.draw(win)
solveEquations.connect("click", showEquationBaseMenu)
solveVariable = Button((150, 200), "Solve Variable")
solveVariable.draw(win)
solveVariable.connect("click", showSolveMenu)






## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
## solveEquations = Button((150, 150), "Solve Equation")
