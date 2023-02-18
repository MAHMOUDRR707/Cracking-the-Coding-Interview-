 def Partition( head, n):
    root = head
    lenght = 0
    left =[]
    right = []
    while  root :
        x =  root.val 
        if x <n:
            left.appebd(x)
        else :
            right.append(x)
        root = root.next
    
    result =  ListNode()
    ans =  result
    for i in left :
        result.next =  ListNode(i)
        result =  result.next
    for i in right :
        result.next =  ListNode(i)
        result =  result.next
    return ans.next
