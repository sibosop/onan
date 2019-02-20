#!/usr/bin/python
import Singleton
import Trigger

debug = True

class SongParser(object):
  __metaclass__ = Singleton.Singleton
  
  def __init__(self,spec):
    self.valTypes = {
      "random" : self.doRandom
    }
    self.events = {
      "rp" : self.parseRepeat
      ,"nt" : self.parseNote
    }  
    self.parseSeq(spec['top'])
    
  def doRandom(self,spec):
    
    min = self.getVal(spec['min'])
    max = self.getVal(spec['max'])
    if debug: "random %d %d"%(min,max)
    return 0  
  
  def parseNote(self,spec):
    tg = self.getVal(spec['tg'])
    note = self.getVal(spec['note'])
    vel = self.getVal(spec['vel'])
    len = self.getVal(spec['len'])
    if debug: print "tg %s note %d vel %d len %d"%(tg,note,vel,len)
    
  def parseSeq(self,spec):
    for e in spec:
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
      v = inVal.split(':')
      if len(v) == 1:
        rval = self.lookup(inVal)
      else:
        rval = Trigger.Trigger(inVal)
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
  

  