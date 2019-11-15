#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:59:12 2019

@author: captcha
"""
import re

def file_save(txt):
    """ takes in the file and saves into a text variable to do as needed """
    text_read = open(txt).read()
    return text_read
    
def file_splitting(text):
    """ takes in the file, and returns an array of 5 different arrays 
        containing classes open each day of the week. """
    text = re.split('Monday|Tuesday|Wednesday|Thursday|Friday', text) 
    class_text = [text[i].splitlines() for i in range(len(text))] # classes are on separate lines, will combine later
    #day = 0
    week = class_text
    week.remove([])
    for i in range(len(week)):
        for j in range(len(week[i])):
            week[i][j] = week[i][j].replace('\t','')
    class_text = [x for x in range(len(week))]
    
    for i in range(len(week)):
        week[i] = [week[i][2*j] + ' ' + week[i][2*j+1] for j in range(len(week[i])//2)]
                 
    return week
    
def test():
    """ function that uses a test file to run test commands """
    print(file_splitting(file_save("../../Desktop/test.txt")))
    