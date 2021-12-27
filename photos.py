#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd7in5_V2.EPD()
    
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    photo = Image.new('1', (epd.width, epd.height), 255)  # 255: clear the frame


    i = 1
    while i < 10:

        img = "/home/pi/photos/" + str(i) + ".jpg"
        bmp = Image.open(img)
        photo.paste(bmp, (0,0))
        epd.display(epd.getbuffer(photo))
        time.sleep(3600)

        i += 1
        if i == 10:
            i = 1

    #logging.info("Clear...")
    #epd.init()
    #epd.Clear()

    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()
