from Graphics import *
from sympy import *
#import force

x, y, z = symbols('x y z')
init_printing(use_unicode=True)


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
        self.work = Button((50, 130), "Planetary Force")
        self.centerOfMass = Button((50, 150), "Center Of Mass")
        self.circularMotion = Button((50, 170), "Circular Motion")
        
        self.equationBaseMenu = Window("Solve Equation", 200, 200)
        self.force.draw(self.equationBaseMenu)
        self.motion.draw(self.equationBaseMenu)
        self.momentumButton.draw(self.equationBaseMenu)
        self.energy.draw(self.equationBaseMenu)
        self.work.draw(self.equationBaseMenu)
        self.centerOfMass.draw(self.equationBaseMenu)
        self.circularMotion.draw(self.equationBaseMenu)
        
        self.force.connect("click", self.showForceBaseMenu)
        self.motion.connect("click", self.showMotionBaseMenu)
        self.momentumButton.connect("click", self.showMomentumBaseMenu)
        self.energy.connect("click", self.showEnergyBaseMenu)
        self.work.connect("click", self.showWorkBaseMenu)
        self.centerOfMass.connect("click", self.showCenterOfMassBaseMenu)
        self.circularMotion.connect("click", self.showCircularMotionBaseMenu)
        
        def showForceBaseMenu(self, o, e):
            forceBaseMenu = ShowForceBaseMenu()
        def showMotionMenu(self, o, e):
            showMotionMenu = ShowMotionMenu()
        def showMomentumBaseMenu(self, o, e):
            momentumBaseMenu = ShowMomentumBaseMenu()
        def showEnergyMenu(self, o, e):
            showEnergyMenu = ShowEnergyMenu()
        def showWorkBaseMenu(self, o, e):
            workBaseMenu = ShowWorkBaseMenu()
        def showCenterOfMassMenu(self, o, e):
            showCenterOfMassMenu = ShowCenterOfMassMenu()
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
       
        self.equationForceMenu = Window("Solve Force Equation", 200, 200)
        self.forceNet.draw(self.equationForceMenu)
        self.forceNormal.draw(self.equationForceMenu)
        self.forceApplied.draw(self.equationForceMenu)
        self.forceFriction.draw(self.equationForceMenu)
        self.forcePlanetary.draw(self.equationForceMenu)

        def showNetForceBaseMenu(self, o, e):
            netForceBaseMenu = ShowNetForceBaseMenu()
        def showNormalForceMenu(self, o, e):
            showNormalForceMenu = ShowNormalForceMenu()
        def showAppliedForceBaseMenu(self, o, e):
            appliedForceBaseMenu = ShowAppliedForceBaseMenu()
        def showFrictionForceBaseMenu(self, o, e):
            showFrictionForceMenu = ShowFrictionForceMenu()
        def showPlanetaryForceBaseMenu(self, o, e):
            workPlanetaryForceBaseMenu = ShowPlanetaryForceBaseMenu()

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
        def showMomentumBaseMenu(self, o, e):
            momentumBaseMenu = ShowMomentumBaseMenu()
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
        def __init__(self):
            #Motion Menu Buttons
            self.distanceTravelled = Button((50, 50), "Distance Travelled")
            self.distanceTravelledWithAcceleration = Button((50, 70), "Distance Travelled with Acceleration")
            self.newVelocityWithTime = Button((50, 90), "New velocity with time")
            self.newVelocityWithDistanceTravelled = Button((50, 110), "New Velocity with distance travelled")
            self.velocityFromDistance = Button((50, 130), "Velcotiy from Distance")
            self.accelerationFromVelocity = Button((50, 150), "Acceleration from Velocity")
            self.velocityFromAcceleration = Button((50, 170), "Velocity from Acceleration")
            self.distanceFromVelocity = Button((50, 50), "Distance from Velocity")
            self.maxRange = Button((50, 70), "Max Range")
            self.maxHeight = Button((50, 90), "Max Height")
            self.motionYVectors = Button((50, 110), "Motion y vectors")
            self.deltaMotionYVectors = Button((50, 130), "Change in Motion y vectors")
            self.motionXVectors = Button((50, 150), "Motion x vectors")
            self.deltaMotionXVectors = Button((50, 170), "Change in Motion x vectors")
    
            self.equationMotionMenu = Window("Solve Motion Equation", 400, 300)
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
            
            ##To be added after each of the next screens are made
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

class ShowEnergyBaseMenu(object):
   def __init__(self):
        #Momentum Menu Buttons
        self.kineticEnergy = Button((50, 50), "Kinetic Energy")
        self.gravitationalPotentialEnergy = Button((50, 70), "Gravitational Potential Energy")
        self.springPotentialEnergy = Button((50, 90), "Spring Potential Energy")
        
        self.equationEnergyMenu = Window("Solve Energy Equation", 400, 300)
        self.kineticEnergy.draw(self.equationMomentumMenu)
        self.gravitationalPotentialEnergy.draw(self.equationMomentumMenu)
        self.springPotentialEnergy.draw(self.equationMomentumMenu)
        
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

        self.equationWorkMenu = Window("Solve Work Equation", 400, 300)
        self.work.draw(self.equationMomentumMenu)
        
        def showWorkBaseMenu(self, o, e):
            workBaseMenu = ShowWorkBaseMenu()

class ShowCenterOfMassBaseMenu(object):
   def __init__(self):
        #Momentum Menu Buttons
        self.centerOfMass = Button((50, 50), "Center Of Mass")

        self.equationMomentumMenu = Window("Solve Center Of Mass Equation", 400, 300)
        self.centerOfMass.draw(self.equationMomentumMenu)
        
        def showCenterOfMassBaseMenu(self, o, e):
            centerOfMassBaseMenu = ShowCenterOfMassBaseMenu()

class ShowCircularMotionBaseMenu(object):
   def __init__(self):
        #Momentum Menu Buttons
        self.acceleration = Button((50, 50), "Acceleration")
        self.verticalCircleVelocity = Button((50, 70), "Vertical Circle Velocity")
        self.horizontalCircleVelocity = Button((50, 90), "Horizontal Circle Velocity")
        self.force = Button((50, 110), "Force")
        
        self.equationCircularMotionMenu = Window("Solve CircularMotion Equation", 400, 300)
        self.acceleration.draw(self.equationMomentumMenu)
        self.verticalCircleVelocity.draw(self.equationMomentumMenu)
        self.horizontalVerticalVelocity.draw(self.equationMomentumMenu)
        self.force.draw(self.equationMomentumMenu)

        def showAccelerationBaseMenu(self, o, e):
            accelerationBaseMenu = ShowAccelerationBaseMenu()
        def showVerticalCircleVelocityMenu(self, o, e):
            verticalCircleVelocityBaseMenu = ShowVerticalCircleVelocityMenu()
        def showHorizontalCircleVelocityBaseMenu(self, o, e):
            horizontalCircleVelocityBaseMenu = ShowHorizontalCircleVelocityBaseMenu()
        def showForceMenu(self, o, e):
            forceMenu = ShowForceMenu()
  
#Base Menu Buttons
baseMenu = BaseMenu()
