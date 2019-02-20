#!/usr/bin/python
import Singleton

debug = True

class SongParser(object):
  __metaclass__ = Singleton.Singleton
  
  def __init__(self,spec):
    self.valTypes = {
      "const" : self.doConst
      ,"random" : self.doRandom
    }
    self.events = {
      "rp" : self.parseRepeat
      ,"nt" : self.parseNote
    }  
    self.parseSeq(spec['top'])
    
  def doRandom(self,spec):
    if debug: "random %d %d"%(spec['min'],spec['max'])
    return 0  
  
  def parseNote(self,spec):
    note = self.getVal(spec['note'])
    vel = self.getVal(spec['vel'])
    if debug: print "note %d vel %d"%(note,vel)
    
  def parseSeq(self,spec):
    for e in spec:
      if debug: print "event",e
      self.events[e.keys()[0]](e[e.keys()[0]])
  
  
  def doConst(self,spec):
    if debug: print "doConst",spec
    return spec['val']
    
  def getVal(self,spec) :
    if debug: print "getVal",spec
    return self.valTypes[spec['type']](spec)


  def parseRepeat(self,spec):
    if debug: print "parse repeat",spec
    reps = self.getVal(spec['reps'])
    if debug: print "reps %d"%reps
    self.parseSeq(spec['seq'])
  

  