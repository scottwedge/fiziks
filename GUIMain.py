from Graphics import *
from sympy import *
#import force

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def showEquationBaseMenu(o, e):
    equationBaseMenu = Window("Solve Equation", 200, 200)
    force.draw(equationBaseMenu)
    motion.draw(equationBaseMenu)
    momentumButton.draw(equationBaseMenu)
    energy.draw(equationBaseMenu)
    work.draw(equationBaseMenu)
    centerOfMass.draw(equationBaseMenu)
    circularMotion.draw(equationBaseMenu)
def showVariableMenu(o, e):
    variableBaseMenu = Window("Solve Variable", 200, 200)
    forceNet.draw(variableBaseMenu)
    forceNormal.draw(variableBaseMenu)
    forceApplied.draw(variableBaseMenu)
    forceFriction.draw(variableBaseMenu)
    forcePlanetary.draw(variableBaseMenu)
def showForceBaseMenu(o, e):
    equationForceMenu = Window("Solve Force Equation", 200, 200)
    forceNet.draw(equationForceMenu)
    forceNormal.draw(equationForceMenu)
    forceApplied.draw(equationForceMenu)
    forceFriction.draw(equationForceMenu)
    forcePlanetary.draw(equationForceMenu)
def showMomentumBaseMenu(o, e):
    equationMomentumMenu = Window("Solve Momentum Equation", 400, 300)
    momentum.draw(equationMomentumMenu)
    impulseFirst.draw(equationMomentumMenu)
    impulseSecond.draw(equationMomentumMenu)
    impulseThird.draw(equationMomentumMenu)
    conservationOfMomentum.draw(equationMomentumMenu)
    hitAndSeperate.draw(equationMomentumMenu)
    hitAndStick.draw(equationMomentumMenu)
    
    
def showMotionBaseMenu(o, e):
    equationMotionMenu = Window("Solve Motion Equation", 400, 300)
    momentum.draw(equationMotionMenu)
    impulseFirst.draw(equationMotionMenu)
    impulseSecond.draw(equationMotionMenu)
    impulseThird.draw(equationMotionMenu)
    conservationOfMomentum.draw(equationMotionMenu)
    hitAndSeperate.draw(equationMotionMenu)
    hitAndStick.draw(equationMotionMenu)
def showEnergyBaseMenu(o, e):
    equationEnergyMenu = Window("Solve Energy Equation", 400, 300)
    momentum.draw(equationEnergyMenu)
    impulseFirst.draw(equationEnergyMenu)
    impulseSecond.draw(equationEnergyMenu)
    impulseThird.draw(equationEnergyMenu)
    conservationOfMomentum.draw(equationEnergyMenu)
    hitAndSeperate.draw(equationEnergyMenu)
    hitAndStick.draw(equationEnergyMenu)
def showWorkBaseMenu(o, e):
    equationWorkMenu = Window("Solve Work Equation", 400, 300)
    momentum.draw(equationWorkMenu)
    impulseFirst.draw(equationWorkMenu)
    impulseSecond.draw(equationWorkMenu)
    impulseThird.draw(equationWorkMenu)
    conservationOfMomentum.draw(equationWorkMenu)
    hitAndSeperate.draw(equationWorkMenu)
    hitAndStick.draw(equationWorkMenu)
def showCenterOfMassBaseMenu(o, e):
    equationCenterOfMassMenu = Window("Solve Center Of Mass Equation", 400, 300)
    momentum.draw(equationCenterOfMassMenu)
    impulseFirst.draw(equationCenterOfMassMenu)
    impulseSecond.draw(equationCenterOfMassMenu)
    impulseThird.draw(equationCenterOfMassMenu)
    conservationOfMomentum.draw(equationCenterOfMassMenu)
    hitAndSeperate.draw(equationCenterOfMassMenu)
    hitAndStick.draw(equationCenterOfMassMenu)
