'''
Reads a csv file
'''
import csv

def generator():
    '''
    Generator for reading and storing the code
    '''
    with open('phonedata.csv', newline='') as csvfile:
        datareader = csv.reader(csvfile)
        firstline = True
        for row in datareader:
            if firstline:
                firstline = False
                continue
            yield row

data = generator()

def return_data():
    '''
    Returns data
    '''
    return data
