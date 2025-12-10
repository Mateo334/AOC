with open('input.txt', 'r') as f:
    mat = [list(row.strip()) for row in f.readlines()]
    
cur_line = [0 for i in range(len(mat[0]))]

s = mat[0].index('S')

cur_line[s] = '|'
next_line = ['0' for i in range(len(mat[0]))]
cnt=0

# for i in range(1,len(mat)):
#     # cur_line = next_line
#     next_line = ['0' for i in range(len(mat[0]))]
#     for j in range(len(cur_line)):
#         # print(mat[i][j])
#         if(cur_line[j]=='|'):
#             if(mat[i][j]=='^'):
#                 # print("here")
#                 cnt+=1
#                 next_line[j-1] = '|'
#                 # cnt+=1
#                 next_line[j+1] = '|'
#             else:
#                 next_line[j]='|'
#         # print(next_line)
#     cur_line = next_line
                # mat[i][j-1]='|'
# print(cur_line,s, cnt)




# mem = {'^':1}#dic of possibilities
def find_hits(i,j):
    global mat
    """Finds the hits from the (i,j)th elements downwards."""
    # print(mat[j:])
    for x, row in enumerate(mat):
        if(row[i]=='^' and x>=j):
            # print(row, x)
            return x    
    return None

graph = {}
not_visited = []
start = (mat[:][0].index('S'), 0)
graph[mat[:][0].index('S'), 0] = [(mat[:][0].index('S'),find_hits(mat[:][0].index('S'),0))]
not_visited.append((mat[:][0].index('S'),find_hits(mat[:][0].index('S'),0)))
visited = []
cnt = 0
all_paths = []
mem ={}
total = 0
def dfs(next): #Need memoization
    if(next in mem):
        return mem[next]
    if (next == (0,0)):
        mem[next] = 1
        return 1
        
    elif not graph[next]:
        mem[next] = 2
        return 2
    total = 0
    for node in graph[next]:
        total +=dfs(node)
    mem[next] = total
    return total


while(not_visited):
    i,j = not_visited.pop() #x and y pos of the node we want to track
    graph[(i,j)] = []
    if([i,j] in visited):
        if(i>0):
            x = find_hits(i-1,j)
            if x is not None:
                graph[(i,j)].append((i-1, x))
            else:
                graph[(i,j)].append((0,0))
        if(i<len(mat[:][0])):
            x = find_hits(i+1,j)
            if x is not None:
                graph[(i,j)].append((i+1, x))
            else:
                graph[(i,j)].append((0,0))
        continue
    visited.append([i,j])
    
    if(i>0):
        x = find_hits(i-1,j)
        if x is not None:
            not_visited.append((i-1, x))
            graph[(i,j)].append((i-1, x))
        else:
            graph[(i,j)].append((0,0))
    if(i<len(mat[:][0])):
        x = find_hits(i+1,j)
        if x is not None:
            not_visited.append((i+1, x))
            graph[(i,j)].append((i+1, x))
        else:
            graph[(i,j)].append((0,0))
total = dfs(start)
print(graph)
print(total)
    