 def removeNthFromEnd( head, n):
    root = head
    counter = 0
    while  root :
        if counter == n-1 :
            return root.val
        root = root.next
    return -1