#!/usr/bin/python

from LIS3DH import LIS3DH
import time
import math

# sensor_a will be the sensor on the handle bars
# debug=False just turns off the verbose output when initializing
sensor_a = LIS3DH(address = 0x18, debug = False)
# This sets the range to 16G because you're biking 
# allowed options are: 2G(default), 4G, 8G, 16G
sensor_a.setRange(LIS3DH.RANGE_16G)

# set up the second sensor(mount this one on the lower fork arm)
sensor_b = LIS3DH(address = 0x19, debug = False)
sensor_b.setRange(LIS3DH.RANGE_16G)

if __name__ == '__main__':
  with open("/home/pi/bike_accel/python-lis3dh/bike_data.csv", "a") as log:
    # You could read a button input here to wait until triggered to start logging
    while True:
      # This order helps to align readings as close as possible
      ax = sensor_a.getX()
      bx = sensor_b.getX()
      ay = sensor_a.getY()
      by = sensor_b.getY()
      az = sensor_a.getZ()
      bz = sensor_b.getZ()
      # this calculates the magnitude of the accelerometers
      magnitude_a = math.sqrt(math.pow(ax,2) + math.pow(ay,2) + math.pow(az,2))
      magnitude_b = math.sqrt(math.pow(bx,2) + math.pow(by,2) + math.pow(bz,2))
      # the difference between the two should only be the suspension movement
      difference = magnitude_a - magnitude_b
      # I don't want long numbers so I'm cutting them off at 3 decimal places
      difference = format(difference, '.3f')
      # This writes the timestamp and the value we just calculated
      # If your suspension isn't moving, you should see a number close to 0
      log.write(format(time.time()*1000, '.1f') + "," + difference + ";")
      # because we don't have interrupts, this is how I'm timing the samples
      # to get a more accurate sample interval, you'll need to look into 
      # buffer sampling and interrupts.
      time.sleep(0.001)
