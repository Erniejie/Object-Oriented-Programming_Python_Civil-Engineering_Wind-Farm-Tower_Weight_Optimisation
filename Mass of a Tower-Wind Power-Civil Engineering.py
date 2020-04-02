
### WIND POWER- MASS OF A TOWER- ENERGY-CIVIL CIVIL ENGINEERING
### Based on the Proceeding of the Institution of Civil Engineers_ Vol. 158_Issue 6_Year 2005: Wind Power : A Major Opportunity for the UK
### The Tower is Generally a Tapering Hollow Tubular  Steel Section

import math
class WindTurbineTowerMass():
    ### CONNECTOR:

    def __init__(self,Height,TopDiameter,ShapeFactor,HollowTubeThickness,TowerDensity):
        self.Height = Height                                ### "L" Lenght of Tower in [m]
        self.TopDiameter =TopDiameter                       #### "d_a" Diameter at the top od Tower in [m]
        self.ShapeFactor = ShapeFactor                      #### Shape Factor "m": a real number
        self.HollowTubeThickness = HollowTubeThickness      ### Thickness of Hollow Tube "t",uniform in [m]
        self.TowerDensity = TowerDensity                    #### Density of the Tower in [ kg/m^3 ]

    #### METHODOLOGY:

    def WindTurbineTowerBaseDiameter(self):
        return self.ShapeFactor*self.TopDiameter

    def MassOfWindPowerTower(self):
        return (math.pi)*self.TowerDensity*self.HollowTubeThickness*self.Height*self.ShapeFactor*self.TopDiameter*(self.ShapeFactor +1)/((2)*self.ShapeFactor)

    ##### OUTPUT

x = WindTurbineTowerMass(10,0.6,2.3,0.2,7850,)

x.Height = 10
x.TopDiameter = 0.6
x.ShapeFactor = 2.3

print(x.WindTurbineTowerBaseDiameter())            ######  Ouput Units in [Meters]
print(round(x.MassOfWindPowerTower(),4))           #####  Output Units in [Kg]






