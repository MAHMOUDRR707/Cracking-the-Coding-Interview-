 def removemidddle( head, n):
    root = head
    lenght = 0
    res =[]
    while  root :
        res.append(root.val)
        root = root.next
    
    res.pop(len(res)//2)
    result =  ListNode()
    ans =  result
    for i in res :
        result.next =  ListNode(i)
        result =  result.next
    return ans.next