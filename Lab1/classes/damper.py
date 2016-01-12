#!/usr/bin/python3

# http://web.engr.oregonstate.edu/~smartw/me499/labs/lab1/
# mx.. = -kx + cx.
# where m is the mass in kg, 
# k is the spring constant in newtons per meter, 
# and c is the damping coefficient in kg per second. 
# x = position, x_dot=velocity, x_dotdot = accelleration
# Write a function to calculate the current acceleration, given m, k, c, x, x_dot.

class Damper(object):
    def __init__(self,  m=1.0, k=1.0, c=1.0):
        self.m = m
        self.k=k
        self.c = c


    def getAcceleration(self):
        return ((-1 * self.x * self.k) + (-1* self.x_dot * self.c)) / self.m


    def damp(self, x=1.0, x_dot=0.0,  t=0.01, epoch=1000):
        self.x = x
        self.x_dot = x_dot
   
        retval = []

        for n in range(epoch):
            accelleration = self.getAcceleration()
            self.x_dot = self.x_dot + accelleration 
            self.x =self.x + (self.x_dot * t)

            retval.append(self.x)

        return retval

