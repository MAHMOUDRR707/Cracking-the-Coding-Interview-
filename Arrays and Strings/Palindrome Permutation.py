def  PalindromePermutation(text) :
    res = []
    for i in range(len(text)) : 
        if text[i] in res :
            res.pop(text[i])
        else :
            res.append(text[i])
    return  len(res) <= 1