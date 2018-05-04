#!/usr/bin/env python3
#############################################################
# Title: Python JSON Data Class                             #
# Description: Handles JSON text structure and allows       #
#              easy access to the raw data                  #
# Version:                                                  #
#   * Version 1.0 05/04/2018 RC                             #
#                                                           #
# Author: Richard Cintorino (c) Richard Cintorino 2018      #
#############################################################


from Debug import pyDebugger

class pyJSON():

   def __init__(self,sJSONData,bDebug=True,bBase64Encoding=False):
      self.Debugger = pyDebugger(self,bDebug,False)
      self.Debugger.Log("Initializing JSON Data Class with Bas64Encoding=" + str(bEncryption) + "...")
      self._bDebug = bDebug
