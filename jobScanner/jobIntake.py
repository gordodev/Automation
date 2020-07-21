#!/usr/bin/python3

#Keep track of all job search contacts (emails/calls)

import csv
import time
from os import system


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

###################                                 <<<WRITE NEW RECORD TO CSV FILE>>>
def writeRecord(sourceRecord):
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

        fields=['Name: ','Company: ','Number: ','NOTES: ']
        #newRecordElement='start'
        for field in fields:
            if newRecordElement=='':                       #If nothing entered for any field, then break
                break                           #QA: Does this work?
            newRecordElement=input(field)
            if newRecordElement=='':
                break                           #QA: Does this work? I THINK THIS IS REDUNDANT, SAME CODE ABOVE
        
            newRecord.insert(0,newRecordElement)           #Add new record element to newRecord list
            print ('.')

        if newRecordElement=='':
            print ('\nNothing entered!\n')
            time.sleep(2)
        else:
            print ('\nInserting new record: \n',newRecord,'\n') 
            time.sleep(2)
            writeRecord(newRecord)                      #This new record inserting/append is now failing?
        clear()

#=======================================================================

clear()
#Read existing records into list

readRecords()
#records=records
print('_____________________________________________________________________________________________________________\n\n',existingRecords[:5],'\n_____________________________________________________________________________________________________________\n')


############ Take new records and add to existingRecords
#MENU

while True:
    print ('CHOOSE OPTION BELOW:\n\n')
    selection=input('New Record: A\nSearch Record: B\n')

    if selection=='A' or selection=='a':
        print ('\n***  Add new records  ***\n')
        addRecord()
    elif selection=='b':
        print ('You want search')
    elif selection=='':
        break
    else: 
        print ('!!!Choose valid option from above!!!\n')
        continue

print('Bye now!')
