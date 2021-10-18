#!/usr/bin/python3
# -*- coding: utf-8 -*-
#

## @file common.py
#
# @author Jan Belohoubek
# @version 0.1
# @date    2019-03-02
# @brief   The KETCube common deffinitions
#
# @note Requirements:
#    Standard Python3 installation (Tested Fedora ...)
#
# @attention
# 
#  <h2><center>&copy; Copyright (c) 2019 University of West Bohemia in Pilsen
#  All rights reserved.</center></h2>
# 
#  Developed by:
#  The SmartCampus Team
#  Department of Technologies and Measurement
#  www.smartcampus.cz | www.zcu.cz
# 
#  Permission is hereby granted, free of charge, to any person obtaining a copy 
#  of this software and associated documentation files (the “Software”), 
#  to deal with the Software without restriction, including without limitation 
#  the rights to use, copy, modify, merge, publish, distribute, sublicense, 
#  and/or sell copies of the Software, and to permit persons to whom the Software 
#  is furnished to do so, subject to the following conditions:
# 
#     - Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimers.
#     
#     - Redistributions in binary form must reproduce the above copyright notice, 
#       this list of conditions and the following disclaimers in the documentation 
#       and/or other materials provided with the distribution.
#     
#     - Neither the names of The SmartCampus Team, Department of Technologies and Measurement
#       and Faculty of Electrical Engineering University of West Bohemia in Pilsen, 
#       nor the names of its contributors may be used to endorse or promote products 
#       derived from this Software without specific prior written permission. 
# 
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
#  PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE CONTRIBUTORS OR COPYRIGHT HOLDERS 
#  BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
#  OR THE USE OR OTHER DEALINGS WITH THE SOFTWARE.

### Imports
from enum import IntEnum
import signal

class SeverityLevels(IntEnum):
    NONE   = 0
    ERROR  = 1
    INFO   = 2
    DEBUG  = 3

# Global severity level    
SEVERITY_LEVEL = SeverityLevels.ERROR

class Types(IntEnum):
    PARAMS_BOOLEAN    =  1
    PARAMS_STRING     =  2
    PARAMS_BYTE       =  3
    PARAMS_INT32      =  4
    PARAMS_UINT32     =  5
    PARAMS_INT32_PAIR =  6
    PARAMS_BYTE_ARRAY =  7


## Converts string to data type
#
# @param typeStr - string representation of Types
#
# @retval type
#
def strToType(typeStr):
    if   typeStr == "PARAMS_BOOLEAN":
        return Types.PARAMS_BOOLEAN
    elif typeStr == "PARAMS_STRING":   
        return Types.PARAMS_STRING
    elif typeStr == "PARAMS_BYTE":   
        return Types.PARAMS_BYTE
    elif typeStr == "PARAMS_INT32":     
        return Types.PARAMS_INT32
    elif typeStr == "PARAMS_UINT32":
        return Types.PARAMS_UINT32
    elif typeStr == "PARAMS_INT32_PAIR":
        return Types.PARAMS_INT32_PAIR
    elif typeStr == "PARAMS_BYTE_ARRAY":
        return Types.PARAMS_BYTE_ARRAY
    else:
        return None

# Correct exit
def exitGracefully(signum, frame):
    exit(0)
    
def exitError():
    print("Fatal Error!")
    exitGracefully(None, None)

# Initialize testbench enviroment
def initEnv():
    signal.signal(signal.SIGINT, exitGracefully)
    signal.signal(signal.SIGTERM, exitGracefully)

