def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = []
        b = []
        
        while headA:
            
            a.append(headA)
            headA = headA.next
        while headB:
            b.append(headB)
            headB = headB.next
        a = a[::-1]
        b = b[::-1]
        if a[0] == b[0] :
            n,m =  len(a),len(b)
            for i in range(min(n,m)):
                if a[i] != b[i] :
                    return a[i-1]
            
            if n >m :
                return b[-1]
            else:
                return a[-1]
        return None