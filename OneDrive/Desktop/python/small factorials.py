'''def small_factorials(n: int)-> int:
    for p in range(n):
        num = int(input())
        fact = 1
        while num>0:
            fact=fact*num
            num=num-1
        print(fact)

print(small_factorials(int(input())))'''

def factorials(n: int)->int():
    i=1
    while i<n:
        ans=n*(n-1)
        i+=1
    print(ans)
print(factorials(int(input())))
        
 
