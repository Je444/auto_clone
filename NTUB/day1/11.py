a=(input())#i am
s=1
index=-1
if a[0]!="英文字母":
    s=0
if 5<=len(a)<=20:
     #good
     pass
else:
     #bad
     s=0

for i in a:
    if i=="英文字母" or i=="數字":
        #good
        pass
    else:
        s=0
        break
      #"i am"=="英文" 並且 "i am"=="數字"    
print(s)