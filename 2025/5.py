with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]
vegs = lines[lines.index("")+1:]
dep = lines[:lines.index("")]
vegs = [int(x) for x in vegs]
cnt=0
# print(lines,dep, vegs)

# for v in vegs:
#     for el in dep:
#         x, y = map(int, el.split("-"))
#         if(v>=x and v<=y):
#             cnt+=1
#             break
# print(cnt)

def find_dep(inter, flag, x, y):
    should_break = 0
    inter[i] = list(inter[i])
    if(x<=inter[i][0] and y>=inter[i][1]):
        inter[i] = x, y
        flag = 1
        should_break =1 
    if(x<=inter[i][1] and x>=inter[i][0] and y>inter[i][1]):
        # print(inter[i])
        inter[i][1] = y
        flag = 1
    if(y<=inter[i][1] and y>=inter[i][0] and x<inter[i][0]):                
        inter[i][0] = x
        flag = 1
    if(flag):
        should_break = 1
    return inter, flag, should_break
inter = []
for d in dep:
    if(not inter):
        inter.append(list(map(int, d.split("-"))))
    else:
        x, y = map(int, d.split("-"))
        flag = 0
        for i in range(len(inter)):
            # print(list(inter[i]))
            inter, flag, sh = find_dep(inter, flag, x, y)
            if(sh):
                break
        if(not flag):
            inter.append([x, y])
# print(inter)



for j in range(len(inter)):
    for i in range(len(inter)):
        flag = 0
        if(i!=j):
            x, y = inter[j][0], inter[j][1]
            inter, flag, sh = find_dep(inter, flag, x, y)
            if(flag):
                inter[j] = [0,0]
                # print(i,j,"these", x, y)
        if(sh):
            break
        
inter = [u for u in inter if u!=[0,0]]
cnt = 0
for el in inter:
    cnt+=el[1]-el[0]+1
                
print(cnt)