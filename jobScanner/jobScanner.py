#!/usr/bin/python3

#jobScanner 2.0 (migrate from shell to Python) 8/10/20

#Purpose: Scan jobs, determine suitability then generate email response

import csv
import time

'''
#mySkills.csv: File with user's skills

Workflow:

Setup:
 - [ ]  CSV file with Skills and ranks
 - [ ]  File with job description (or user copy paste description)
 Resume in application folder
 - [ ]  - Run resume ingester (load and convert resume to usable data structure
Prepare job description for loading:
 - [ ]  Remove non alpha
 - [ ]  Lowercase all
 - [ ]  Load job description into list
 - [ ]  Count skills, using skills.csv for the skills to look for
 - [ ]  Pass or Fail job description
Pass: go to responder module
Fail: Give user option to try another job or respond anyway


Task list:

 - [ ]  Figure out data structure for resume
 - [ ]  Figure out data structure for job description
 - [ ]  CODE read skill ratings into variables from a CSV source
 - [ ]  CODE Read resume into data structure
>Need dates, companies and words list (work history with skills data)
 - [ ]  CODE: Read Job Description into data structure
 - [ ]  CODE: Rank job vs skills
- [ ]  CODE: If pass: get skills, dates & comps from resume


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

