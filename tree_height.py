# python3
def right(n,l):
  ind=[]
  for i in range(n):
    if(i>n):
      if (l[i] not in ind):
        ind.append(l[i])
  return len(ind)

  
def left(n,l):
  ind=[]
  for i in range(n):
    if (l[i] not in ind):
      ind.append(l[i])
  return len(ind)
  
def main():
  amount=int(input())
  nr=0
  if (amount>0 and amount<106):
    for i in range(amount):
      n=int(input())
      if(n==-1):
        nr=i
      list.append(n)
    if(right(nr,list)>=left(nr,list)):
      print(right(nr,list))
    else:
      print(left(nr,list))
main()
