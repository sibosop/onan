#!/usr/bin/env python

import json
import Singleton

debug=True

def setup(path):
  global specs
  
    
class specs(object):
  __metaclass__ = Singleton.Singleton
  
  
  def __init__(path):
    with open(path) as f:
      self.specs = json.load(f)
      
  def specs():
    return self.specs
