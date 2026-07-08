now_money=int(input())
b=float(input())
c=int(input())
for rs in range(c):
    now_money=now_money*(1+b/1200)
    print(f"{rs+1},{now_money:.2f}")