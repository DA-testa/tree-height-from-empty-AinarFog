# python3
def right(n,l,a):
  ind=[-1]
  for i in range(a):
    if(i>n):
      if (l[i] not in ind):
        ind.append(l[i])
  return (len(ind))
  
def left(n,l):
  ind=[-1]
  for i in range(n+1):
    if (l[i] not in ind):
      ind.append(l[i])
  return (len(ind))
  
def main():
  amount=int(input())
  nr=0
  if (amount>0):
    list=[]
    for i in range(amount):
      n=int(input())
      if(n==-1):
        nr=i
      list.append(n)
    if(right(nr,list,amount)>left(nr,list)):
      print(right(nr,list,amount))
    else:
      print(left(nr,list))
q1=input()
q1=input()
if(q1=='I'):
  main()
