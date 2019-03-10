#!/usr/bin/env python
import os
import sys
home = os.environ['HOME']
proj = "%s/GitProjects/onan"%home
sys.path.append(proj+"/EventHandler")
import random
import specs
import argparse
import datetime
import time
import pygame
import SongParser
from MidiScheduler import MidiScheduler
debug=True
defaultSpecPath="%s/Specs/onan.json"%proj
conf = None

if __name__ == '__main__':
  random.seed()
  pname = sys.argv[0]
  os.environ['DISPLAY']=":0.0"
  os.chdir(os.path.dirname(sys.argv[0]))
  print(pname+" at "+datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
  parser = argparse.ArgumentParser() 
  parser.add_argument('-c','--config',nargs=1,type=str,default=[defaultSpecPath],help='specify different config file')
  args = parser.parse_args()
  if debug: print("config path"+args.config[0])
  conf = specs.specs(args.config[0])
  print conf.specs
  ms = MidiScheduler(inPort='IAC Driver IAC Bus 2',outPort='IAC Driver IAC Bus 1')
  songParser = SongParser.SongParser(conf,ms)
  #pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
  #pygame.init()
  
  #ms.run()