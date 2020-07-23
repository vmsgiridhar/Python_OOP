#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:20:03 2020

@author: z003z7n
"""

class Product:
    def __init__(self):
        self._x = 10
        self._y = 15
    
    # We are using @property to make display to work as an instance variable than a function
    # Getter method
    @property
    def display(self):
        return self._x
    
    # we cant set any value to p1 = Product(), p1.display = 20
    # to do that we need to do the following
    
    # Setter method
    @display.setter
    def display(self, val):
        self._x = val