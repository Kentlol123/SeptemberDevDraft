from sets import Set

def main():
# format input to the problem into a series of lists.
  n=raw_input().split()
  for i in range(0,len(n)):
    n[i]=int(n[i])

  blocks=raw_input().split()
  for i in range(0,len(blocks)):
    blocks[i]=int(blocks[i])

  patrols=raw_input().split()
  for i in range(0,len(patrols)):
    patrols[i]=int(patrols[i])
  
  patrol_distances=[]
  for elmnt in patrols[::2]:
    patrol_distances.append(elmnt)
  
  num_patrols=[]
  for elmnt in patrols[1::2]:
    num_patrols.append(elmnt)

  #print blocks
  #print patrols
  #print patrol_distances
  #print num_patrols

  total=sum(blocks)
  outer_index=max_sum=overall_sum=0
  remove=Set()
  current=Set()
  while outer_index<len(patrol_distances):
#    for index in range(0,(len(blocks)-len(patrol_distances))):
    patrol_counter = 0;
    while patrol_counter<num_patrols[outer_index]:
      for index in range(0,(len(blocks)-patrol_distances[outer_index])):
        current_sum=0
        for inner_index in range(0,patrol_distances[outer_index]):
          current_sum+=blocks[(inner_index + index)]
          current.add((inner_index+index))
        if current_sum > max_sum:
          remove.clear()
          max_sum = current_sum
          for elmnt in current:
            remove.add(elmnt)
          current.clear()
        else:
          current.clear()
          continue
      overall_sum+=max_sum
      #print blocks
      #print remove
      for thing in remove: #error list index out of range, added append to the blocks with value 0
        #print thing
        del(blocks[thing])
        blocks.append(0)
        #print blocks
      max_sum=0
      patrol_counter+=1
    outer_index+=1

  total=total-overall_sum
  if total < 0:
    total+=sum(blocks)

  print total   
  #print max_sum
  #print remove
  #print current
  #print blocks
     
if __name__ == "__main__":
  main()