def showCircularMotionBaseMenu(o, e):
    equationCircularMotionMenu = Window("Solve Circular Motion Equation", 400, 300)
    momentum.draw(equationCircularMotionMenu)
    impulseFirst.draw(equationCircularMotionMenu)
    impulseSecond.draw(equationCircularMotionMenu)
    impulseThird.draw(equationCircularMotionMenu)
    conservationOfMomentum.draw(equationCircularMotionMenu)
    hitAndSeperate.draw(equationCircularMotionMenu)
    hitAndStick.draw(equationCircularMotionMenu)

def showVariableBaseMenu(o, e):
    welcome.draw(win)
    #welcome.undraw(win)    
win = Window("Fiziks Mill", 400, 400)

#Equation Base Menu Buttons
force = Button((50, 50), "Force")
motion = Button((50, 70), "Motion")
momentumButton = Button((50, 90), "Momentum")
energy = Button((50, 110), "Energy")
work = Button((50, 130), "Planetary Force")
centerOfMass = Button((50, 150), "Center Of Mass")
circularMotion = Button((50, 170), "Circular Motion")

#Force Menu Buttons
forceNet = Button((50, 50), "Net Force")
forceNormal = Button((50, 70), "Normal Force")
forceApplied = Button((50, 90), "Applied Force")
forceFriction = Button((50, 110), "Force of Friction")
forcePlanetary = Button((50, 130), "Planetary Force")

#Motion Menu Buttons
forceNet = Button((50, 50), "Net Force")
forceNormal = Button((50, 70), "Normal Force")
forceApplied = Button((50, 90), "Applied Force")
forceFriction = Button((50, 110), "Force of Friction")
forcePlanetary = Button((50, 130), "Planetary Force")
#Momentum Menu Buttons
momentum = Button((50, 50), "Momentum")
impulseFirst = Button((50, 70), "Impulse with Change in Momentum")
impulseSecond = Button((50, 90), "Impulse with Force and Change in Time")
impulseThird = Button((50, 110), "Impulse with Mass and Change in Velocity")
conservationOfMomentum = Button((50, 130), "Conservation Of Momentum")
hitAndSeperate = Button((50, 150), "Hit and Seperate")
hitAndStick = Button((50, 170), "Hit and Stick")
## #Energy Menu Buttons
## forceNet = Button((50, 50), "Net Force")
## forceNormal = Button((50, 70), "Normal Force")
## forceApplied = Button((50, 90), "Applied Force")
## forceFriction = Button((50, 110), "Force of Friction")
## forcePlanetary = Button((50, 130), "Planetary Force")
## #Work Menu Buttons
## forceNet = Button((50, 50), "Net Force")
## forceNormal = Button((50, 70), "Normal Force")
## forceApplied = Button((50, 90), "Applied Force")
## forceFriction = Button((50, 110), "Force of Friction")
## forcePlanetary = Button((50, 130), "Planetary Force")
## #Center of Mass Menu Buttons
## forceNet = Button((50, 50), "Net Force")
## forceNormal = Button((50, 70), "Normal Force")
## forceApplied = Button((50, 90), "Applied Force")
## forceFriction = Button((50, 110), "Force of Friction")
## forcePlanetary = Button((50, 130), "Planetary Force")
## #Circular Menu Buttons
## forceNet = Button((50, 50), "Net Force")
## forceNormal = Button((50, 70), "Normal Force")
## forceApplied = Button((50, 90), "Applied Force")
## forceFriction = Button((50, 110), "Force of Friction")
## forcePlanetary = Button((50, 130), "Planetary Force")

#Base Menu Buttons
solveEquations = Button((150, 150), "Solve Equation")
solveEquations.draw(win)
solveEquations.connect("click", showEquationBaseMenu)
solveVariable = Button((150, 200), "Solve Variable")
solveVariable.draw(win)
solveVariable.connect("click", showVariableMenu)

#Button Connectors
force.connect("click", showForceBaseMenu)
motion.connect("click", showMotionBaseMenu)
momentumButton.connect("click", showMomentumBaseMenu)
energy.connect("click", showEnergyBaseMenu)
work.connect("click", showWorkBaseMenu)
centerOfMass.connect("click", showCenterOfMassBaseMenu)
circularMotion.connect("click", showCircularMotionBaseMenu)

