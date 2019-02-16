#!/usr/bin/python
import MidiScheduler
import sys


def Trigger(spec):
  loop = 0
  measure = 0
  beat = 0
  tick = 0
  ms = MidiScheduler.measureSize
  ls = MidiScheduler.loopSize

  #print "Trigger spec:"+spec
  vals = spec.split(":")
  try:
    l = len(vals)
    #print "Trigger len:" + str(l) + " vals:" + str(vals)
    if l == 1:
      tick = int(vals[0])
    elif l == 3:
      measure = int(vals[0])-1
      beat = int(vals[1])-1
      tick = int(vals[2])
    elif l == 4:
      loop = int(vals[0])-1
      measure = int(vals[1])-1
      beat = int(vals[2])-1
      tick = int(vals[3])
    else:
      raise Exception("Trigger bad parameter:"+spec)
  except:
    print("Unexpected error:", sys.exc_info()[0])
    raise Exception(sys.exc_info()[0])
  return (loop*(ms*ls))+(measure*ms)+(beat*24)+tick
      