def reversingSentence(str1: str)->str:
    words=str1.split(" ")
    words=words[::-1]
    return " ".join(words)
print(reversingSentence("hello world"))
print(reversingSentence("a quick old fox jumped !"))
