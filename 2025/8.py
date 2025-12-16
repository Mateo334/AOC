with open("input.txt",'r') as file:
    points  = [ list(map(int, x.split(","))) for x in file.readlines()]
    
import math
import heapq
heap = []
N = 7883 #Second - binary manual search 
# N = 29 #First
for i, point in enumerate(points):
    for j in range(i+1, len(points)):
        d = math.dist(point, points[j])
        if(len(heap)<N):
            heapq.heappush(heap, (-d, i,j))
        else:
            if(d<-heap[0][0]):
                heapq.heapreplace(heap, (-d,i,j))
dists = sorted([(-d, points[i], points[j]) for d, i, j in heap],
            key=lambda x: x[0])    
print(dists[-1])
print(dists[-1][1][0])
print(dists[-1][2][0])
print(dists[-1][1][0]*dists[-1][2][0])

ls_of_lights = [set(tuple(p) for p in dists.pop(0)[1:])]
# print("Lights: ", ls_of_lights)
for pair in dists:
    p, q = tuple(pair[1]), tuple(pair[2])
    ind = []
    for id, sublist in enumerate(ls_of_lights):
        if p in sublist or q in sublist:
            sublist.update([p, q])
            ind.append(id)

    if ind:
        first_id = ind[0]
        first_set = ls_of_lights[first_id]
        for id in sorted(ind[1:], reverse=True):
            first_set.update(ls_of_lights[id])
            del ls_of_lights[id]
    else:
        ls_of_lights.append({p, q})

            
# print("Lights: ", ls_of_lights)
ll = sorted([len(l) for l in ls_of_lights], reverse=True)
print(ll)
