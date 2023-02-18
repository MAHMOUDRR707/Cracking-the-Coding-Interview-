 def Sum(root1 , root2):
    root = root1
    res =[]
    while  root :
        res.append(str(root.val))
        root = root.next
    helper = int("".join(res))
    root = root2
    while  root :
        res.append(str(root.val))
        root = root.next
    
    helper += int("".join(res))
    helper = str(helper)
    result =  ListNode()
    ans =  result
    for i in helper :
        result.next =  ListNode(i)
        result =  result.next
    return ans.next