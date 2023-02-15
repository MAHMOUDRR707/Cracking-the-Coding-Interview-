def  StringRotation(text1,text2) :
    if len(text1) != text2 :
        return False
    return(isSubstring(text1+text2,text2))
