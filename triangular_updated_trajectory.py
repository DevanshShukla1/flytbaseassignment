#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)  # instance of flyt droneigation cla$

time.sleep(3)

print '0. taking off till 10m'
drone.take_off(10.0)
print 'taking down 5 m'

print ' move in a triangular trajectory of side length 10m at a height of 5m'

print ' 1. moving from Point A to B of triangle ABC'
# h^2=p^2+b^2, here square root of sum of square of p=8m and b=6m
# gives us the desired side length of 10m. 
drone.position_set(8.0, 6.0, 5, relative=True)

print ' 2. moving from Point B to C of triangle ABC'
drone.position_set(-8.0, 6.0, 0, relative=True)

print ' 3. moving back to home position  from Point C to A of triangle ABC'
drone.position_set(0, -10, 0, relative=True)

print ' 4. Landing'
drone.land(async=False)

# shutdown the instance
drone.disconnect()
