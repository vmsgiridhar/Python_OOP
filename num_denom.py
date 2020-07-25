#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 08:46:23 2020

@author: z003z7n
"""

class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        
        if dr < 0:
            self.dr = -1 * dr
    
    def show(self):
        print(f'{self.nr}/{self.dr}')

    def multiply(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        return Fraction(self.nr * other.nr , self.dr * other.dr)
 
    def add(self,other):
        if isinstance(other,int):
            other = Fraction(other)
        return Fraction(self.nr * other.dr + other.nr * self.dr, self.dr * other.dr)
    
    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s

            