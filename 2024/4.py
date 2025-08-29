import os
import re
import numpy as np
os.chdir('C:/Users/matej/OneDrive/Desktop/Statistical methods/AOC')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
filename = "data.txt"
filename = "startdata.txt"
u = 0
with open(filename) as f:
    cont = "".join(f.readlines())
with open(filename) as f:
    for line in f:
        u+=1
cont = re.sub(r'\n', r';', cont)
rows = cont.split(';')
matrix = [list(row) for row in rows]
cnt = 0
def find_xmas(strung):
    a = 0
    a+=len(re.findall("SAMX", strung))
    a+=len(re.findall("XMAS", strung))
    return a
    

length = len(matrix[0])
lower_diag = []
upper_diag = [] #w/o main diag
rev_upper_diag = []
rev_lower_diag = []
for i in range(length):
    
    cnt+=find_xmas("".join(matrix[i])) #row-wise search
    cnt+=find_xmas("".join(matrix[j][i] for j in range(len(matrix)))) #column-wise search
    for j in range(length):
        if(length-1-j-i>=0):
            rev_upper_diag += matrix[j][length-1-j-i]
        if(length-j-1>=0 and i>0):#nechci aby se opakovala hlavni diagonala
            rev_lower_diag += matrix[j+i][length-j-1]
        lower_diag += matrix[i+j][j]
        if(i>0): #nechci aby se opakovala hlavni diagonala
            upper_diag += matrix[j][i+j]
        if(i+j+1>=length):
            cnt+=find_xmas("".join(upper_diag))
            cnt+=find_xmas("".join(lower_diag))
            cnt+=find_xmas("".join(rev_lower_diag))
            cnt+=find_xmas("".join(rev_upper_diag))
            # print("".join(upper_diag), len(upper_diag))
            # print("".join(rev_lower_diag), len(rev_lower_diag))
            # print("".join(rev_upper_diag), len(rev_upper_diag))
            # print("".join(lower_diag), len(lower_diag))
            lower_diag = []
            upper_diag = []
            rev_upper_diag = []
            rev_lower_diag = []
            break
        
        
    
print(cnt)


        
        