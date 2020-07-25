#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:31:36 2020

@author: z003z7n
"""

class Person:
    
    # init method of Person class
    def __init__(self, name, city):
        self.name = name
        self.city = city
    
    # print of data from Person
    def showDetails(self):
        print('The Person name is: ',self.name, ' His address is: ', self.city)
        
class Employee(Person):
    
    # init method of Employee class
    def __init__(self, name, city, job, company):
        self.job = job
        self.company = company
        Person.__init__(self, name, city)
        super().__init__(name, city)
    # print of data from Employee
    def showDetails(self):
        Person.showDetails(self)
        super().showDetails()
        print('The Employee job is: ',self.job, 'and he works at: ', self.company)