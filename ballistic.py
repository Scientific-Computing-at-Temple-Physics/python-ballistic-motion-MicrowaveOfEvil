# -*- coding: utf-8 -*-
"""
Created on Thu Feb 01 14:39:12 2018

@author: John Doe
"""
import math as ma
earthmass=5.972e24 #kg
earthrad=6.371e6 #meters
univgrav=raw_input("Please input the Universal Gravitational Constant. (The code will use this if you leave this prompt blank: 6.67408x10^-11 m^3 kg^-1 s^-2): ")
initvel=float(raw_input("Please input the initial velocity of your projectile in m/s: "))
initangle=float(raw_input("Please input the angle at which the projectile is launched, in degrees (-90 to 90): "))
initheight=float(raw_input("Please input the initial height from which the projectile is launched: "))
timestep=float(raw_input("Please choose a timestep to simulate in seconds (Don't include units): "))
if univgrav=="":
    univgrav=6.67408e-11#Automatically uses this if nothing is inputted
else:
    univgrav=float(univgrav)
initrad=initangle*ma.pi/180 #angle in radians

def accel(gravconstant,height,earthmass,earthrad):
    accel=-univgrav*earthmass/((earthrad+height)**2)
    return accel
    
"""
-----------------------
This is a version without using arrays.
-----------------------
"""
velx=initvel*ma.cos(initrad)
vely=initvel*ma.sin(initrad)
velocitylisty=[vely]
positionlistx=[0]
heightlist=[initheight]
timelist=[0]
t=1
pos=0 #x position variable
curh=initheight #Setting the current height value

while curh>0:
    #-------------------------------------
    
    typer="Explicit Euler Method"
    curh=curh+timestep*vely
    vely=vely+timestep*accel(univgrav,curh,earthmass,earthrad)
    timelist.append(t*timestep)
    
    #-------------------------------------
    """#Inaccurate currently?
    typer="Runge-Kutta 2nd order"
    acc=accel(univgrav,curh,earthmass,earthrad)
    zstar1=curh+timestep*(1/2.0)*vely
    zstar2=vely+timestep*(1/2.0)*acc
    ztwo1=timestep*vely
    ztwo2=timestep*acc
    znew1=zstar1+(1/2.0)*ztwo1
    znew2=zstar2+(1/2.0)*ztwo2
    k21=timestep*znew2
    k22=timestep*accel(univgrav,znew1,earthmass,earthrad)
    curh=curh+k21
    vely=vely+k22
    timelist.append(t*timestep)
    """
    #-------------------------------------
    """#Not accurate currently?
    typer="Runge-Kutta 4th order" #This looks a lot nicer with arrays, alright?
    acc4=accel(univgrav,curh,earthmass,earthrad)
    fourk11=timestep*vely
    fourk12=timestep*acc4
    
    kstar1=curh+timestep*vely
    kstar2=vely+timestep*acc4
    knew1=kstar1+fourk11
    knew2=kstar2+fourk12
    fourk21=timestep*knew2
    fourk22=timestep*accel(univgrav,knew1,earthmass,earthrad)
    
    knewer1=kstar1+(1/2.0)*fourk21
    knewer2=kstar2+(1/2.0)*fourk22
    fourk31=timestep*knewer2
    fourk32=timestep*accel(univgrav,knewer1,earthmass,earthrad)
    
    kstar41=curh+timestep*vely
    kstar42=vely+timestep*acc4
    knewest1=kstar41+fourk31
    knewest2=kstar42+fourk32
    fourk41=timestep*knewest2
    fourk42=timestep*accel(univgrav,knewest1,earthmass,earthrad)
    curh=curh+(1/6.0)*fourk11+(1/3.0)*fourk21+(1/3.0)*fourk31+(1/6.0)*fourk41
    vely=vely+(1/6.0)*fourk12+(1/3.0)*fourk22+(1/3.0)*fourk32+(1/6.0)*fourk42
    timelist.append(t*timestep)
    """
    #----------------------------------
    velocitylisty.append(vely)
    pos=pos+timestep*velx #This part is less likely to have error problems since it's linear, so I'm sticking with just an Explicit Euler method.
    positionlistx.append(pos)
    heightlist.append(curh)
    t=t+1
    
    
    

highest=max(heightlist)
q=heightlist.index(highest)
print("The highest point the projectile reaches is "+str(highest)+" meters.")
print("The projectile reaches this point at t= "+str(timelist[q])+" seconds.")
print("The flight time is "+str(timelist[-1])+" seconds.")
#print(typer)

    
    
    
    
    
    
    
    
    
    
    
    
    
















