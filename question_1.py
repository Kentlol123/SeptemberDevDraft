# your code goes here

import random
from sets import Set
import sys

class workbench:
  def __init__(self,crystal_count,crystal_string):
    self.elmnts=['F','B','Z','R','A','I']
    self.crystal_count=crystal_count
    self.staging_bench = ''
    self.bench=crystal_string
    self.current=Set()
    #self.populate_bench()

  def populate_bench(self):
    for i in range(0,self.crystal_count):
      self.bench+=random.choice(self.elmnts)
      i+=1
    self.bench
    return self.bench

  @property
  def check_condition(self):
    for i in range(0,len(self.bench)):
      if self.bench[i] == 'A' or self.bench[i] == 'I':
        return False
      else:
        pass
    return True

  @property
  def purge(self):
    i=0
    self.current.clear()
    while i in range(0,(len(self.bench)-3)):
      if self.bench[i]=='F' and (self.bench[(i+1):(i+3)]=='IZ'):
        self.current.add(i)
        self.current.add((i+1))
        self.current.add((i+2))
        i+=2

      elif self.bench[i]=='R' and (self.bench[(i+1):(i+3)]=='AB'):
        self.current.add(i)
        self.current.add((i+1))
        self.current.add((i+2))
        i+=2


      elif self.bench[i]=='B' and ((self.bench[(i+1):(i+3)]=='AR') or (self.bench[(i+1):(i+3)]=='AZ')):
        self.current.add(i)
        self.current.add((i+1))
        self.current.add((i+2))
        i+=2

      elif self.bench[i]=='Z' and ((self.bench[(i+1):(i+3)]=='AB') or (self.bench[(i+1):(i+3)]=='IF')):
        self.current.add(i)
        self.current.add((i+1))
        self.current.add((i+2))
        i+=2
      else:
        i+=1
        pass
#    print(self.current)
    self.staging_bench=''
    for index in range(0,len(self.bench)):
       if index not in self.current:
          self.staging_bench+=self.bench[index]
       else:
          continue
    self.bench = self.staging_bench
    return self.bench

  def move_crystal(self, i, j):
    if (j-i)==1 and j<=(len(self.bench)-1): 
      self.bench=''.join((self.bench[:i],self.bench[j],self.bench[i+1:j],self.bench[i],self.bench[j+1:]))
    else:
      print('Not a valid move!')
      i,j = raw_input('input two indices seperated by a space: ').split()
      i = int(i)
      j = int(j)
      self.move_crystal(i,j)


def main():
  n = int(raw_input())
  thing = raw_input()
  playbench=workbench(n,thing)

  playbench.purge

  #print(playbench.bench)
  turns = int(raw_input())
  current_turn = []*turns
  moves = raw_input().split()
#  print moves
  for i in range(0, len(moves)):
    moves[i] = int(moves[i])
  for num in moves:
    playbench.move_crystal(num, (num+1))
    playbench.purge
#  print moves
  print(playbench.bench)
    

#  if playbench.check_condition:
#    print('works')
#  else:
#    print('wut')

if __name__ == "__main__":
	main()