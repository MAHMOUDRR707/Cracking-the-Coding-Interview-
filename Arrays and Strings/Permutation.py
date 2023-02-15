def  Permutation(text1,text2) :
    text1 =  sorted(text1)
    text2 =  sorted(text2)
    if len(text1) != len(text2):
        return "Not Permutation"
    for i in range(len(text1)):
        if text1[i]!= text2[i]:
            return "Not Permutation"
    return "Permutation"