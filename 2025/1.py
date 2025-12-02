with open("din.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]
base = 50
cnt = 0
prev_base = 0
for line in lines:
    print(line,base, cnt)
    if(line[0] == "R"):
        base+=int(line[1:])
        cnt+=base//100
        base%=100
    else:
        base-=int(line[1:])
        cnt+=abs(base)//100
        if(base<0):
            base = 100 - abs(base)%100
        # base = -abs(base)//100
        # while(base<0):
        #     base+=100
        #     cnt+=1
    # if(base==0):
    #     cnt+=1
    if(cnt>10):
        break
print(cnt)
        # cnt+=base//100
        
    
    
#     print(line, base, cnt)
#     # if(cnt>10):break
#     # if(base==0):
#     #     cnt-=1
#     if(line[0] == "R"):
#         base+=int(line[1:])
#         while(base>=100):
#             cnt+=1
#             base-=100
#     else:
#         base-=int(line[1:])
#         while(base<0):
#             cnt+=1
#             base += 100
#     if(prev_base):
#         cnt-=1
#     if(base==0):
#         prev_base = 1
#     else:
#         prev_base = 0
#     #    cnt+=1
# print(cnt)