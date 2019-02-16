#!/usr/bin/python
import random

def getVal(inVal):
  rval = 0
  try:
    rval = inVal()
    #print "func"
  except:
    rval = inVal
    #print "native type"
    
  
  #if inVal.__class__.__name__ == 'int' or inVal.__class__.__name__ == 'str':
    #rval = inVal
  #else:
    #rval = inVal()
  return rval
  
def chooseUnique(list,count):
  rval = []
  tmp = list[:]
  for x in range(0,count):
    v = tmp[random.randint(0,len(tmp)-1)]
    rval.append(v)
    tmp.remove(v)
  return #