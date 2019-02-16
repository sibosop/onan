#!/usr/bin/python
import mido
from EvUtil import getVal
from Note import Note

class Chord(object):
  def __init__(self,chord,vel,len,chan): 
    self.chord = chord
    self.vel = vel
    self.len = len
    self.chan = chan
    
  def fire(self,ms):
    playList = []
    ch=[]
    if self.chord.__class__.__name__ == 'list':
      ch = self.chord[:]
    else:
      ch = self.chord()[:]
    for x in ch:
      playList.append(getVal(x))
    playVel = getVal(self.vel)
    playChan = getVal(self.chan)
    playLen = getVal(self.len)
    for x in playList:
      msg=mido.Message('note_on',note=x,velocity=playVel,channel=playChan)
      #print str(msg)
      ms.midiOut.send(msg)
    if playVel != 0:
      off=ms.count+playLen
      for x in playList:
        ms.addEvent(off,Note(note=x,vel=0,len=0,chan=playChan))
      