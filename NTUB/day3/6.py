n=int(input())
s=[]
for i in range(n):
    a ,b , c =input().split()
    a=int(a)
    b=int(b)
    #print(eval("{}{}{}".format(a,c,b)))
    if c=="+":
        s.append(str(a+b))
    elif c=="-":
        s.append(str(a-b))
    elif c=="*": 
        s.append(str(a*b))
    elif c=="/":
        s.append(str(a/b))
    else:
        s.append(c)
#print(s)            
#"".join(s)
print("\n".join(s))