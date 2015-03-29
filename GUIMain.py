from Graphics import *
from sympy import *
#import force

x, y, z = symbols('x y z')
init_printing(use_unicode=True)

0
class BaseMenu(object):
    def __init__(self):
        self.win = Window("Fiziks Mill", 400, 400)
        self.solveEquations = Button((150, 150), "Solve Equation")
        self.solveVariable = Button((150, 200), "Solve Variable")
        self.solveEquations.draw(self.win)
        self.solveVariable.draw(self.win)
        #Button Connectors
        self.solveEquations.connect("click", self.showEquationMenu)
        self.solveVariable.connect("click", self.showVariableMenu)
    def showEquationMenu(self, o, e):
        equationBaseMenu = EquationBaseMenu()
    def showVariableMenu(self, o, e):
        showVariableMenu = ShowVariableMenu()
class EquationBaseMenu(object):
    def __init__(self):
        #Equation Base Menu Buttons
        self.force = Button((50, 50), "Force")
        self.motion = Button((50, 70), "Motion")
        self.momentumButton = Button((50, 90), "Momentum")
        self.energy = Button((50, 110), "Energy")
        self.work = Button((50, 130), "Work")
        self.planetaryForce = Button((50, 150), "Planetary Force")
        self.centerOfMass = Button((50, 170), "Center Of Mass")
        self.circularMotion = Button((50, 190), "Circular Motion")
        
        self.equationBaseMenu = Window("Solve Equation", 200, 300)
        self.force.draw(self.equationBaseMenu)
        self.motion.draw(self.equationBaseMenu)
        self.momentumButton.draw(self.equationBaseMenu)
        self.energy.draw(self.equationBaseMenu)
        self.work.draw(self.equationBaseMenu)
        self.planetaryForce.draw(self.equationBaseMenu)
        self.centerOfMass.draw(self.equationBaseMenu)
        self.circularMotion.draw(self.equationBaseMenu)
        
        self.force.connect("click", self.showForceBaseMenu)
        self.motion.connect("click", self.showMotionBaseMenu)
        self.momentumButton.connect("click", self.showMomentumBaseMenu)
        self.energy.connect("click", self.showEnergyBaseMenu)
        self.work.connect("click", self.showWorkBaseMenu)
        self.planetaryForce.connect("click", self.showPlanetaryForceBaseMenu)
        self.centerOfMass.connect("click", self.showCenterOfMassBaseMenu)
        self.circularMotion.connect("click", self.showCircularMotionBaseMenu)
    
    def showForceBaseMenu(self, o, e):
        forceBaseMenu = ShowForceBaseMenu()
    def showMotionBaseMenu(self, o, e):
        showMotionMenu = ShowMotionBaseMenu()
    def showMomentumBaseMenu(self, o, e):
        momentumBaseMenu = ShowMomentumBaseMenu()
    def showEnergyBaseMenu(self, o, e):
        showEnergyMenu = ShowEnergyBaseMenu()
    def showWorkBaseMenu(self, o, e):
        workBaseMenu = ShowWorkBaseMenu()
    def showPlanetaryForceBaseMenu(self, o, e):
        planetaryForceBaseMenu = ShowPlanetaryForceBaseMenu()
    def showCenterOfMassBaseMenu(self, o, e):
        showCenterOfMassMenu = ShowCenterOfMassBaseMenu()
    def showCircularMotionBaseMenu(self, o, e):
        forceCircularMotionMenu = ShowCircularMotionBaseMenu()

class ShowVariableMenu(object):
    def __init__(self):
        #Equation Base Menu Buttons
        self.force = Button((50, 50), "Force")
        self.motion = Button((50, 70), "Motion")
        self.momentumButton = Button((50, 90), "Momentum")
        self.energy = Button((50, 110), "Energy")
        self.work = Button((50, 130), "Planetary Force")
        self.centerOfMass = Button((50, 150), "Center Of Mass")
        self.circularMotion = Button((50, 170), "Circular Motion")       
        #input draw things here
        #input connectors here      
   

