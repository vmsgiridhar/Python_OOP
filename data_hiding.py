#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:04:24 2020

@author: z003z7n
"""

class Product:
    def __init__(self):
        # accessible from outside the class
        self.data1 = 20
        self._data2 =30
        
        #not accessible
        self.__data3 = 40
    
    def methodA(self):
        pass
    def _methodB(self):
        pass
    def __methodC(self):
        pass