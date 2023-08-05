def TowerOfHanoi(n,from_rod,to_rod,aux_rod):
    if(n==1):
        print("move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1,from_rod,aux_rod,to_rod)
    print("move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1,aux_rod,to_rod,from_rod)
n=int(input("Enter number of disks:"))
TowerOfHanoi(n,'A','C','B')