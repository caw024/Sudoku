#!/usr/bin/python3
import sys
import time

#ctr tells you first occurence of '_'
def check(puzzle,ctr):
  Cliques=[[0,1,2,3,4,5,6,7,8],\
  [9,10,11,12,13,14,15,16,17],\
  [18,19,20,21,22,23,24,25,26],\
  [27,28,29,30,31,32,33,34,35],\
  [36,37,38,39,40,41,42,43,44],\
  [45,46,47,48,49,50,51,52,53],\
  [54,55,56,57,58,59,60,61,62],\
  [63,64,65,66,67,68,69,70,71],\
  [72,73,74,75,76,77,78,79,80],\
  [0,9,18,27,36,45,54,63,72],\
  [1,10,19,28,37,46,55,64,73],\
  [2,11,20,29,38,47,56,65,74],\
  [3,12,21,30,39,48,57,66,75],\
  [4,13,22,31,40,49,58,67,76],\
  [5,14,23,32,41,50,59,68,77],\
  [6,15,24,33,42,51,60,69,78],\
  [7,16,25,34,43,52,61,70,79],\
  [8,17,26,35,44,53,62,71,80],\
  [0,1,2,9,10,11,18,19,20],\
  [3,4,5,12,13,14,21,22,23],\
  [6,7,8,15,16,17,24,25,26],\
  [27,28,29,36,37,38,45,46,47],\
  [30,31,32,39,40,41,48,49,50],\
  [33,34,35,42,43,44,51,52,53],\
  [54,55,56,63,64,65,72,73,74],\
  [57,58,59,66,67,68,75,76,77],\
  [60,61,62,69,70,71,78,79,80]\
  ]
  
  badplaces = {0}
  badnums = {0}
  badplaces.remove(0)
  badnums.remove(0)

  #badplaces gives locations where ctr is part of the same clique
  for k in Cliques:
    if ctr in k:
      for places in k:
        if places != ctr:
          badplaces.add(places)
          
  #gives all badnums based on bad places in puzzle
  for a in badplaces:
    if puzzle[a] != '_':
      badnums.add(puzzle[a])
  possible = {'1','2','3','4','5','6','7','8','9'}
  return possible.difference(badnums)


def retSudoku(puzzle):
  ctr = 0
  retstr = ""
  while ctr < 75:
    retstr += ",".join(puzzle[ctr:ctr+9]) + "\n"
    ctr += 9
  return retstr

  
def Sudoku(stack):
  #make a stack to check if state is good or bad
  #if no possibilities, pop stack and check next
  STATE = 'find_next_cell'
  goodset = 0
  backtrack = 0
  cell = 0
  while True:
    #gets current puzzle
    currentpuzzle = stack[len(stack)-1]
    #shouldn't change everytime
    goodset = check(currentpuzzle,cell)
    
    if STATE == "find_next_cell":
      #gets first occurence of _
      cell = 0
      while cell < 81 and currentpuzzle[cell] != '_':
        cell += 1
        #return boolean and associated puzzle
      if cell == 81:
        return retSudoku(currentpuzzle)

      STATE = 'new_cell'
      continue
      #if set is 0, del possibility, Sudoku keeps moving on with possibilities

    if STATE == "new_cell":
      #gets set of possibilities
      if len(goodset) == 0:
        STATE = 'backtrac'
      else:
        #adds to stack
        guessval = goodset.pop()
        newpuzzle = currentpuzzle[:cell] + [guessval] + currentpuzzle[cell+1:]
        tempstack = stack[:]
        tempstack.append(newpuzzle)
        STATE = 'find_next_cell'
      continue

    if STATE == "backtrac":
      #bad values, go back + remove
      backtrack += 1
      del stack[len(stack)-1]
      STATE = 'find_next_cell'
      continue
        

def main():
  Process(sys.argv[1])
  
def Process(infile):
  f = open(infile,'r')
  lines = f.read().split('\n')
  f.close()
  board = []
  stop = 0
  retstr = ""
  for i in lines:
    ctr = i.split(',')
    if stop == 9:
      start = time.time()
      retstr += Sudoku( [board] )
      totaltime = time.time()-start
      #print("totaltime: " + str(totaltime) + " seconds")
      #print("\n*******************************\n")
    if len(ctr) < 2:
      global backtrack
      backtrack = 0
      stop = 0
      board = []
    elif len(ctr) == 3:
      retstr += ",".join(ctr) + "\n"
    elif len(ctr) == 9:
      board.extend(ctr)
      stop += 1
  print(retstr)
  return retstr

main()