s=[]
#s.appned(a)
#s.pop()

while True:
    a=input()
    if a=="stop":
        break
    else:
        s.append(a)
print(s)   

n=int(input())
for i in range(n):
    a ,b , c =input().split()
    a=int(a)
    b=int(b)
    #print(eval("{}{}{}".format(a,c,b)))
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*": 
        print(a*b)
    elif c=="/":
        print(int(a/b))           
    