class ShowForceBaseMenu(object):
    def __init__(self):
        self.forceNet = Button((50, 50), "Net Force")
        self.forceNormal = Button((50, 70), "Normal Force")
        self.forceApplied = Button((50, 90), "Applied Force")
        self.forceFriction = Button((50, 110), "Force of Friction")
        self.forcePlanetary = Button((50, 130), "Planetary Force")
        self.forceMass = Button((50,150), "Solve for mass")
        self.forceAcceleration = Button((50,170), "Solve for Acceleration")
        self.mu = Button((50,190), "Solve for mu")
        self.mu2 = Button((50,210), "Solve for mu with out normal force")

        
        self.equationForceMenu = Window("Solve Force Equation", 400, 300)
        self.forceNet.draw(self.equationForceMenu)
        self.forceNormal.draw(self.equationForceMenu)
        self.forceApplied.draw(self.equationForceMenu)
        self.forceFriction.draw(self.equationForceMenu)
        self.forcePlanetary.draw(self.equationForceMenu)
        self.forceMass.draw(self.equationForceMenu)
        self.forceAcceleration.draw(self.equationForceMenu)
        self.mu.draw(self.equationForceMenu)
        self.mu2.draw(self.equationForceMenu)

        self.forceNet.connect("click", self.showNetForceBaseMenu)
        self.forceNormal.connect("click", self.showNormalForceBaseMenu)
        self.forceApplied.connect("click", self.showAppliedForceBaseMenu)
        self.forceFriction.connect("click", self.showFrictionForceBaseMenu)
        self.forcePlanetary.connect("click", self.showPlanetaryForceBaseMenu)
        self.forceMass.connect("click", self.showMassForceBaseMenu)
        self.forceAcceleration.connect("click", self.showAccelerationForceBaseMenu)
        self.mu.connect("click", self.showmuBaseMenu)
        self.mu2.connect("click", self.showmu2BaseMenu)
        
    def showNetForceBaseMenu(self, o, e):
        showNetForceBaseMenu = ShowNetForceBaseMenu()
    def showNormalForceBaseMenu(self, o, e):
        showNormalForceBaseMenu = ShowNormalForceMenu()
    def showAppliedForceBaseMenu(self, o, e):
        showAppliedForceBaseMenu = ShowAppliedForceBaseMenu()
    def showFrictionForceBaseMenu(self, o, e):
        showFrictionForceBaseMenu = ShowFrictionForceMenu()
    def showPlanetaryForceBaseMenu(self, o, e):
        showPlanetaryForceBaseMenu = ShowPlanetaryForceBaseMenu()
    def showMassForceBaseMenu(self, o, e):
        showMassForceBaseMenu = ShowMassForceBaseMenu()
    def showAccelerationForceBaseMenu(self, o , e):
        showAccelerationForceBaseMenu = ShowAccelerationForceBaseMenu()
    def showmuBaseMenu(self, o, e):
        showmuBaseMenu = ShowmuBaseMenu()
    def showmu2BaseMenu(self, o, e):
        showmu2BaseMenu = Showmu2BaseMenu()
class ShowMomentumBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.momentum = Button((50, 50), "Momentum")
        self.impulseFirst = Button((50, 70), "Impulse with Change in Momentum")
        self.impulseSecond = Button((50, 90), "Impulse with Force and Change in Time")
        self.impulseThird = Button((50, 110), "Impulse with Mass and Change in Velocity")
        self.conservationOfMomentum = Button((50, 130), "Conservation Of Momentum")
        self.hitAndSeperate = Button((50, 150), "Hit and Seperate")
        self.hitAndStick = Button((50, 170), "Hit and Stick")

        self.equationMomentumMenu = Window("Solve Momentum Equation", 400, 300)
        self.momentum.draw(self.equationMomentumMenu)
        self.impulseFirst.draw(self.equationMomentumMenu)
        self.impulseSecond.draw(self.equationMomentumMenu)
        self.impulseThird.draw(self.equationMomentumMenu)
        self.conservationOfMomentum.draw(self.equationMomentumMenu)
        self.hitAndSeperate.draw(self.equationMomentumMenu)
        self.hitAndStick.draw(self.equationMomentumMenu)
        
        self.momentum.connect("click", self.showMomentumMenu)
        self.impulseFirst.connect("click", self.showImpulseFirstMenu)
        self.impulseSecond.connect("click", self.showImpulseSecondBaseMenu)
        self.impulseThird.connect("click", self.showImpulseThirdBaseMenu)
        self.conservationOfMomentum.connect("click", self.showConservationOfMomentumBaseMenu)
        self.hitAndSeperate.connect("click", self.showHitAndSeperateMenu)
        self.hitAndStick.connect("click", self.showHitAndStickBaseMenu)
        
    def showMomentumMenu(self, o, e):
        momentumMenu = ShowMomentumMenu()
    def showImpulseFirstMenu(self, o, e):
        showImpulseFirstMenu = ShowImpulseFirstMenu()
    def showImpulseSecondBaseMenu(self, o, e):
        showImpulseSecondMenu = ShowImpulseSecondMenu()
    def showImpulseThirdBaseMenu(self, o, e):
        showImpulseThirdMenu = ShowImpulseThirdMenu()
    def showConservationOfMomentumBaseMenu(self, o, e):
        conservationOfMomentumBaseMenu = ShowConservationOfMomentumBaseMenu()
    def showHitAndSeperateMenu(self, o, e):
        showHitAndSeperateMenu = ShowHitAndSeperateMenu()
    def showHitAndStickBaseMenu(self, o, e):
        HitAndStickMenu = ShowHitAndStickBaseMenu()


