# cook your dish here
t=int(input())
for i in range(t):
    a,b,x,y=map(int,input().split())
    if a/x<b/y:
        print("Chef")
    elif a/x==b/y:
        print("Both")
    else:
        print("Chefina")
