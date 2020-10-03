import sys

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Leetcode 328 - odd Even Linked List
def oddEvenLinkedList(head):

    if head is None or head.next is None:
        return head

    temp = head
    odd = temp
    even = temp.next
    odd_point = odd
    even_point = even

    while temp.next.next is not None:
        temp = temp.next.next
        odd_point.next = temp
        odd_point = odd_point.next
        if temp.next is not None:
            even_point.next = temp.next
            even_point = even_point.next

        if temp.next is None:
            even_point.next = None
            break

    odd_point.next = even

    return odd


# Test
lls = [ListNode(), ListNode(), ListNode(), ListNode(), ListNode()]
vs = [1, 2, 3, 4, 5]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]

input = lls[0]

out = oddEvenLinkedList(input)


# 2. Leetcode 1474 - Delete N Nodes After M Nodes of a Linked List
def deleteNNodes(head, m, n):

    if head is None or head.next is None:
        return head

    temp = head
    temp_point = head


    while temp.next is not None:
        i = 1
        j = 1

        while i < m and temp_point.next is not None:
            i = i + 1
            temp_point = temp_point.next

        temp = temp_point

        while j <= n and temp_point.next is not None:
            j = j + 1
            temp_point = temp_point.next

        if temp_point.next is None:
            temp.next = None
            break

        temp.next = temp_point.next

        temp = temp.next
        temp_point = temp

    return head


# Test
lls = [ListNode(), ListNode(), ListNode(), ListNode(), ListNode(),ListNode(), ListNode(), ListNode(), ListNode(), ListNode(),ListNode(), ListNode(), ListNode()]
vs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]

input = lls[0]

out = deleteNNodes(input, 2, 3)


# 3. Leetcode 237 - Delete Node in a Linked List
def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val
    node.next = node.next.next


# 4. Leetcode 725 - Split Linked List in Parts
def splitListToParts(root, k):
    """
    :type root: ListNode
    :type k: int
    :rtype: List[ListNode]
    """

    out = [None] * k

    if root is None:
        return out

    if root.next is None:
        out[0] = root
        return out

    i = 1
    temp = root

    while temp.next is not None:
        i = i + 1
        temp = temp.next

    temp = root
    if i <= k:
        j = 0
        while j < i and temp is not None:
            tempp = temp
            left = temp.next
            tempp.next = None
            out[j] = tempp
            temp = left
            j = j + 1

        return out

    re = i % k
    quant = i // k
    count = 1
    temp = root

    for ki in range(0, k):
        if count <= re:
            amount = quant + 1
        else:
            amount = quant

        j = 1
        left = temp
        tempp = left
        while j < amount:
            tempp = tempp.next
            j = j + 1

        temp = tempp.next
        tempp.next = None
        out[ki] = left

        count = count + 1

    return out


# 5. Leetcode 82 - Remove Duplicates from Sorted List II
def deleteDuplicates(head):
    dummy = ListNode()
    dummy.val = -sys.maxsize - 1
    dummy.next = head
    temp = dummy
    point = temp.next
    dup = -sys.maxsize - 1

    while point is not None:
        if point.next is not None and point.val == point.next.val:
            dup = point.val
            point = point.next.next
        elif point.val == dup:
            point = point.next
        else:
            temp.next = point
            point = point.next
            temp = temp.next

    temp.next = point

    return dummy.next

# 6. Leetcode 25 - Reverse Nodes in k-Group
# Hard

# 7. Leetcode 143 - Reorder List
# No thought

# 8. Leetcode 1019 - Next Greater Node In Linked List
def nextLargerNodes(head):
    out = []
    st = []
    ind = []
    i = 0

    while head is not None:

        out.append(i)
        if len(st) == 0 or head.val <= st[-1]:
            st.append(head.val)
        else:
            while len(st) != 0 and head.val > st[-1]:
                out[ind.pop()] = head.val
                st.pop()

            st.append(head.val)

        ind.append(i)
        i = i + 1
        head = head.next

    while len(ind) != 0:
        out[ind.pop()] = 0

    return out


# 9. Leetcode 24 - Swap Nodes in Pairs
def swapPairs(head):

    if head is None or head.next is None:
        return head

    dummy = ListNode()
    dummy.next = head
    temp = dummy

    while head is not None:
        if head.next is None:
            break

        tempp = head.next.next
        temp.next = head.next
        temp.next.next = head
        temp = head
        temp.next = tempp
        head = temp.next

    return dummy.next


# 10. Leetcode 25 - Reverse Nodes in k-Group
# hard

# 11. Leetcode 203 - Remove Linked List Elements
def removeElements(head, val):
    dummy = ListNode()
    dummy.val = -sys.maxsize - 1
    dummy.next = head
    temp = dummy

    while head is not None:
        while head is not None and head.val == val:
            head = head.next

        temp.next = head
        temp = temp.next

        if head is not None:
            head = head.next

    return dummy.next


# 12. Leetcode 20 - Valid Parentheses
def isValid(s):
    dic = {')': '(', ']': '[', '}': '{'}

    if len(s) == 1 or len(s) % 2 != 0 or dic.get(s[0]) is not None:
        return False

    st = []

    for i in s:

        if dic.get(i) is None:
            st.append(i)
        else:
            if len(st) == 0:
                return False
            else:
                val = st.pop()
                if val != dic.get(i):
                    return False

    if len(st) == 0:
        return True
    else:
        return False


