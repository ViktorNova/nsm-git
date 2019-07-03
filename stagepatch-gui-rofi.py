#!/usr/bin/env python3
# filename: stagepatch-gui.py

# I should probably just redo this in bash!!!!!!

import os
import sys
import subprocess
from rofi import Rofi
import argparse                 #for incoming arguments
import signal

# -----------------------------------------------------------------------
r = Rofi()

# Parse the arguments sent by the main process
# so that we know what we're working with
parser = argparse.ArgumentParser()
parser.add_argument("saveFile") # First argument (AJ-Snapshot saveFile)
parser.add_argument("pid")      # Second argument  (AJ-Snapshot PID)
args = parser.parse_args()

# Convert the parsed arguments into variables
saveFile = args.saveFile
pid = int(args.pid)
# Print the stuff

print("Patchbay save file is %s" % saveFile)
print("aj-snapshot pid is ")
print(pid)

def overwrite(self): # Save Patchbay
    print("Overwritepatchbay is clicked")
    print("Saving current MIDI and JACK connections over existing patchbay")
    subprocess.call(["aj-snapshot", "-f", self.saveFile],
                     stdout=subprocess.PIPE,
                     preexec_fn=os.setsid)
    print("Attempting to restart the thingy")
    os.kill(self.pid, signal.SIGHUP)
    print("OK, see if it got restarted.")
                    # Replace this with a proper python sendsignal thing
                    #subprocess.call(["kill", "-HUP", self.pid],
                    #=               stdout=subprocess.PIPE,
                    #                preexec_fn=os.setsid)


options = ['Overwrite Patchbay', 'Reload from save file', 'Disconnect All']
index, key = r.select('Would you like to save all JACK and  MIDI connections', options)

# Index contains the value that was selected
print("You chose option : ", index)


