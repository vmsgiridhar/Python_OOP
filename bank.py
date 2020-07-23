#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:53:50 2020

@author: z003z7n
"""

class bank_account:
    
    # constructor - called just after the object creation
    # dunder - double underscore
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    
    # #method 1
    # def set_details(self, name, balance=0):
    #     self.name = name
    #     self.balance = balance
    
    #method 2
    def display(self):
        print('Name of customer:', self.name)
        print('Balance:', self.balance)
    
    #method 3
    def withdraw(self, amount):
        self.balance -= amount
    
    #method 4
    def deposit(self, amount):
        self.balance += amount

cust1 = bank_account('Giri', 50000)
cust2 = bank_account('Keeru', 100000)