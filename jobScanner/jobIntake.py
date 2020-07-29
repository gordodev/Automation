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
def read_records():
    print ('[Loading existing records]\n')
    time.sleep(0.8)

    global existingRecords                          #Make records list global
    with open('jobsRecords.dat', newline='') as f:  #Populate existingRecords list with csv
        reader = csv.reader(f)
        existingRecords = list(reader)

###################                                 <<<APPEND NEW RECORD TO CSV FILE>>>
def append_record(sourceRecord):
    print ('[Inserting new records]\n')
    time.sleep(0.8)

    with open('jobsRecords.dat', 'a', newline='') as f:  #QA- Is this function broken? Now new rows anymore
        writer = csv.writer(f)
        writer.writerow(sourceRecord)

################                                   <<<GET NEW RECORD FROM USER>>>
def addrecord():
    newRecordElement='start'                               #Initializing newRecordElement var
    newRecord=[]                                           #Init newRecord list

    while True:
        if newRecordElement=='':                           #Stop adding records if nothing entered
            break                               #QA: Does this work?

        #FULL SCHEMA: ['Name: ','Company: ','Number: ','NOTES: ','Salary: ','Date: ','Record #','Rating','Interview Count','Status']
        #FULL SCHEMA: ['Date','Firm','Agency','Name','Rating','Type','Rate','Interview Count','Days since last contact','Status','Source','Notes']
        '''
        DESIGN NOTES: Pick a schema and stick to it. Perhaps include 5-6 custom fields for future use. So maybe do this:
        fields=['','','','','','','','','','']

        Then have a note with field numbers for refrence
        When you loop through field names to insert values or whenever you insert values, use the designated index numbers
        Maybe us an if statement that matches the field name with index number like; if name=='notes', then index=4. Then insert value into [4]

        '''
        fields=['Name: ','Company: ','Number: ','NOTES: ','Salary: ','Rating: ','Interview Count: ','Status: ']
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
            append_record(newRecord)                                #This new record append is now failing?
        clear()

#=======================================================================

clear()
#Read existing records into list

read_records()
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
        addrecord()
    elif selection=='B' or selection=='b':
        print ('\nHere are the existing records:\n')
        read_records()                                                           #Update records
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
