def Solve(ban,box,hei,mon,hold):
    if(mon==ban and hei==1):
        ans.append("Monkey took banana")
        found=1
        return True
    if (ban,box,hei,mon,hold) in d:
        return False
    found=0
    d[(ban,box,hei,mon,hold)]=1
    options={1:"move to the box",2:"move to the banana",
             3:"climb onto the box",4:"hold box to move"}
    for op in options:
        if(op==1 and hei==0 and hold==0 and Solve(ban,box,hei,box,hold)):
            ans.append(options[op])
            found=1
            break
        elif(op==2 and hei==0 and (hold==1 and Solve(ban,ban,hei,ban,hold)) or
             (hold==0 and Solve(ban,box,mon,ban,hold))):
            ans.append(options[op])
            found=1
            break
        elif(op==3 and hei==0 and mon==box and Solve(ban,box,hei+1,mon,0)):
            ans.append(options[op])
            found=1
            break
        elif(op==4 and hei==0 and mon==box and Solve(ban,box,hei,mon,1)):
            ans.append(options[op])
            found=1
            break
    return found
n=int(input("Enter the size of world"))
world=[[0]*n for i in range(n)]
x,y=map(int,input("Enter tree position").split())
world[x][y]=1
x,y=map(int,input("ENter box positon").split())
world[x][y]=-1
x,y=map(int,input("Enter monkey position").split())
for i in range(n):
    for j in range(n):
        if(world[i][j]==1):
            print(f"monkey found the banana tree at ({i},{j})")
            ban=(i,j)
        if(world[i][j]==-1):
            print(f"box found at ({i},{j})")
            box=(i,j)
d={}
ans=[]
Solve(ban,box,0,(x,y),0)
ans.reverse()
print(*ans,sep="\n")
             

