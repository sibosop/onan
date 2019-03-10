#!/usr/bin/python
import os
import sys
home = os.environ['HOME']
proj = "%s/GitProjects/onan"%home
sys.path.append(proj+"/EventHandler")
sys.path.append(proj)
import Singleton
import specs
import onan
import random

debug = True

class SongParser(object):
  __metaclass__ = Singleton.Singleton
  
  def __init__(self,conf,ms):
    self.conf = conf
    self.ms = ms
    self.valTypes = {
      "random" : self.doRandom
    }
    self.events = {
      "rp" : self.parseRepeat
      ,"nt" : self.parseNote
    }  
    self.parseSeq(self.conf.attr('top'))
    
  def doRandom(self,spec):
    min = self.getVal(spec['min'])
    max = self.getVal(spec['max'])
    if debug: print "random %d %d"%(min,max)
    x = lambda : random.randint(min,max)
    return x
    
  def getTg(self,spec):
    tg = spec['tg']
    print "tg: %s"%tg
    rval = 0
    if tg.__class__.__name__ == 'int':
      return self.getVal(tg)
    loop = None
    measure = None
    beat = None
    tick = None
    ms = self.conf.attr('measureSize')
    ls = self.conf.attr('loopSize')
    state = 0
    rval = []
    for val in tg:
      rval.append(self.getVal(val))
    print "tg: %s"%rval
    return rval
  
  def parseNote(self,spec):
    tg = self.getTg(spec)
    note = self.getVal(spec['note'])
    vel = self.getVal(spec['vel'])
    len = self.getVal(spec['len'])
    if debug: print "tg %s note %s vel %s len %s"%(tg,note,vel,len)
    
  def parseSeq(self,spec):
    print "spec %s"%spec
    offset = self.getVal(spec['offset'])
    for e in spec['list']:
      if debug: print "event",e
      self.events[e.keys()[0]](e[e.keys()[0]])
  
  
  def doConst(self,spec):
    if debug: print "doConst",spec
    return spec['val']
    
  def getVal(self,inVal):
    if debug: print "inVal type: %s"%inVal.__class__.__name__
    rval = 0
    if inVal.__class__.__name__ == 'int':
      rval = inVal 
    elif inVal.__class__.__name__ == 'unicode':
        rval = self.lookup(inVal)
    elif inVal.__class__.__name__ == 'dict':
      k = inVal.keys()[0]
      print "inval key: %s"%k
      rval = self.valTypes[k](inVal[k])
    else:
      raise Exception ("can't parse %s"%inVal)
    return rval
    
  def parseRepeat(self,spec):
    if debug: print "parse repeat",spec
    tg = self.getVal(spec['tg'])
    reps = self.getVal(spec['cnt'])
    if debug: print "reps %d"%reps
    self.parseSeq(spec['seq'])
  

  