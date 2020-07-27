#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 20:19:25 2020

@author: z003z7n
"""

class Person:
    def greet(self):
        print('I am a Person')
 
class Teacher(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Teacher')
 
class Student(Person):
    def greet(self):
        Person.greet(self)    
        print('I am a Student')
 
class TeachingAssistant(Student, Teacher):
     def greet(self):
         super().greet()
         print('I am a Teaching Assistant')
       
x = TeachingAssistant()
x.greet()