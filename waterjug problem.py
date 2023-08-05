from collections import defaultdict
jug1,jug2,aim=4,3,2
visited=defaultdict(lambda:False)
def WJS(a1,a2):
    if(a1==aim and a2==0) or (a2==aim and a1==0):
        print(a1,a2)
        return True
    if visited[(a1,a2)]==False:
        print(a1,a2)
        visited[(a1,a2)]=True
        return (WJS(a1,0) or
                WJS(0,a2) or
                WJS(a1,jug2) or
                WJS(jug1,a2) or
                WJS(a1+min(a2,jug1-a1),a2-min(a2,jug1-a1)) or
                WJS(a1-min(a1,jug2-a2),a2+min(a1,jug2-a2)))
    else:
        return False
print("STEPS:")
WJS(0,0)
