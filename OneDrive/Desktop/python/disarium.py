def isDisarium(n: int)->bool:
    length=len(str(n))
    count=0
    result=0
    for i in str(n):
        count+=1
        for j in range(count, length+1):
            result += int(i) ** j
            break
    return result == n
print(isDisarium(175))
print(isDisarium(89))
print(isDisarium(25))
