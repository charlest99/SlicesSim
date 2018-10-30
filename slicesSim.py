#Simulator for two methods of iPhone game slices. Game entails 5 sliced circles arranged in a circle
#random pieces that fill slices are given, and the user must fill the circles fully to gain points and
#reset the circle to empty, but lose the game if they are ever unable to play a piece
from random import randint
import numpy
from matplotlib import pyplot
from scipy.stats import ttest_ind

#simulates filling the circles in order, regardless of previous placement of pieces
#if a circle has the piece's position already filled, moves to the next circle in line
def fillFirst():
    pieces = [0,1,2,3,4,5] 
    double_pieces = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,0]]
    boards = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]] #define the board as empty
    pts = 0
    x = True
    while(x):
        piece = 0
        ran = randint(0, 5) #the game randomly selects either a double or single piece at a rate of about .2
        if (ran == 0):
            piece = double_pieces[ran]
            a = piece[0] #checks the doubles in each position and sees if it is possible to place the piece
            b = piece[1]
            if(boards[0][a] == 0 & boards[0][b] == 0):
                boards[0][a] = 1
                boards[0][b] = 1
                pts+=2
            elif(boards[1][a] == 0 & boards[1][b] == 0):
                boards[1][a] = 1
                boards[1][b] = 1
                pts+=2
            elif(boards[2][a] == 0 & boards[2][b] == 0):
                boards[2][a] = 1
                boards[2][b] = 1
                pts+=2
            elif(boards[3][a] == 0 & boards[3][b] == 0):
                boards[3][a] = 1
                boards[3][b] = 1
                pts+=2
            else:
                x = False #if not possible, exit while loop on next go around
        else:
            a = pieces[ran] #checks single pieces
            if(boards[0][a] == 0):
                boards[0][a] = 1
                pts+=1
            elif(boards[1][a] == 0):
                boards[1][a] = 1
                pts+=1
            elif(boards[2][a] == 0):
                boards[2][a] = 1
                pts+=1
            elif(boards[3][a] == 0):
                boards[3][a] = 1
                pts+=1
            else:
                x = False

            for u in range(4): 
                it = 0
                it_o = 0
                if(boards[u][0] == 1 & boards[u][1] == 1 & boards[u][2] == 1 & 
                   boards[u][3] == 1 & boards[u][4] == 1 & boards[u][5] == 1):
                    if (u == 3):
                        it = 2
                        it_o = 0
                    elif (u == 0):
                        it = 1
                        it_o = 3
                    else:
                        it = u -1
                        it_o = u+1
                    pts += 6
                    temp_pts = sum(boards[it]) + sum(boards[it_o])
                    pts+= temp_pts
                    for c in range(6):
                        boards[u][c] = 0
                        boards[it][c] = 0
                        boards[it_o][c] = 0
    return pts


#checks to fill based on the total number of pieces already in each circle, attempting to fill the most
#filled circle already
def fillSum():
    pieces = [0,1,2,3,4,5]
    double_pieces = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,0]]
    boards = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
    pts = 0
    x = True
    while(x):
        piece = 0
        ran = randint(0, 5)
        z = [[sum(boards[0]),0],[sum(boards[1]),1],[sum(boards[2]),2],[sum(boards[3]), 3]]
        z.sort(key = lambda x: x[0], reverse=True) #sums each circle's point total, and sorts by points
        if (ran == 0):
            piece = double_pieces[ran]
            a = piece[0]
            b = piece[1]
            if(boards[z[0][1]][a] == 0 & boards[z[0][1]][b] == 0):
                boards[z[0][1]][a] = 1
                boards[z[0][1]][b] = 1
                pts+=2
            elif(boards[z[1][1]][a] == 0 & boards[z[1][1]][b] == 0):
                boards[z[1][1]][a] = 1
                boards[z[1][1]][b] = 1
                pts+=2
            elif(boards[z[2][1]][a] == 0 & boards[z[2][1]][b] == 0):
                boards[z[2][1]][a] = 1
                boards[z[2][1]][b] = 1
                pts+=2
            elif(boards[z[3][1]][a] == 0 & boards[z[3][1]][b] == 0):
                boards[z[3][1]][a] = 1
                boards[z[3][1]][b] = 1
                pts+=2
            else:
                x = False
        else:
            a = pieces[ran]
            if(boards[z[0][1]][a] == 0):
                boards[z[0][1]][a] = 1
                pts+=1
            elif(boards[z[1][1]][a] == 0):
                boards[z[1][1]][a] = 1
                pts+=1
            elif(boards[z[2][1]][a] == 0):
                boards[z[2][1]][a] = 1
                pts+=1
            elif(boards[z[3][1]][a] == 0):
                boards[z[3][1]][a] = 1
                pts+=1
            else:
                x = False

            for u in range(4): 
                it = 0
                it_o = 0
                if(boards[u][0] == 1 & boards[u][1] == 1 & boards[u][2] == 1 & 
                   boards[u][3] == 1 & boards[u][4] == 1 & boards[u][5] == 1): 
                    if (u == 3): #checks which circles are full, and if any 'explodes' the circle and two adjacent
                        it = 2 #extra points given for filling circles per game's rules
                        it_o = 0
                    elif (u == 0):
                        it = 1
                        it_o = 3
                    else:
                        it = u -1
                        it_o = u+1
                    pts += 6
                    temp_pts = sum(boards[it]) + sum(boards[it_o])
                    pts+= temp_pts
                    for c in range(6):
                        boards[u][c] = 0
                        boards[it][c] = 0
                        boards[it_o][c] = 0
    return pts

