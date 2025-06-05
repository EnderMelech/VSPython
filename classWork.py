# import math

# # function that calculated distance between two points
# def distance(p: list[float],q: list[float])-> float:
#     return math.sqrt((p[0]-q[0])**2+(p[-1]-q[-1])**2)
# print(distance([0,0],[3,4]))

# # function that calculates the slope given two points, returns None if vertical
# def slope(p: list[float],q: list[float])-> float:
#     if q[-1]-p[-1]!=0:
#         return (q[-1]-p[-1])/(q[0]-p[0])
#     else:
#         None
# print(slope([4,3],[7,4]))

# function that given an integer, returns either TRUE or FALSE for whether it is prime or not
def prime(int):
    primeOrNot=True
    if int<=1:
        primeOrNot=True
        return primeOrNot
    elif int==2:
        primeOrNot=True
        return primeOrNot
    for i in range(2,int):
        if int%i==0:
            primeOrNot=False
            return primeOrNot
        elif int%int==0:
            primeOrNot=True
            return primeOrNot
int=int(input('What integer would you like today? '))
print (f'The very notion that the integer {int} is prime is obviously {prime(int)}')