import numpy as np
mat = [list(line.strip()) for line in open("input.txt")]

dirs = [    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)]
def trav_mat(i,j):
    c = 0
    for dir in dirs:
        if(i==0 and dir[0]<0):
            continue
        elif(i==len(mat)-1 and dir[0]>0):
            continue
        elif(j==0 and dir[1]<0):
            continue
        elif(j==len(mat)-1 and dir[1]>0):
            continue
        if(mat[i+dir[0]][j+dir[1]]=="@"):
            c+=1
    return True if c<4 else False
        
cnt = 0
for i in range(80):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(mat[i][j]=="@"):
                if(trav_mat(i,j)):
                    mat[i][j]="."
                    cnt+=1
print(cnt)