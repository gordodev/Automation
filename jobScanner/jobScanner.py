#!/usr/bin/python3

import csv
import time

'''
#mySkills.csv: File with user's skills

'''

def load_skills():
    #mySkills.csv
    global mySkills
    with open('mySkills.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mySkills = {rows[0]:rows[1] for rows in reader}
        #print (mySkills)

load_skills()
print (mySkills)



git:
    git add .
    git commit -m "$m"
    git push -u origin master
