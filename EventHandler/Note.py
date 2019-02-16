#!/usr/bin/python
import mido
from EvUtil import getVal

class Note(object):
  def __init__(self,note,vel,len,chan=0):
    self.vel = vel
    self.note = note
    self.len = len
    self.chan = chan
    
  def fire(self,ms):
    playNote = getVal(self.note)
    playVel = getVal(self.vel)
    playChan = getVal(self.chan)
    playLen = getVal(self.len)
    msg=mido.Message('note_on',note=playNote,velocity=playVel,channel=playChan)
    #print 'count:'+str(ms.count)+' '+str(msg)+' '
    ms.midiOut.send(msg)
    if playVel != 0:
      off=ms.count+playLen
      ms.addEvent(off,Note(note=playNote,vel=0,len=0,chan=playChan))