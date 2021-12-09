def palindromesOf(str1: str)->str:
    
    output= []
    for i in range(len(str1)):
        for j in range(i+1,len(str1)+1):
            substr = str1[i:j]
            if substr == substr[::-1] and len(substr) != 1:
                output.append(substr)
    return output
print(palindromesOf("aabbbaa"))
print(palindromesOf("repaper"))        
