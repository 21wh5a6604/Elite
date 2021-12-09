def triplets(p):
    tri=([a,b,c] for a in range(1,p+1)
                 for b in range(1,p+1)
                 for c in range(1,p+1)
                 if (a**2 + b**2 == c**2) and a<b<c)
    return tri
def perimeter(p):
    if p == sum(triplets(p)):
        return triplets(p)
print(perimeter(120))

'''def divide(p: int)->{}:
    l=[[a,b,c] for a in range(1,p+1)
               for b in range(1,p+1)
               for c in range(1,p+1)
               if (a**2 + b**2 == c**2) and (a+b+c == p) and a<b<c]
    return l
print(divide(120))'''


