with open("input.txt", 'r') as f:
    lines = [l.strip() for l in f.readlines()]
cnt = 0
for line in lines:
    cur_ls = []
    ll = [int(x) for x in line]
    for i in range(11,-1, -1):
        if(i!=0):
            to_search = ll[:-i]
        else:
            to_search = ll
        y = to_search.index(max(to_search))
        cur_ls.append(to_search[y])
        ll = ll[y+1:]
    cnt+=int("".join(map(str,cur_ls)))
print(cnt)
