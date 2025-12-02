
with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]
base = 50
cnt=0
for line in lines:
    if(line[0] == "R"):
        y= int(line[1:])
        
        cnt+=(base+y)//100
        base = (base+y)%100
    else:
        y = int(line[1:])
        if(base>y):
            base -= y
            continue
        elif(base==y):
            cnt+=1
            base = 0
            continue
        else:
            
            if(base!=0):
                cnt+=1+abs(base-y)//100
            else:
                cnt+=abs(base-y)//100
            base = (100 - abs(base-y)%100)%100
        
    
print(cnt)