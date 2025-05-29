import math
# function that calculated distance between two points
def distance(p,q):
    print(math.sqrt(((p[0]-q[0])**2)+((p[-1]-q[-1])**2)))
distance([0,0],[3,4])