import numpy as np
import os,sys
from util.yaml_reader import yamlReader
input_=int(input("Press \n 1. To Accept input from console \n 2. To Accept input from configuration file: \t "))
if input_ ==1:
    #Passengers Input
    number =int(input("Enter Number of Passengers: "))

    #Dimensions Input
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))
    
    
    print("Enter the entries in a single line (separated by space): ")
    
    # User input of entries in a 
    # single line separated by space
    entries = list(map(int, input().split()))
    
    # For constructing the matrix
    seatsGrid = np.array(entries).reshape(R, C)
elif input_ ==2:
    #Reading from configuration file(input.yaml)
    config = yamlReader(os.path.dirname(os.path.realpath(__file__)) + '/config/input.yaml')
    number = config['passengers']
    seatsGrid = config ['dimensions']
else:
    print("Wrong Option!!")

#temporary variables
filled = 0
row = 0
tempFilled = -1

def construct(seatsGrid):
    '''
    Method to construct seatsGrid
    '''
    seats = []
    for i in seatsGrid:
        rows = i[1]
        cols = i[0]
        # mat = [[-1]*cols]*rows
        mat = []
        for i in range(rows):
            mat.append([-1]*cols)
        seats.append(mat)
    return seats

def printSeats(seats):
    '''
    Method to print seats in console
    '''
    blksize = len(str(number))
    rows = [x[1] for x in seatsGrid]
    cols = [x[0] for x in seatsGrid]
    maximum = max(rows)
    top = True
    for i in range(maximum):
        rowlist = []
        rowlistl = []
        for j in range(length):
            row = ' '
            rowl = ' '
            if len(seats[j]) <= i:
                for k in range(cols[j]):
                    row += ' '*blksize
                    rowl += ' '*blksize
                    row += ' '
                    rowl += ' '
            else:
                row = '|'
                rowl = '+'
                for k in seats[j][i]:
                    if k == -1:
                        row += ' '*blksize
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
                    else:
                        row += str(k)+(' '*(blksize - len(str(k))))
                        rowl += '-'*blksize
                        row += '|'
                        rowl += '+'
            
            rowlist.append(row)
            rowlistl.append(rowl)
        if top:
            print('    '.join(rowlistl))
            top = False
        print('    '.join(rowlist))
        print('    '.join(rowlistl))

                
def fillAisleSeats():
    '''
    Method to fill Aisle seats
    '''
    # filled = 0
    global filled
    row = 0
    tempFilled = -1
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if i == 0 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = seatsGrid[i][0] - 1
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                elif i == length - 1 and seatsGrid[i][0] > 1:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                else:
                    filled += 1
                    aisleCol = 0
                    seats[i][row][aisleCol] = filled
                    if filled >= number:
                        break
                    if seatsGrid[i][0] > 1:
                        filled += 1
                        aisleCol = seatsGrid[i][0] - 1
                        seats[i][row][aisleCol] = filled
                        if filled >= number:
                            break
        row += 1


def fillWindowSeats():
    '''
    Method to fill Window Seats
    '''
    row = 0
    global filled
    global number
    tempFilled = 0
    while filled < number and filled != tempFilled:
        tempFilled = filled
        if seatsGrid[0][1] > row:
            filled += 1
            window = 0
            seats[0][row][window] = filled
            if filled >= number:
                break
        if seatsGrid[length-1][1] > row:
            filled += 1
            window = seatsGrid[length-1][0] - 1
            seats[length-1][row][window] = filled
            if filled >= number:
                break
        row += 1

def fillMiddleSeats():
    '''
    Method to fill center seats
    '''
    row = 0
    tempFilled = 0
    global filled
    while filled < number and filled != tempFilled:
        tempFilled = filled
        for i in range(length):
            if seatsGrid[i][1] > row:
                if seatsGrid[i][0] > 2:
                    for col in range(1, seatsGrid[i][0] - 1):
                        filled += 1
                        seats[i][row][col] = filled
                        if filled >= number:
                            break
        row += 1

seats = construct(seatsGrid)
length = len(seatsGrid)
# Fill Aisle seats first
fillAisleSeats()
# Fill Window seats second
fillWindowSeats()
# Fill Center seats at last
row = 0
tempFilled = 0
fillMiddleSeats()

#To display output

output=int(input("Press \n 1. To show output in console (Recommended) \n 2. To show output in file: \t"))

if output == 1:
    #print output in console
    printSeats(seats)
elif output == 2:
    #print output in file
    f = open("outputs/output.txt","w")
    f.write(str(seats))
    f.close()
else:
    print("Wrong Option!!")