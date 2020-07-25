#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 19:58:59 2020

@author: z003z7n
"""

class Course:
    
    # constructor
    def __init__(self, title, instructor, price, lectures, users, ratings, avg_rating):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = users
        self.ratings = ratings
        self.avg_rating = avg_rating
    
    # method __self__
    def __self__(self):
        pass
    
    # method new_user_enrolled
    def new_user_enrolled(self):
        pass
    
    # method received_a_rating
    def received_a_rating(self):
        pass
    
    # method show_details
    def show_details(self):
        pass
    
class VideoCourse(Course):
    
    # constructor
    def __init__(self, length_video, title):
        # calling init of Course
        self.length_video = length_video
        
class PdfCourse(Course):
    
    # constructor
    def __init__(self, pages):
        Course.__init__(self, title, instructor, price, lectures, users, ratings, avg_rating)
        self.pages = pages
        