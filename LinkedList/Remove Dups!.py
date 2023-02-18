#method one

res = set()
node = root 
while node :
    res.add(node.val)
    node =  node.next

res =  ListNode()
ans =  res
for i in res:
    res.next =  ListNode(i)
    res = res.next
return ans.next