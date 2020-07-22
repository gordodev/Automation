#!/usr/bin/python3

#Keep track of all job search contacts (emails/calls)
#Data will be stored in flat file(CSV)
#Data should be searchable and able to be changed

import csv
import time
from os import system

from datetime import datetime

print(datetime.today().strftime('%Y-%m-%d %H:%M'))
myDate=(datetime.today().strftime('%Y-%m-%d %H:%M'))     #Date for data entry

#Functions
#--------------------------------------------------
############
def clear():
    _=system('clear')

##################                                  <<<READ RECORDS FROM CSV FILE & insert into existingRecords>>>
def readRecords():
    print ('[Loading existing records]\n')
    time.sleep(0.8)

    global existingRecords                          #Make records list global
    with open('jobsRecords.dat', newline='') as f:  #Populate existingRecords list with csv
        reader = csv.reader(f)
        existingRecords = list(reader)

###################                                 <<<APPEND NEW RECORD TO CSV FILE>>>
def appendRecord(sourceRecord):
    print ('[Inserting new records]\n')
    time.sleep(0.8)

    with open('jobsRecords.dat', 'a', newline='') as f:  #QA- Is this function broken? Now new rows anymore
        writer = csv.writer(f)
        writer.writerow(sourceRecord)

################                                   <<<GET NEW RECORD FROM USER>>>
def addRecord():
    newRecordElement='start'                               #Initializing newRecordElement var
    newRecord=[]                                           #Init newRecord list

    while True:
        if newRecordElement=='':                           #Stop adding records if nothing entered
            break                               #QA: Does this work?

        #FULL SCHEMA: ['Name: ','Company: ','Number: ','NOTES: ','Salary: ','Date: ','Record #','Rating','Interview Count','Status']
        fields=['Name: ','Company: ','Number: ','NOTES: ','Salary: ','Date: ','Record #: ','Rating: ','Interview Count: ','Status: ']
        #newRecordElement='start'
        for field in fields:
            if newRecordElement=='':                       #If nothing entered for any field, then break
                break                           #QA: Does this work?
            newRecordElement=input(field)
            if newRecordElement=='':
                break                           #QA: Does this work? I THINK THIS IS REDUNDANT, SAME CODE ABOVE
        
            newRecord.insert(0,newRecordElement)                    #Add new record element to newRecord list
            print ('.')

        if newRecordElement=='':
            print ('\nNothing entered!\n')
            time.sleep(2)
        else:
            print ('\nInserting new record: \n',newRecord,'\n')
            myDate=(datetime.today().strftime('%Y-%m-%d %H:%M'))
            recordID=(datetime.today().strftime('%y%m%d%S'))       #QA: Future refactor to replace with numeric values. Just have to search records to figure what next record number should be.
            newRecord.insert(0,myDate)
            time.sleep(2)
            appendRecord(newRecord)                                #This new record append is now failing?
        clear()

#=======================================================================

clear()
#Read existing records into list

readRecords()
#records=records
#PRINT LAST 5 RECORDS
print('_____________________________________________________________________________________________________________\n\n',existingRecords[-5:],'\n____________________________________________________________________________________________________________\n')


############ Take new records and add to existingRecords
#MENU

while True:
    print ('\nCHOOSE OPTION BELOW:\n\n')
    selection=input('(A) Add new Record\n(B) Search existing Records\n')

    if selection=='A' or selection=='a':
        print ('\n***  Add new records  ***\n')
        addRecord()
    elif selection=='B' or selection=='b':
        print ('\nHere are the existing records:\n')
        readRecords()                                                           #Update records
        print (existingRecords)                                                 #Print existing records
    elif selection=='':
        break
    else: 
        print ('!!!Choose valid option from above!!!\n')
        continue

print('Bye now!')

#NOTES:
'''
Future upgrade; xcel support: https://www.youtube.com/watch?v=1Kcco6koC34


'''
