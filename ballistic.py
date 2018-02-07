# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 14:39:12 2018

@author: John Doe
"""
import math as ma
import numpy as np
import scipy as sc
import scipy.constants
import matplotlib as mpl
import matplotlib.pyplot as plt

earthmass=5.972e24 #kg
earthrad=6.371e6 #meters
univgrav=raw_input("Please input the Universal Gravitational Constant. (The code will use this if you leave this prompt blank: 6.67408x10^-11 m^3 kg^-1 s^-2): ")
initvel=float(raw_input("Please input the initial velocity of your projectile in m/s: "))
initangle=float(raw_input("Please input the angle at which the projectile is launched, in degrees (-90 to 90): "))
initheight=float(raw_input("Please input the initial height from which the projectile is launched: "))
timestep=float(raw_input("Please choose a timestep to simulate in seconds (Don't include units): "))
if univgrav=="":
    univgrav= scipy.constants.gravitational_constant #Automatically uses this if nothing is inputted
else:
    univgrav=float(univgrav)
initrad=initangle*ma.pi/180 #angle in radians

def accel(gravconstant,height,earthmass,earthrad):
    accel=-univgrav*earthmass/((earthrad+height)**2)
    return accel
    
"""
-----------------------
This is a version WITH arrays.
-----------------------
"""

velx=initvel*ma.cos(initrad) #Initial x velocity
vely=initvel*ma.sin(initrad) #Initial y velocity
velocitylisty=[vely] #starting a velocity list
positionlistx=[0] #starting a position list in x
heightlist=[initheight] #starting a position list in y
#Make array that is curh and vely as a single variable


timelist=[0]
t=0
pos=0 #x position variable
curh=initheight #Setting the current height value

while round(curh,6)>=0:
    #-------------------------------------
    
    typer="Explicit Euler Method"
    accy=accel(univgrav,curh,earthmass,earthrad)
    zmat=np.array([curh,vely])
    zmatprime=np.array([vely,accy])
    zmat=zmat+timestep*zmatprime
    timelist.append(t*timestep)
    
    #-------------------------------------
    #Runge-Kutta 2 method, seems to work
    """
    typer="Runge-Kutta 2nd order"
    accy=accel(univgrav,curh,earthmass,earthrad)
    zmat=np.array([curh,vely])
    zmatprime=np.array([vely,accy])
    k1=timestep*(np.array([zmat[1],accy]))
    k2=timestep*(np.array([zmat[1]+(1/2.0)*k1[0],zmatprime[1]+(1/2.0)*k1[1]]))
    zmat=zmat+k2
    timelist.append(t*timestep)
    """
    
    #-------------------------------------
    """#Not accurate currently?
    typer="Runge-Kutta 4th order"
    accy=accel(univgrav,curh,earthmass,earthrad)
    zmat=np.array([curh,vely])
    zmatprime=np.array([vely,accy])
    fourk1=timestep*zmatprime
    
    kstar=zmat+timestep*zmatprime
    knew=kstar+fourk1
    fourk2=timestep*(np.array([knew[1],accel(univgrav,knew[0],earthmass,earthrad)]))
    
    knewer=kstar+(1/2.0)*fourk2
    fourk3=timestep*(np.array([knewer[1],accel(univgrav,knewer[0],earthmass,earthrad)]))
    
    kstar4=zmat+timestep*zmatprime
    knewest=kstar+fourk3
    fourk4=timestep*(np.array([knewest[1],accel(univgrav,knewest[0],earthmass,earthrad)]))
    zmat=zmat+(1/6.0)*fourk1+(1/3.0)*fourk2+(1/3.0)*fourk3+(1/6.0)*fourk4
    timelist.append(t*timestep)
    """
    
    """#Rewrite of RK4 function. . .is it accurate?
    typer="Runge-Kutta 4th order"
    accy=accel(univgrav,curh,earthmass,earthrad)
    zmat=np.array([curh,vely])
    zmatprime=np.array([vely,accy])
    k1=timestep*(np.array([zmat[1],accy]))
    k2=timestep*(np.array([zmat[1]+(1/2.0)*k1[0],zmatprime[1]+(1/2.0)*k1[1]]))
    k3=timestep*(np.array([zmat[1]+(1/2.0)*k2[0],zmatprime[1]+(1/2.0)*k2[1]]))
    k4=timestep*(np.array([zmat[1]+k3[0],zmatprime[1]+k3[1]]))
    zmat=zmat+(1/6.0)*k1+(1/3.0)*k2+(1/3.0)*k3+(1/6.0)*k4
    timelist.append(t*timestep)
    """
    #----------------------------------
    velocitylisty.append(zmat[1])
    heightlist.append(zmat[0])
    curh=heightlist[-1]
    vely=velocitylisty[-1]
    pos=pos+timestep*velx #This part is less likely to have error problems since it's linear, so I'm sticking with just an Explicit Euler method.
    positionlistx.append(pos)
    t=t+1
    
    
    

highest=max(heightlist)
q=heightlist.index(highest)
print("The highest point the projectile reaches is "+str(highest)+" meters.")
print("The projectile reaches this point at t= "+str(timelist[q])+" seconds.")
print("The flight time is "+str(timelist[-1])+" seconds.")
plt.plot(positionlistx,heightlist)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
print(typer)

    
    
    
    
    
    
    
    
    
    
    
    
    
















