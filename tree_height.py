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
  q2=str(input())
  e="test/"+q2
  if ("a" not in e):
    with open(e) as t:
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
if 'I' in q1:
  main1()
elif 'F' in q1:
  main2()
