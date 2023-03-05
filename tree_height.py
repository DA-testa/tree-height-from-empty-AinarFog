# python3
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
  
def main1():
  base=input()
  amount=input()
  list=amount.split()
  if(rechts(list)>links(list)):
    print(rechts(list))
  else:
    print(links(list))
      
def main2():
  q2=input()
  if ("a" not in q2):
    with open(q2) as t:
      data=t.readlines()
      data.pop(0)
      if(len(data)==1):
        a=data[0]
        step=a.split(" ")
      else:
        print(data)
        a=" ".join(data)
        a=a.replace("\n","")
        print(a)
        step=a.split(" ")
        print(step)
    if(rechts(step)>links(step)):
      print(rechts(step))
    else:
      print(links(step))
q1=input()
if(q1=='I'):
  main1()
elif (q1=='F'):
  main2()
