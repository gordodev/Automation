#!/usr/bin/python3

#jobScanner 2.0 (migrate from shell to Python) 8/10/20

#Purpose: Scan jobs, determine suitability then generate email response

import csv
import time

'''
Workflow:

Setup:
 - [x]  CSV file with Skills and ranks
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


#mySkills.csv: File with user's skills

DATA STRUCTURES:

    mySkills = {}     -- Dictionary of skills rates(importance of skill)
    job = {}          -- Dictionary of job's required skills
    resume = [[],[]]  -- List of lists; each element is a nested list, representing one past job

VARIABLES:

    jobScore=Sum of all scores for each skill found in job

'''

#------------------------------------------------------------------ FUNCTIONS

def load_skills():
    #############                Load job skills CSV into variable
    #mySkills.csv
    '''
    Load skills from CSV file into a dict called mySkills.

            File: mySkilles.csv

    '''

    print ("*** Loading skills ***"); time.sleep(2)
    global mySkills
    with open('mySkills.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mySkills = {rows[0]:rows[1] for rows in reader}
        #print (mySkills)
    
    print ("*** Skills loaded ***\n"); time.sleep(2)

def load_job():
    #########                   Load job description into dictionary called job{}
    print ("*** Loading Job  ***"); time.sleep(2)
    global job; global jobScore
    job = {}
    pass 
    #Iterate through skills list
    #count each skill
    #append to job{} dict (only has matched skills)
    #count and return the total skills score
    jobScore = 20               #QA Hard coding score until score logic is built
    
    print ("*** Job Loaded ***\n"); time.sleep(2)
    return jobScore
    

def load_resume():
    #########                  Load job history from resume into list called resume[]
    print ("*** Loading resume ***"); time.sleep(2)
    global resume
    #parse resume for years, companies and skills
    #create list of lists: resume[]
    
    print ("*** Resume Loaded ***\n")

def write_letter():
    #########                  Write response letter (respond to job post)
    print ("*** Writing letter ***"); time.sleep(2)
    #Iterate through matched skills list
    #Search each job for skills
    #where skill exists, get company/year
    #create response letter
    #Print letter

    print ("***Letter written***\n"); time.sleep(2)

def loop_control():
    #########                 Allow user to scan another job or exit
    global reply
    reply = input ("Would you like to apply for another job? (y/n)")
    
    if reply == "y":
        continue                              #WARNING!!! This function may not work. Can you continue global loop locally from within a function?
    else:
        print ("Have a good day and good luck on your job search!"); time.sleep(3)
        sys.exit("Exit application")

#___________________________________________________________________________________________ FUNCTIONS

#MAIN:

load_skills()
print (mySkills,"\n")  #QA

#Job Scanner loop:
while True:
    print ("Beginning Job scan\n\n"); time.sleep(2)
    load_job()                   #Load job and return score
    print ("Job Score:",jobScore)             #QA: confirm job score is returned from load_job function

    #Check is job is a match or not
    if jobScore > 15:            #True if Job is a match based on score
        load_resume()
        write_letter()
        loop_control()

    if jobScore < 16:            #True if job not match; lets user respond anyway or scan another job
        reply = input ("Job does not appear to be a good match!\n\nDo you want to apply for this job anyway? (y/n)")
        if reply == "y":     #Apply for job anyway, even though job was not a match
            load_resume()
            write_letter()
        else:
            reply = input ("Would you like to apply for another job? (y/n)")
            if reply == "y":
                continue
            else:
                print ("Have a good day and good luck on your job search!"); time.sleep(3)
                sys.exit("Exit application") 

print ("Reached end of program!")

#Last line added
