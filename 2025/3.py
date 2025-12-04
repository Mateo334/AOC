with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]
cnt = 0
# ten list muze jit jen do len(ll)-12-cur_ls, aby to pridalo vzdycky jen ten nejvetsi a mohlo bejt greedy
for line in lines:
    cur_ls = []
    ll = [int(x) for x in line]
    # print(line)
    for i in range(11,-1, -1): #tohle dodela celej cur_ls
        if(i!=0):
            to_search = ll[:-i]
        else:
            # print(ll)
            to_search = ll
        # print(to_search, ll[:-1])
        y = to_search.index(max(to_search))
        # print(y)
        cur_ls.append(to_search[y])
        ll = ll[y+1:]
    cnt+=int("".join(map(str,cur_ls)))
    
    # print(cnt)
    # print(int("".join(map(str,cur_ls))))
print(cnt)
    # usek = len(ll)-12
    # while(len(cur_ls)<n):
    #     cur_max = 0
    #     # ll+curls < 12
    #     for i in range(len(ll)-n+len(cur_ls)):
    #         x = int(ll[i])
    #         if(x>cur_max):
    #             cur_max = x
    #             el = x
    #             ind = i
    #     cur_ls.append(el)
    #     ll = ll[:ind]+ ll[ind+1:]
        # if(len(ll)+len(cur_ls)<4):
        #     cur_ls.append(ll)
        #     break
          
    # print(cur_ls)  
    # 3   
    # 12137
    # 88145
    # 11834
    # cur_line = line
    # while(len(cur_ls)<4):
    #     cur_max = 0
    #     index_rem = []
    #     for el in cur_line:
    #         x = int(el)
    #         if(x>=cur_max):
    #             cur_ls.append(x)
    #             cur_max = x
    #             index_rem.append(cur_line.index(el))
    #     # print(index_rem)
    #     for ind in index_rem:
    #         cur_line = cur_line[:ind] + cur_line[ind+1:]
    
    
# print(lines)