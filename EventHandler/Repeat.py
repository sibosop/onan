#!/usr/bin/python
import mido
import copy
from EvUtil import getVal


class Repeat(object):
  def __init__(self,len,reps,event):
    self.len = len
    self.reps = reps
    self.event = copy.deepcopy(event)
    self.rep = 0
    self.calcReps = 0

  def fire(self,ms):
    count = ms.count
    len = getVal(self.len)
    #print "repeat fire count:"+str(count) + " len:"+str(len)
    if self.rep == 0:
      self.calcReps = getVal(self.reps)
      if self.calcReps < 1:
        raise Exception("parameter error reps:"+str(self.calcReps))    
    ms.fire(self.event)
    self.rep = self.rep + 1
    if self.rep < self.calcReps:
      next = count+len
      print "rep: count:" + str(count) + " next:"+str(next)
      ms.addEvent(next,self)
    else:
      self.rep = 0