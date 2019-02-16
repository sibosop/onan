#!/usr/bin/python
import mido
from EvUtil import getVal


class CCEvent(object):
  def __init__(self,cc,val,chan=0):
    self.cc = cc
    self.val = val
    self.chan = chan
    
  def fire(self,ms):
    cc = getVal(self.cc)
    val = getVal(self.val)
    chan = getVal(self.chan)
    msg=mido.Message('control_change',value=val,control=cc,channel=chan)
    print 'count:'+str(ms.count)+' '+str(msg)+' '+ms.__class__.__name__+' '+ms.midiOut.__class__.__name__
    ms.midiOut.send(msg)