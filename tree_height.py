# python3
def right(n,l,a):
  ind=[-1]
  for i in range(a):
    if(i>n):
      if (l[i] not in ind):
        ind.append(l[i])
  return (len(ind))

def links(l):
  ind=[-1]
  hed=l.index('-1')
  for i in range(hed):
    if(i!=hed):
      if(l[i] not in ind):
        ind.append(l[i])
    else:
      break
  return(len(ind))

def rechts(l):
  ind=[-1]
  hed=l.index('-1')
  for i in range(len(l)):
    if(i>hed):
      if(l[i] not in ind):
        ind.append(l[i])
  return(len(ind))
  
def left(n,l):
  ind=[-1]
  for i in range(n+1):
    if (l[i] not in ind):
      ind.append(l[i])
  return (len(ind))

def main1():
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
      
def main2():
  q2=input("file: ")
  if ("a" not in q2):
    with open(q2) as t:
      data=t.readlines()
      data.pop(0)
      if(len(data)==1):
        a=data[0]
        step=a.split(" ")
    if(rechts(step)>links(step)):
      print(rechts(step))
    else:
      print(links(step))
q1=input()
q1=input("Quest: ")
if(q1=='I'):
  main1()
elif (q1=='F'):
  main2()
