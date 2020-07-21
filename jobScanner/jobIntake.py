#!/usr/bin/python3

#Take details of contacts

import csv

#Functions
#---------------
def readRecords():
    print ('Here are your records')

    global existingRecords
    with open('jobsRecords.dat', newline='') as f:
        reader = csv.reader(f)
        existingRecords = list(reader)

def addRecord():
    newRecord='start'

    while True:
        if newRecord=='':
            break

        fields=['Name: ','Company: ','Number: ']
        #newRecord='start'
        for field in fields:
            if newRecord=='':
                break
            newRecord=input(field)
            if newRecord=='':
                break


#====================================

#Read existing records into list

readRecords()
#records=records
#print(records)


############ Take new records and add to existingRecords
#MENU

while True:
    print ('CHOOSE OPTION BELOW:\n\n')
    selection=input('New Record: A\nSearch Record: B\n')

    if selection=='A':
        print ('You want new record')
        addRecord()
    elif selection=='b':
        print ('You want search')
    elif selection=='':
        break

print('Bye now!')