def fillTotSum(): #checks to fill the circle with the most adjacent points
    pieces = [0,1,2,3,4,5]
    double_pieces = [[0,1], [1,2], [2,3], [3,4], [4,5], [5,0]]
    boards = [[0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]]
    pts = 0
    x = True
    while(x):
        piece = 0
        ran = randint(0, 5)
        z = [[(sum(boards[0]) + sum(boards[1]) + sum(boards[3])),0],[(sum(boards[0]) + sum(boards[1]) + sum(boards[2])),1],[(sum(boards[2]) + sum(boards[1]) + sum(boards[3])),2],[(sum(boards[3]) + sum(boards[2]) + sum(boards[0])), 3]]
        z.sort(key = lambda x: x[0], reverse=True)
        if (ran == 0):
            piece = double_pieces[ran]
            a = piece[0]
            b = piece[1]
            if(boards[z[0][1]][a] == 0 & boards[z[0][1]][b] == 0):
                boards[z[0][1]][a] = 1
                boards[z[0][1]][b] = 1
                pts+=2
            elif(boards[z[1][1]][a] == 0 & boards[z[1][1]][b] == 0):
                boards[z[1][1]][a] = 1
                boards[z[1][1]][b] = 1
                pts+=2
            elif(boards[z[2][1]][a] == 0 & boards[z[2][1]][b] == 0):
                boards[z[2][1]][a] = 1
                boards[z[2][1]][b] = 1
                pts+=2
            elif(boards[z[3][1]][a] == 0 & boards[z[3][1]][b] == 0):
                boards[z[3][1]][a] = 1
                boards[z[3][1]][b] = 1
                pts+=2
            else:
                x = False
        else:
            a = pieces[ran]
            if(boards[z[0][1]][a] == 0):
                boards[z[0][1]][a] = 1
                pts+=1
            elif(boards[z[1][1]][a] == 0):
                boards[z[1][1]][a] = 1
                pts+=1
            elif(boards[z[2][1]][a] == 0):
                boards[z[2][1]][a] = 1
                pts+=1
            elif(boards[z[3][1]][a] == 0):
                boards[z[3][1]][a] = 1
                pts+=1
            else:
                x = False

            for u in range(4): 
                it = 0
                it_o = 0
                if(boards[u][0] == 1 & boards[u][1] == 1 & boards[u][2] == 1 & 
                   boards[u][3] == 1 & boards[u][4] == 1 & boards[u][5] == 1):
                    if (u == 3):
                        it = 2
                        it_o = 0
                    elif (u == 0):
                        it = 1
                        it_o = 3
                    else:
                        it = u -1
                        it_o = u+1
                    pts += 6
                    temp_pts = sum(boards[it]) + sum(boards[it_o])
                    pts+= temp_pts
                    for c in range(6):
                        boards[u][c] = 0
                        boards[it][c] = 0
                        boards[it_o][c] = 0
    return pts

#creates a list of averages for each method, plots as a histogram and performs a t-test
def getResults(n):
    tot = 0
    num = n
    avgFirst = []
    avgSum = []
    avgTotSum = []
    totTwo = 0
    totThree = 0
    for y in range(num):
        tot = 0
        totTwo = 0
        totThree = 0
        for x in range(num):
            tot += fillFirst()
            totTwo += fillSum()
            totThree += fillSum()
        avgSum.append(totTwo/num)
        avgFirst.append(tot/num)
        avgTotSum.append(totThree/num)
    bins = numpy.linspace(20, 60, 100)
    pyplot.hist(avgFirst, bins, alpha=0.5, label='first')
    pyplot.hist(avgSum, bins, alpha=0.5, label='sum')
    pyplot.hist(avgTotSum, bins, alpha=0.5, label='adj-sum')
    pyplot.legend(loc='upper right')
    pyplot.show()
    t, p = ttest_ind(avgFirst, avgSum, equal_var=False)
    print('ttest t = ', t)
    print('ttest p = ', p)
getResults(200)