class ShowMotionBaseMenu(object):
## <<<<<<< HEAD
    def __init__(self):
        #Motion Menu Buttons
        self.distanceTravelled = Button((50, 50), "Distance Travelled")
        self.distanceTravelledWithAcceleration = Button((50, 70), "Distance Travelled with Acceleration")
        self.newVelocityWithTime = Button((50, 90), "New velocity with time")
        self.newVelocityWithDistanceTravelled = Button((50, 110), "New Velocity with distance travelled")
        self.velocityFromDistance = Button((50, 130), "Velcotiy from Distance")
        self.accelerationFromVelocity = Button((50, 150), "Acceleration from Velocity")
        self.velocityFromAcceleration = Button((50, 170), "Velocity from Acceleration")
        self.distanceFromVelocity = Button((50, 190), "Distance from Velocity")
        self.maxRange = Button((50, 210), "Max Range")
        self.maxHeight = Button((50, 230), "Max Height")
        self.motionYVectors = Button((50, 250), "Motion y vectors")
        self.deltaMotionYVectors = Button((50, 270), "Change in Motion y vectors")
        self.motionXVectors = Button((50, 290), "Motion x vectors")
        self.deltaMotionXVectors = Button((50, 310), "Change in Motion x vectors")
        self.accelerationNoX = Button((50,330), "Acceleration with out distance")
        self.accelerationNoV2 = Button((50,350), "Accelerattion with out final velocity")

        self.equationMotionMenu = Window("Solve Motion Equation", 400, 400)
        self.distanceTravelled.draw(self.equationMotionMenu)
        self.distanceTravelledWithAcceleration.draw(self.equationMotionMenu)
        self.newVelocityWithTime.draw(self.equationMotionMenu)
        self.newVelocityWithDistanceTravelled.draw(self.equationMotionMenu)
        self.velocityFromDistance.draw(self.equationMotionMenu)
        self.accelerationFromVelocity.draw(self.equationMotionMenu)
        self.velocityFromAcceleration.draw(self.equationMotionMenu)
        self.distanceFromVelocity.draw(self.equationMotionMenu)
        self.maxRange.draw(self.equationMotionMenu)
        self.maxHeight.draw(self.equationMotionMenu)
        self.motionYVectors.draw(self.equationMotionMenu)
        self.deltaMotionYVectors.draw(self.equationMotionMenu)
        self.motionXVectors.draw(self.equationMotionMenu)
        self.deltaMotionXVectors.draw(self.equationMotionMenu)
        self.accelerationNoX.draw(self.equationMotionMenu)
        self.accelerationNoV2.draw(self.equationMotionMenu)

        self.distanceTravelled.connect("click", self.showDistanceTravelledBaseMenu)
        self.distanceTravelledWithAcceleration.connect("click", self.showDistanceTravelledWithAccelerationMenu)
        self.newVelocityWithTime.connect("click", self.showNewVelocityWithTimeBaseMenu)
        self.newVelocityWithDistanceTravelled.connect("click", self.showNewVelocityWithDistanceTravelledMenu)
        self.velocityFromDistance.connect("click", self.showVelocityFromDistanceBaseMenu)
        self.accelerationFromVelocity.connect("click", self.showAccelerationFromVelocityMenu)
        self.velocityFromAcceleration.connect("click", self.showVelocityFromAccelerationBaseMenu) 
        self.distanceFromVelocity.connect("click", self.showDistanceFromVelocityBaseMenu)
        self.maxRange.connect("click", self.showMaxRangeBaseMenu)
        self.maxHeight.connect("click", self.showMaxHeightBaseMenu)
        self.motionYVectors.connect("click", self.showMotionYVectorsBaseMenu)
        self.deltaMotionYVectors.connect("click", self.showDeltaMotionYVectorsBaseMenu)
        self.motionXVectors.connect("click", self.showMotionXVectorsBaseMenu)
        self.deltaMotionXVectors.connect("click", self.showDeltaMotionXVectorsBaseMenu)
        self.accelerationNoX.connect("click", self.showAccelerationNoXBaseMenu)
        self.accelerationNoV2.connect("click", self.showAccelerationNoV2BaseMenu)
            
    def showDistanceTravelledBaseMenu(self, o, e):
        distanceTravelledBaseMenu = ShowDistanceTravelledBaseMenu()
    def showDistanceTravelledWithAccelerationMenu(self, o, e):
        distanceTravelledWithAccelerationMenu = ShowDistanceTravelledWithAccelerationMenu()
    def showNewVelocityWithTimeBaseMenu(self, o, e):
        newVelocityWithTimeBaseMenu = ShowNewVelocityWithTimeMomentumBaseMenu()
    def showNewVelocityWithDistanceTravelledMenu(self, o, e):
        newVelocityWithDistanceTravelledEnergyMenu = ShowNewVelocityWithDistanceTravelledEnergyMenu()
    def showVelocityFromDistanceBaseMenu(self, o, e):
        velocityFromDistanceBaseMenu = ShowVelocityFromDistanceBaseMenu()
    def showAccelerationFromVelocityMenu(self, o, e):
        accelerationFromVelocityMenu = ShowAccelerationFromVelocityMenu()
    def showVelocityFromAccelerationBaseMenu(self, o, e):
        velocityFromAccelerationMenu = ShowVelocityFromAccelerationBaseMenu()
    def showDistanceFromVelocityBaseMenu(self, o, e):
        distanceFromVelocityBaseMenu = ShowDistanceFromVelocityBaseMenu()
    def showMaxRangeBaseMenu(self, o, e):
        maxRangeBaseMenu = ShowMaxRangeBaseMenu()
    def showMaxHeightBaseMenu(self, o, e):
        maxHeightBaseMenu = ShowMaxHeightBaseMenu()
    def showMotionYVectorsBaseMenu(self, o, e):
        motionYVectorsBaseMenu = ShowMotionYVectorsBaseMenu()
    def showDeltaMotionYVectorsBaseMenu(self, o, e):
        deltaMotionYVectorsBaseMenu = ShowDeltaMotionYVectorsBaseMenu()
    def showMotionXVectorsBaseMenu(self, o, e):
        motionXVectorsBaseMenu = ShowMotionXVectorsBaseMenu()
    def showDeltaMotionXVectorsBaseMenu(self, o, e):
        deltaMotionXVectorsBaseMenu = ShowDeltaMotionXVectorsBaseMenu()
    def showAccelerationNoXBaseMenu(self, o, e):
        accelertaionNoXBaseMenu = ShowAccelerationNoXBaseMenu()
    def showAccelerationNoV2BaseMenu(self, o, e):
        accelerationNoV2BaseMenu = ShowAccelerationNoV2BaseMenu()

class ShowEnergyBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.kineticEnergy = Button((50, 50), "Kinetic Energy")
        self.gravitationalPotentialEnergy = Button((50, 70), "Gravitational Potential Energy")
        self.springPotentialEnergy = Button((50, 90), "Spring Potential Energy")
        
        self.equationEnergyMenu = Window("Solve Energy Equation", 400, 300)
        
        self.kineticEnergy.draw(self.equationEnergyMenu)
        self.gravitationalPotentialEnergy.draw(self.equationEnergyMenu)
        self.springPotentialEnergy.draw(self.equationEnergyMenu)
        
        self.kineticEnergy.connect("click", self.showKineticEnergyBaseMenu)
        self.gravitationalPotentialEnergy.connect("click", self.showGravitationalPotentialEnergyMenu)
        self.springPotentialEnergy.connect("click", self.showSpringPotentialEnergyBaseMenu)
        
        ##To be added after each of the next screens are made
    def showKineticEnergyBaseMenu(self, o, e):
        kineticEnergyBaseMenu = ShowKineticEnergyBaseMenu()
    def showGravitationalPotentialEnergyMenu(self, o, e):
        gravitationalPotentialEnergyMenu = ShowGravitationalPotentialEnergyMenu()
    def showSpringPotentialEnergyBaseMenu(self, o, e):
        springPotentialEnergyBaseMenu = ShowSpringPotentialEnergyBaseMenu()

class ShowWorkBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.work = Button((50, 50), "Work")
        self.CalcWork = Button((50,70), "Calculus Work")
        self.power = Button((50,90), "Power")

        self.equationWorkMenu = Window("Solve Work Equation", 400, 300)
        self.work.draw(self.equationWorkMenu)
        self.CalcWork.draw(self.equationWorkMenu)
        self.power.draw(self.equationWorkMenu)

        self.work.connect("click", self.showWorkMenu)
        self.CalcWork.connect("click", self.showCalcWorkBaseMenu)
        self.power.connect("click", self.showPowerBaseMenu)
        
    def showWorkMenu(self, o, e):
        workMenu = ShowWorkMenu()
    def showCalcWorkBaseMenu(self, o, e):
        CalcWorkBaseMenu = showCalcWorkBaseMenu()
    def showPowerBaseMenu(self,o,e):
        PowerBaseMenu = showPowerBaseMenu()
class ShowPlanetaryForceBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.force = Button((50, 50), "Force")
        self.gravity = Button((50, 70), "Gravity")
        self.keplersConstant = Button((50, 90), "Keplers Constant")

        self.equationPlanetaryForceMenu = Window("Solve Planetary Force Equation", 400, 300)
        self.force.draw(self.equationPlanetaryForceMenu)
        self.gravity.draw(self.equationPlanetaryForceMenu)
        self.keplersConstant.draw(self.equationPlanetaryForceMenu)
        self.force.connect("click", self.showPlanetaryForce)
        self.gravity.connect("click", self.showPlanetaryGravity)
        self.keplersConstant.connect("click", self.showKeplersConstant)

    def showPlanetaryForce(self, o, e):
        planetaryForceMenu = ShowPlanetaryForceMenu()
    def showPlanetaryGravity(self, o, e):
        planetaryGravityMenu = ShowPlanetaryGravityMenu()
    def showKeplersConstant(self, o, e):
        keplersConstant = ShowKeplersConstantMenu()
class ShowCenterOfMassBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.centerOfMass = Button((50, 50), "Center Of Mass")

        self.equationMomentumMenu = Window("Solve Center Of Mass Equation", 400, 300)
        self.centerOfMass.draw(self.equationMomentumMenu)
   
        self.centerOfMass.connect("click", self.showCenterOfMass)
        
    def showCenterOfMass(self, o, e):
        centerOfMass = ShowCenterOfMass()

class ShowCircularMotionBaseMenu(object):
    def __init__(self):
        #Momentum Menu Buttons
        self.acceleration = Button((50, 50), "Acceleration")
        self.verticalCircleVelocity = Button((50, 70), "Vertical Circle Velocity")
        self.horizontalCircleVelocity = Button((50, 90), "Horizontal Circle Velocity")
        self.force = Button((50, 110), "Force")
        
        self.equationCircularMotionMenu = Window("Solve CircularMotion Equation", 400, 300)
        
        self.acceleration.draw(self.equationCircularMotionMenu)
        self.verticalCircleVelocity.draw(self.equationCircularMotionMenu)
        self.horizontalCircleVelocity.draw(self.equationCircularMotionMenu)
        self.force.draw(self.equationCircularMotionMenu)

        self.acceleration.connect("click", self.showAccelerationBaseMenu)
        self.verticalCircleVelocity.connect("click", self.showVerticalCircleVelocityMenu)
        self.horizontalCircleVelocity.connect("click", self.showHorizontalCircleVelocityBaseMenu)
        self.force.connect("click", self.showForceMenu)

    def showAccelerationBaseMenu(self, o, e):
        showAccelerationBaseMenu = ShowAccelerationBaseMenu()
    def showVerticalCircleVelocityMenu(self, o, e):
        verticalCircleVelocityBaseMenu = ShowVerticalCircleVelocityMenu()
    def showHorizontalCircleVelocityBaseMenu(self, o, e):
        horizontalCircleVelocityBaseMenu = ShowHorizontalCircleVelocityBaseMenu()
    def showForceMenu(self, o, e):
        forceMenu = ShowForceMenu()


class ShowAccelerationForceBaseMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowmuBaseMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class Showmu2BaseMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class showPowerBaseMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class showCalcWorkBaseMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowPlanetaryForceMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowPlanetaryGravityMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowKeplersConstantMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowNetForceBaseMenu(object):
   def __init__(self):  
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowNormalForceMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowAppliedForceBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowFrictionForceMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
## class ShowPlanetaryForceBaseMenu(object):
##    def __init__(self):
##        self.inputWindow = Window("Input Window", 400, 300)
##        self.textBox = input()
##        self.textbox.draw(self.inputWindow)
class ShowMomentumMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowImpulseFirstMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowImpulseSecondMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowImpulseThirdMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowConservationOfMomentumBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowHitAndSeperateMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowHitAndStickBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowDistanceTravelledBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowDistanceTravelledWithAccelerationMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowNewVelocityWithTimeBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowNewVelocityWithDistanceTravelledMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowVelocityFromDistanceBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowAccelerationFromVelocityMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowVelocityFromAccelerationBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowDistanceFromVelocityBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowMaxRangeBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowMaxHeightBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowMotionYVectorsBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowDeltaMotionYVectorsBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowMotionXVectorsBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowDeltaMotionXVectorsBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowKineticEnergyBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowGravitationalPotentialEnergyMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowSpringPotentialEnergyBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowWorkMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowCenterOfMass(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowAccelerationBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowVerticalCircleVelocityMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowHorizontalCircleVelocityBaseMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
class ShowForceMenu(object):
   def __init__(self):
       self.inputWindow = Window("Input Window", 400, 300)
       self.textBox = input()
       self.textbox.draw(self.inputWindow)
  
#Base Menu Buttons
baseMenu = BaseMenu()
