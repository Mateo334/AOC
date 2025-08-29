import os
import re
os.chdir('C:/Users/matej/OneDrive/Desktop/Statistical methods/AOC')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
filename = "startdata.txt"

with open(filename) as f:
    cont = "".join(f.readlines())

x = (re.findall(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", cont))
do = True
cnt = 0
for el in x:
    cur = re.findall(r"\d{1,3},\d{1,3}", el)
    if(cur==[]):
        if(el=="don't()"):
            do = False
        else:
            do = True
        continue
    if(not do):
        continue
    cur = cur[0].split(",")
    cnt += int(cur[0])*int(cur[1]) 
print(cnt)
    

        
        