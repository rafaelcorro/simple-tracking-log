############################ Copyrights and license #############################
#                                                                               #
# Copyright 2020 Rafael Corro Haba <rafaelcorro@gmail.com>                      #
# Link https://github.com/rafaelcorro/simple-tracking-log                       #
# License: Mit                                                                  #
#                                                                               #
#################################################################################

import os
import datetime
import re


class LogFile:
    def __init__(self,data):
        self.maxline=data["maxline"]
        self.filename=data["filename"]
    
    def newline(self,level,message):
        # Open input file in 'read' mode
        with open(self.filename, "r") as rfile:
            lines = rfile.readlines()
            nlines=len(lines)
            substract=0
            if nlines>self.maxline:
                substract = nlines-self.maxline
        # Open input file in 'write' mode
        with open(self.filename, "w") as wfile:
            num=0
            # Loop over each log line
            for line in lines:
                if num>=substract:
                    wfile.write(line)    
                num+= 1
            if nlines>0:
                frac=re.split(',',line)
                nlog=int(frac[1])+1
            else:
                nlog=1

        if level=="1":
            level="DEBUG"
        elif level=="2":
            level="INFO"
        elif level=="3":
            level="WARN"
        elif level=="4":
            level="ERROR"
        elif level=="5":
            level="FATAL"

        now = datetime.datetime.now()
        datelog = str(now.year)+"-"+str('{:02d}'.format(now.month))+"-"+str('{:02d}'.format(now.day))+" "+str('{:02d}'.format(now.hour))+":"+str('{:02d}'.format(now.minute))+":"+str('{:02d}'.format(now.second))
        message=datelog+","+str(nlog)+", "+level+" - "+message
        # Open output file in 'append' mode
        with open(self.filename, "a") as afile:
            afile.write(message+" \n")
    
data={}
#maximum number of lines allowed in the file
data["maxline"]=5
#log file name
data["filename"]="janus.log"
log=LogFile(data)
#indicate the level and the message
message="esto es un mensaje"
log.newline("1",message)

"""
    1.-DEBUG: Detailed information, typically of interest only when diagnosing problems.
    2.-INFO: For messages that show information about the program during its execution (for example, version to be executed, processes that are launched, etc.)
    3.-WARN: For warning messages about abnormal situations that occur, but that do not affect the correct operation of the program.
    4.-ERROR: To keep a record of program errors that, although it may continue to work, affect its operation. For example, a configuration parameter has an incorrect value, or a non-critical file is not found.
    5.-FATAL: It is used for critical messages, due to errors that make the program generally abort its execution.
"""
