def  StringCompression(text) :
    ans = ""
    res = 0
    for i in range(1,len(text)):
        if text[i] !=  text[i-1]:
            ans += text[i-1]+str(res+1)
            res = 0
        else :
            res +=1 
    ans += text[i-1]+str(res+1)    
    print(res)
    if len(ans) <=  len(text):
        return ans
    return text
print(StringCompression("aabcccccaaa"))