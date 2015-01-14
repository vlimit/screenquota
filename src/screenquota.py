#!/usr/bin/env python

import cec      # from python-cec
import os.path
import time

cec.init()

for adress, device in cec.list_devices().items():
    print device.address, device.vendor, device.osd_string

tv = cec.Device(0)
while True:

    if os.path.exists('/var/opt/screendisable/disable'):
        try:
            print tv.standby()
        
        except:
            print 'Reinitialising'
            cec.init()
            tv = cec.Device(0)

    time.sleep(2)


