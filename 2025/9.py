with open("input.txt",'r') as file:
    points  = [ list(map(int, x.split(","))) for x in file.readlines()]