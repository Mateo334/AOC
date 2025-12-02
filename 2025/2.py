with open("input.txt", 'r') as f:
    lines = [l for l in f.readline().split(",")]
cnt=0
for line in lines:
    a,b =  [int(x) for x in line.split("-")]
    for i in range(a,b+1):
        x = str(i)
        if (x in (x+x)[1:-1]):
            print(x)
            cnt+=i
print(cnt)