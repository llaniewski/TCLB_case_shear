from __future__ import division
#import the appropriate ESyS-Particle modules:
from esys.lsm import *
from esys.lsm.util import *

class WallLoaderRunnable (Runnable):
    def __init__ (self,
        LsmMpi=None,
        wallName=None,
        vPlate=Vec3(0,0,0),
        startTime=0,
        rampTime = 200):
        """
            Subroutine to initialise the Runnable and store parameter values.
        """
        Runnable.__init__(self)
        self.sim = LsmMpi
        self.wallName = wallName
        self.Vplate = vPlate
        self.dt = self.sim.getTimeStepSize()
        self.rampTime = rampTime
        self.startTime = startTime
        self.Nt = 0
    def run (self):
        """
        Subroutine to move the specified wall. After self.startTime
        timesteps, the speed of the wall increases linearly over
        self.rampTime timesteps until the desired wall speed is achieved.
        Thereafter the wall is moved at that speed.
        """
        if (self.Nt >= self.startTime):
            #compute the slowdown factor if still accelerating the wall:
            if (self.Nt < (self.startTime + self.rampTime)):
                f = float(self.Nt - self.startTime) / float(self.rampTime)
            else:
                f = 1.0
            #compute the amount by which to move the wall this timestep:
            Dplate = Vec3(
                f*self.Vplate[0]*self.dt,
                f*self.Vplate[1]*self.dt,
                f*self.Vplate[2]*self.dt
            )
            #instruct the simulation to move the wall:
            self.sim.moveWallBy (self.wallName, Dplate)
        #count the number of timesteps completed thus far:
        self.Nt += 1


class ServoWallLoaderRunnable (Runnable):
    def __init__ (self,
        LsmMpi=None,
        interactionName=None,
        force=Vec3(0,0,0),
        startTime=0,
        rampTime = 200
    ):
        """
        Subroutine to initialise the Runnable and store parameter values.
        """
        Runnable.__init__(self)
        self.sim = LsmMpi
        self.interactionName = interactionName
        self.force = force
        self.dt = self.sim.getTimeStepSize()
        self.rampTime = rampTime
        self.startTime = startTime
        self.Nt = 0
    def run (self):
        """
        Subroutine to apply the force to a wall interaction. After self.startTime
        timesteps, the force on the wall increases linearly over
        self.rampTime timesteps until the desired wall force is achieved.
        Thereafter the wall force is kept fixed.
        """
        if (self.Nt > self.startTime):
            #compute the slowdown factor if still accelerating the wall:
            if (self.Nt < (self.startTime + self.rampTime)):
                f = float(self.Nt - self.startTime) / float(self.rampTime)
            else:
                f = 1.0
            #compute the amount by which to move the wall this timestep:
            Dforce = Vec3(
                f*self.force[0],
                f*self.force[1],
                f*self.force[2]
            )
            #instruct the simulation to apply the prescribed force to the wall:
            self.sim.applyForceToWall (self.interactionName, Dforce)
        self.Nt += 1