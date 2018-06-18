#!/usr/bin/python
import mido
import sys
mido.set_backend('mido.backends.rtmidi')
out= mido.open_output('IAC Driver IAC Bus 1') 
msg=mido.Message('control_change',value=int(sys.argv[2]),control=int(sys.argv[1]))
print msg
out.send(msg)
