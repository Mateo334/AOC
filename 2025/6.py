# with open('din.txt', 'r') as f:
#     nums = f.readlines()
# import math
# nums = [x.strip() for x in nums]
# ops = nums[-1].split()
# # nums = [n.split() for n in nums]
# n = len(nums[0].split())
# ls = [int(x.split()[i]) for x in nums[:-1] for i in range(n)]
# ls = [[ls[i] for i in range(len(ls)) if i % n == j] for j in range(n)]
# cnt = 0
# for i,op in enumerate(ops):
#     if(op=='*'):
#         cnt+=math.prod(ls[i])
#     else:
#         cnt+=sum(ls[i])
# print(cnt)



import re
empty_col = []
with open('input.txt', 'r') as f:
    nums = f.readlines()
with open('input.txt', 'r') as f:
    xx = f.readlines()[:-1]
    num_max = []
    for i in range(4):
        num_max.append(xx[i].split())
    num_max = [len(str(max(int(x) for x in col))) for col in zip(*num_max)]
    # print(num_max[:10])

ops = nums[-1].split()
nums = nums[:-1]
empty_lines = []
for line in nums:
    empty_lines.append([m.start() for m in re.finditer(r'\s', line)])
# print(empty_lines, line)
col_ind = empty_lines[0]
for l in empty_lines:
    col_ind = sorted(list(set(l)&set(col_ind)))
for j,el in enumerate(nums):
    nums[j] = list(nums[j])
    for i in range(len(el)):
        if(i in col_ind):
            continue
        elif(nums[j][i]==' '):
            nums[j][i] = 'p'
for i in range(len(nums)):
    nums[i] = "".join(nums[i]).strip()
nums = " ".join(nums).split()


n = len(col_ind)
# print(col_ind)
nums = [[nums[i] for i in range(len(nums)) if i % n == j] for j in range(n)]
lls =[]
for i,col in enumerate(nums):
    ln = len(nums[i][0])
    for j in range(ln-1, -1, -1):
        dm = []
        for c in col:
            # print(c)
            dm.append(c[j])
        x = int("".join(dm).replace("p", ""))
        lls.append(x)
print(num_max[:10])
cnt=0  
import math
start = 0
for i,op in enumerate(ops):
    n = num_max[i]
    print(lls[start:start+n],n, op)
    if(op=='*'):
        cnt+=math.prod(lls[start:start+n])
    else:
        cnt+=sum(lls[start:start+n])
    start += n
print(cnt)  