# 13. Leetcode 71 - Simplify Path
# no understand


# 14. Leetcode 155 - Min Stack - too slow (better solution?)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        self.data = self.data[:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.data)


# 15. Leetcode 224 - Basic Calculator
# Hard

# 16. Leetcode 316 - Remove Duplicate Letters
# Hard

# 17. Leetcode 385 - Mini Parser
# Complicated


# 18. Leetcode 394 - Decode String
def decodeString(s):

    out = ''
    nonum_st = []
    num_st = []
    pr = ['[', ']']
    temp_st = []
    num = ''

    for i in range(0, len(s)):

        if s[i].isdigit():
            if s[i + 1].isdigit():
                num = num + s[i]
            else:
                num_st.append(int(num + s[i]))
                num = ''
        else:
            if s[i] not in pr and len(nonum_st) == 0:
                out = out + s[i]
            elif s[i] == pr[0] or (s[i] not in pr and len(nonum_st) != 0):
                nonum_st.append(s[i])
            else:
                temp = ''
                k = num_st.pop()
                while nonum_st[-1] != pr[0]:
                    temp = temp + nonum_st.pop()

                nonum_st.pop()

                temp = temp * k

                if len(num_st) == 0:
                    out = out + temp[::-1]
                else:
                    nonum_st.append(temp)

    return out


# 19. Leetcode 402 - Remove K Digits
def removeKdigits(num, k):
    if len(num) == k:
        return str(0)

    st = []

    for i in range(0, len(num)):

        if len(st) == 0 or st[-1] <= num[i] or k == 0:
            st.append(num[i])
        else:
            while len(st) != 0 and st[-1] > num[i] and k > 0:
                st.pop()
                k = k - 1

            st.append(num[i])

    while k > 0:
        st.pop()
        k = k - 1

    return str(int("".join(st)))


# 20. Leetcode 456 - 132 Pattern
# Medium - classic dont know to do to

# 21. Leetcode 496 - Next Greater Element I
def nextGreaterElement(nums1, nums2):
    if len(nums2) == 0:
        return []

    st = [nums2[0]]
    dic = {}
    res = []
    for j in range(1, len(nums2)):

        i = nums2[j]

        while len(st) != 0 and st[-1] < i:
            dic[st[-1]] = i
            st.pop()

        st.append(i)

    for i in nums1:
        if dic.get(i) != None:
            res.append(dic[i])
        else:
            res.append(-1)

    return res


# 22. Leet code 503 - Next Greater Element II
# Median - dont know how to do


# 23. Leet code 726 - Number of Atoms
# Hard


# 24. Leet code 735 - Asteroid Collision
def asteroidCollision(asteroids):
    out = []
    st = []

    for i in asteroids:

        if i > 0:
            st.append(i)
        elif i < 0 and len(st) == 0:
            out.append(i)
        else:
            while st[-1] < -i:
                st.pop()
                if len(st) == 0:
                    out.append(i)
                    break

            if len(st) != 0 and st[-1] == -i:
                st.pop()

    out = out + st

    return out


# 25. Leet code 739 - Daily Temperatures
def dailyTemperatures(T):
    st = []
    out = [0] * len(T)

    for i in range(0, len(T)):
        if len(st) == 0 or T[st[-1]] >= T[i]:
            st.append(i)
        else:
            while T[st[-1]] < T[i]:
                out[st[-1]] = i - st[-1]
                st.pop()
                if len(st) == 0:
                    break

            st.append(i)

    return out


# 26. Leet code 844 - Backspace String Compare
def backspaceCompare(S, T):
    emp = '#'
    sst = []
    tst = []

    for i in S:

        if i != emp:
            sst.append(i)
        elif len(sst) != 0 and i == emp:
            sst.pop()

    for i in T:
        if i != emp:
            tst.append(i)
        elif len(tst) != 0 and i == emp:
            tst.pop()

    if sst == tst:
        return True
    else:
        return False


# 27. Leet code 856 - Score of Parentheses
# Similar to decoding problem


# 28. Leet code 880 - Decoded String at Index
# Memory Limit Exceed
def decodeAtIndex(S, K):
    st = ''

    for i in range(0, len(S)):
        if S[i].isdigit():
            num = int(S[i])
            if len(st) * num >= K:
                return st[(K % len(st)) - 1]
            else:
                st = st * int(S[i])
        else:
            st = st + S[i]

    return st[K - 1]

# 29. Leet code 895 - Maximum Frequency Stack
# Hard



# 30. Leet code 921 - Minimum Add to Make Parentheses Valid
# Parentheses questions are confusing



# 31. Leet code 1019 - Next Greater Node In Linked List
def nextLargerNodes(head):
    out = []
    st = []
    ind = []
    i = 0

    while head is not None:

        out.append(i)
        if len(st) == 0 or head.val <= st[-1]:
            st.append(head.val)
        else:
            while len(st) != 0 and head.val > st[-1]:
                out[ind.pop()] = head.val
                st.pop()

            st.append(head.val)

        ind.append(i)
        i = i + 1
        head = head.next

    while len(ind) != 0:
        out[ind.pop()] = 0

    return out


# 32. Leet code 1021 - Remove Outermost Parentheses
# Simple




