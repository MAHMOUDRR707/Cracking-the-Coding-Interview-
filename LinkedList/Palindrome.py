 def Palindrome(head):
    root = head
    res =[]
    while  root :
        res.append(root.val)
        root = root.next
    return res ==res[::-1]