#!/usr/bin/env python
import os
import sys
proj = os.environ['HOME'] + "//GitProjects/onan"
unbuff = os.environ['PYTHONUNBUFFERED']
sys.path.append(proj+"/EventHandler")

import random
import specs

import datetime
import time
import pygame
from MidiScheduler import MidiScheduler


def usage():
  print "usages:",sys.argv[0]," pathToConfigFile"
  os._exit(-1)

if __name__ == '__main__':
  random.seed()
  pname = sys.argv[0]
  os.environ['DISPLAY']=":0.0"
  os.chdir(os.path.dirname(sys.argv[0]))
  print(pname+" at "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))  
  if len (sys.argv) < 2:
    usage()
  specs.setup(sys.argv[1])
  pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
  pygame.init()
  ms = MidiScheduler(inPort='IAC Driver IAC Bus 2',outPort='IAC Driver IAC Bus 1')
  ms.run()