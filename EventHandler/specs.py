#!/usr/bin/env python

import json
import Singleton
import argparse

import os
defaultSpecPath = os.environ['HOME'] + "/GitProjects/onan/specs/onan.json"
import sys
debug=True

class specs(object):
  __metaclass__ = Singleton.Singleton

  def loadSpecs(self,file):
    if file in self.specList:
      if debug: print "%s already loaded"%file
      return
    self.specList.append(file)
    path = "%s/%s"%(self.specDir,file)
    if debug: print "path %s"%path
    specs = {}
    with open(path) as f:
      specs = json.load(f)
      if 'include' in specs:
        if debug: print "found include"
        for i in specs['include']:
          self.loadSpecs(i)
    self.specs.update(specs)
  
  def __init__(self,path):
    self.specDir = os.path.dirname(path)
    file = os.path.basename(path)
    self.specs = {}
    self.specList = []
    self.loadSpecs(file)
      
  def attr(self,a):
    return self.specs[a];



if __name__ == '__main__':
  parser = argparse.ArgumentParser() 
  parser.add_argument('-c','--config',nargs=1,type=str,default=[defaultSpecPath],help='specify different config file')
  args = parser.parse_args()
  if debug: print("config path"+args.config[0])
  specs = specs(args.config[0])
  print specs.specs

