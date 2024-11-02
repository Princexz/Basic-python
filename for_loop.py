# using for loop in python
# syntax: for i in range(start,stop,increment)
# start and increment are optional parameters
# by default start=0 and increment=1 if not mentioned

def main():
  for i in range(11): # start=0 stop=11 increment=1
      print(i,end=' ')
  print()
  for j in range(1,11): # start=1 stop=11 increment=1
      print(j,end=' ')
  print()
  for k in range(1,11,2): # start=1 stop=11 increment=2
      print(k,end=' ')
  print()
main()
