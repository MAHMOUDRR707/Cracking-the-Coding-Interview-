def  OneAway(text1,text2) :
    ans = 0
    for i in range(len(text1)):
        if text1[i] !=  text2[i]  :
            ans+=1
    return ans <=1 