import os
import re
os.chdir('C:/Users/matej/OneDrive/Desktop/Statistical methods/AOC')
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)
# filename = "data.txt"
filename = "startdata.txt"
with open(filename) as f:
    cnt = 0
    rem = 0
    for line in f.readlines():
        x = [int(el.rstrip()) for el in line.split(" ")]
        print(x)
        if((x!=sorted(x)) and (x[::-1] !=sorted(x[::-1]))):
            print("This level is not safe because of ordering")
            continue
        if(len(set(x))!=len(x)):
            print("This level is not safe because same elements")
            continue
        if(x!=sorted(x)):
            x = x[::-1]
        for i in range(len(x)-1):
            if(abs(int(x[i])-int(x[i+1]))>3):
                print("Not safe because of distance")
                break
            if(i==len(x)-2):
                cnt+=1
print(cnt)
    

        
        