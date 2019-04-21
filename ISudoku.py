#!/usr/bin/python3
#results of timing + backtrack: naive and smarter
import sys
import time

#from hardest: 0.76139,37.964589,284.629255

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
  
  badplaces = []
  badnums = []

  #O(n^2) time (is it possible to reduce it?)
  #badplaces gives locations where ctr is part of the same clique
  for k in Cliques:
    if ctr in k:
      for places in k:
        if places != ctr:
          badplaces.append(places)
          
  #gives all badnums based on bad places in puzzle
  for a in badplaces:
    if puzzle[a] != '_':
      badnums.append(puzzle[a])
  possible = ['1','2','3','4','5','6','7','8','9']
  return [nums for nums in possible if nums not in badnums]


def retSudoku(puzzle):
  ctr = 0
  retstr = ""
  while ctr < 75:
    #print( ",".join(puzzle[ctr:ctr+9]) )
    retstr += ",".join(puzzle[ctr:ctr+9]) + "\n"
    ctr += 9
  return retstr

NEW_CELL = 0
FIND_NEXT_CELL = 1
BACKTRAC = 2

def Sudoku(board):
  #make a stack to check if state is good or bad
  #if no possibilities, pop stack and check next
  backtrack = 0
  stack = []
  stack.append([board,[0],-1])
  state = NEW_CELL
  visitedctr = []
  case = 0
    
  #gets current puzzle
  while True:
    currentpuzzle = stack[len(stack)-1][0]

    if state == NEW_CELL:
      #print("new cell puzzle:\n" + retSudoku(currentpuzzle))
      ctr = 0
      #gets first occurence of _
      while ctr < 81 and currentpuzzle[ctr] != '_':
        ctr += 1
        
      #return boolean and associated puzzle
      if ctr == 81:
        #global finalstr
        #finalstr += retSudoku(currentpuzzle)
        #print(retSudoku(currentpuzzle))
        print("number of backtracks: " + str(backtrack))
        break

      #print("ctr: " + str(ctr))
      for k in visitedctr:
        if k > ctr:
          visitedctr.remove(k)
      #print("visited ctr:")
      #print(visitedctr)
      if ctr in visitedctr:
        goodlist = stack[len(stack)-1][1]
      else:
        visitedctr.append(ctr)
        case = 1
        goodlist = check(currentpuzzle,ctr)
        
      if len(goodlist) == 0:
        #print("starting backtrack")
        if case == 1:
          visitedctr.remove(ctr)
        state = BACKTRAC
      else:
        case = 0
        #print("goodlist before deletion")
        #print(goodlist)
        k = goodlist[0]
        del goodlist[0]
        #print(goodlist)
        newpuzzle = currentpuzzle[:ctr] + [k] + currentpuzzle[ctr+1:]
        #print("new puzzle:\n" + retSudoku(newpuzzle))
        stack.append([newpuzzle,goodlist,ctr])
      continue
  
    if state == BACKTRAC:
      while len( stack[len(stack)-1][1] ) == 0:
        backtrack += 1
        visitedctr.remove(stack[len(stack)-1][2])
        del stack[len(stack)-1]
        #print("backtracking puzzle:\n" + retSudoku(stack[len(stack)-1][0]))
        #print("previous goodlist")
        #print(stack[len(stack)-1][1])
        #print("visited ctr:")
        #print(visitedctr)

      pastworkingpuzzle = stack[len(stack)-1][0][:]
      goodlist = stack[len(stack)-1][1][:]
      pastctr = stack[len(stack)-1][2]
      #print("goodlist before deletion")
      #print(goodlist)
      k = goodlist[0]
      del goodlist[0]
      newpuzzle = pastworkingpuzzle[:pastctr] + [k] + pastworkingpuzzle[pastctr+1:]
      del stack[len(stack)-1]
      stack.append([newpuzzle,goodlist,pastctr])
      #print("ending backtrack")

      #print(backtrack)
      state = NEW_CELL
      continue
  return retSudoku(currentpuzzle)


      #you have to store (i) current working board, (ii) keep adding and removing to state per guess, (iii) keeping track of which ctr is last usable + guesses of it
      #idea: iterate through board and get pos of all "_"
      #from the _ you are on, keep track of what guesses are available and remove guesses one at time
      #if no guesses work, delete state and go back to modify value

def main():
  Process(sys.argv[1], sys.argv[2])
  
def Process(infile,outfile):
  f = open(infile,'r')
  lines = f.read().split('\n')
  f.close()
  #text = text.split(',')

  board = []
  stop = 0
  retstr = ""
  
  for i in lines:
    ctr = i.split(',')
    if stop == 9:
      start = time.time()
      print( Sudoku( board ) )
      #retstr += Sudoku(board)
      skip = 0
      #retstr += str(backtrack)+  "\n"

      totaltime = time.time()-start
    
      print("totaltime: " + str(totaltime) + " seconds" + "\n*******************************\n")
      #retstr += "totaltime: " + str(totaltime) + " seconds" + "\n*******************************\n"
      stop = 0
      board = []
    elif len(ctr) == 3:
      #if ctr == text:
       # skip = 3
      print(",".join(ctr))
      #retstr += ",".join(ctr) + "\n"
    elif len(ctr) == 9:
      board.extend(ctr)
      stop += 1
  
  #g = open(outfile,'w')
  #g.write(retstr)
  #g.close()

main()
