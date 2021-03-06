#!/usr/bin/python3

#jobScanner 2.0 (migrate from shell to Python) 8/10/20

#Purpose: Scan jobs, determine suitability then generate email response

import csv
import time
import sys
import os

import tkinter as tk
#from tkinter import simpledialog
from tkinter import simpledialog

ROOT = tk.Tk()

ROOT.withdraw()
# the input dialog
USER_INP = simpledialog.askstring(title="Test",
                                  prompt="What's your Name?:")

# check it out
print("Hello", USER_INP)



'''
Workflow:

Setup:
 - [x]  CSV file with Skills and ranks
 - [ ]  File with job description (or user copy paste description)
 
 Resume in application folder
 - [ ]  - Run resume ingester (load and convert resume to usable data structure

Prepare job description for loading:
 - [ ]  Remove non alpha
 - [x]  Lowercase all
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

FILES:

mySkills.csv: File with user's skills
job.txt:      File with job description  

DATA STRUCTURES:

    mySkills = {}     -- Dictionary of skills rates(importance of skill)
    job = {}          -- Dictionary of job's required skills
    resume = [[],[]]  -- List of lists; each element is a nested list, representing one past job

VARIABLES:

    jobScore=Sum of all scores for each skill found in job

'''

#------------------------------------------------------------------ FUNCTIONS


def load_skills():
    '''
    Load skills from CSV file into a dict called mySkills.

            File: mySkilles.csv

    '''

    print ("*** Loading skills ***"); time.sleep(.7)
    global mySkills
    
    with open('mySkills.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mySkills = {rows[0]:rows[1] for rows in reader}
        #print (mySkills)                             #QA
    
    print ("*** Skills loaded ***\n"); time.sleep(.7)


def load_job():
    '''
    Load job description into dictionary called job{}.

            File: mySkilles.csv
            #[x] Iterate through skills list
            #[x] count each skill
            #[x] append to job{} dict (only has matched skills)
            #[x] count and return the total skills score
            #8/18/20

    '''
    print ("*** Loading Job  ***"); time.sleep(.7)
    
    global job; global jobScore
    job = {}
    jobScore=0
   
    with open ('job.txt', 'r') as file:
        jobSource = file.read().lower()     #Read job description into variable 'data'

    for skill in mySkills:
        count=jobSource.count(skill)             #Count skill. NOTE: update so count is an OR. Count UNIX OR Linux OR redhat. Nested?
        if count == 0:
            continue                             #Go to next skill if not found

        print ("Found",skill); time.sleep(0.6)
        rate = int((mySkills[skill]))            #Rate for the skill; value in dict
        countTotal = count * rate; print ("    Score: ",countTotal); time.sleep(0.3)
        jobScore += countTotal                   #Sum of all skill's scores
        job.update({skill : countTotal})

    time.sleep(2); os.system('clear')
    job_sorted = sorted(job.items(), key=lambda x: x[1], reverse=True)   #Sort by scores

    #Display scores for top 5 skills:
    displayMax=4; displayC=0

    print ("Most popular skills found (Skill/Score):\n__________________________\n")

    for i in job_sorted:
        displayC+=1
        if displayC < 5:
            print (i[0], i[1])
        else:
            break

    #print (job_sorted)

    print ("\n*** Job Loaded ***\n"); time.sleep(.7)
    return jobScore
    

def load_resume():
    '''
    Load job history from resume into list called resume[].

            parse resume for years, companies and skills
            create list of lists: resume[]

    '''    
    print ("*** Loading resume ***"); time.sleep(.7)

    global resume
    
    print ("*** Resume Loaded ***\n"); time.sleep(.7)


def write_letter():
    '''
    Write response letter (respond to job post).

            Iterate through matched skills list
            Search each job for skills
            where skill exists, get company/year
            create response letter
            Print letter

    '''
    print ("*** Writing letter ***"); time.sleep(.7)

    print ("*** Letter written ***\n"); time.sleep(.7)


def door():
    '''
    Allow user to scan another job or exit.

            n=exit
            otherwise, loop will continue as normal. Should iterate.

    '''   
    global reply

    reply = input ("Would you like to apply for another job? (y/n)")
    
    if reply == "n":
        sys.exit("Have a good day and good luck on your job search!"); time.sleep(3)                              

#___________________________________________________________________________________________ FUNCTIONS

#MAIN:

load_skills()
#print (mySkills,"\n") ; time.sleep(1) #QA
os.system('clear')

#Job Scanner loop:
while True:
    print ("Beginning Job scan\n\n"); time.sleep(2); #os.system('clear')
    
    load_job()                   #Load job and return score
    print ("Job Score:",jobScore)             #QA: confirm job score is returned from load_job function

    #Check if job is a match or not
    if jobScore > 16:            #True if Job is a match based on score
        print ("Congrats! This job looks like a good match for your background!\n\n"); time.sleep(1)
        load_resume()
        write_letter()
        door()

    if jobScore < 17:            #True if job not match; lets user respond anyway or scan another job
        reply = input ("Job does not appear to be a good match!\n\nDo you want to apply for this job anyway? (y/n)")
        if reply == "y":     #Apply for job anyway, even though job was not a match
            load_resume()
            write_letter()
            door()
        
        else:
            door()


print ("Reached end of program!")

