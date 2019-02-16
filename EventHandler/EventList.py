#!/usr/bin/python
import mido
from Trigger import Trigger as tg



    
class EventList(object):
  def __init__(self,list):
    self.list = list[:]
    self.iter = 0
    self.base = 0
    self.first = True
    
  def fire(self,ms):
    #print "EventList"+" iter:"+str(self.iter)
    if self.iter == 0 and self.first:
      #print "first is True"
      self.first = False
      self.base = ms.count
      offset = self.list[0][0]
      #print "offset:"+str(offset)+" base:"+str(self.base)
      if (self.base+offset) != ms.count:
        ms.addEvent(self.base+offset,self)
        return
    #print "fire"
    ms.fire(self.list[self.iter][1])
    self.iter = self.iter+1
    if self.iter == len(self.list):
      #print "Eventlist at end of list:" +str(self.iter)+' '+str(len(self.list))
      self.iter = 0
      self.first = True
    else:
      #print "trigger event:"+str(self.list[self.iter][0])+str(self.list[self.iter][0].v())
      ms.addEvent(self.list[self.iter][0]+self.base,self)
      