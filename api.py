#/usr/bin/python3
# coding: utf8

import hug
import time
import subprocess
import mysql.connector



print(__file__+" LAUNCHED")
#//////////////////////////////////////////////////////////////////////////////////////////////////////








#////////////////////////////////////////////////////////////////////////////////////////////////////
print(__file__+" ENDED")



#https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
p.terminate()