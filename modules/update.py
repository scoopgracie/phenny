import subprocess
import os
import sys

def checkup(phenny, input):
    """.checkup - Check if begiak is up"""
    phenny.say("Pulling new source code...")
    if subprocess.call(['git', 'pull']) == 0:
        phenny.say("Successfully pulled...")
    else:
        phenny.say("Uh oh...")
        return 0
    
    phenny.say("Beginning to restart...")
    phenny.say("If I rejoin, I succeeded.")
    os.execv('./phenny', sys.argv)

checkup.commands = ['update']
checkup.priority = 'high'
checkup.example = '.update'
