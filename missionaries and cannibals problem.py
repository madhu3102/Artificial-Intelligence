def is_valid(state):
    if state[0]>3 or state[1]>3 or state[2]>1 or state[0]<0 or state[1]<0 or state[2]<0 or (0<state[0]<state[1]) or (0<(3-state[0])<(3-state[1])):
        return False
    else:
        return True
def gen_next_s(M,C,B):
    valid_states=[]
    moves=[[1,0,1],[0,1,1],[2,0,1],[0,2,1],[1,1,1]]
    for each in moves:
        if(B==1):
            next_s=[x1-x2 for (x1,x2) in zip([M,C,B],each)]
        else:
            next_s=[x1+x2 for (x1,x2) in zip([M,C,B],each)]
        if is_valid(next_s):
            valid_states.append(next_s)
    return valid_states
solutions=[]
def find_sol(M,C,B,visited):
    if [M,C,B]==[0,0,0]:
        solutions.append(visited+[[0,0,0]])
        return True
    elif [M,C,B] in visited:
        return False
    else:
        visited.append([M,C,B])
        if(B==1):
            for each_s in gen_next_s(M,C,B):
                find_sol(each_s[0],each_s[1],each_s[2],visited[:])
        else:
            for each_s in gen_next_s(M,C,B):
                find_sol(each_s[0],each_s[1],each_s[2],visited[:])
find_sol(3,3,1,[])
solutions.sort()
n=1
for each_sol in solutions:
    print("solution:",n)
    print(each_sol,"\n")
    n=n+1
