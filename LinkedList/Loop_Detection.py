 def Loop_Detection:(head):
    root = head
    res =[]
    while  root :
        if root.val in res :
            return root
        res.append(root.val)
        root = root.next
    