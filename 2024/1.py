import os
os.chdir('C:/Users/matej/OneDrive/Desktop/Statistical methods/AOC')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
filename = "data.txt"
l1 = []
l2 = []
with open(filename) as f:
    for el in f.readlines():
        l1.append(int(el.split(" ")[0]))
        l2.append(int(el.split(" ")[-1].rstrip()))
cnt = 0
matr = [0]*(max(max(l1), max(l2))+1)
for i in range(max(l2)+1):
    if i in l2:
        matr[i] = l2.count(i)

for el in l1:
    if(matr[el]!=0):
        cnt+=el*matr[el]
# print(cnt)a
        
        