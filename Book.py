#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 19:26:48 2020

@author: z003z7n
"""

class Book:
    
    # constructor
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies
    
    # method to display
    def display(self):
        print(self.isbn, self.title, self.price, self.copies)
        
    # method in_stock
    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False
        
    # method sell
    def sell(self):
        if self.in_stock():
            self.copies -= 1
        else:
            print('Book is out of stock!')
            
    # Creating a property named Price
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        
        if (price < 50 or price > 1000):
            raise Exception('Price is not valid')
        else:
            self._price = price
        
        
# implementation
book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 1000,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 220,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

listofbooks = [book1, book2, book3, book4]
for book in listofbooks:
    book.display()

titleofBooksbyJack = [book.title for book in listofbooks if book.author == 'Jack']
# book1.display()
# book2.display()
# book3.display()
# book4.display()
        
    