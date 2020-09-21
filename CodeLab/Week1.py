import sys

class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# DAY 1
# 1. Sum of two Strings: Given two non-negative integers num1 and num2 represented as string,
# return the sum of num1 and num2.
def sumTwoStrings(s1, s2):
    return int(s1) + int(s2)


# Test
s1 = '123'
s2 = '348'
print(sumTwoStrings(s1, s2))


# 2. (1)Two Sum Problem: Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
## Return if the sum exist
def twoSumExist(nums, target):
    nums = sorted(nums)
    start = 0
    end = len(nums) - 1

    while start < end:
        if nums[start] + nums[end] == target:
            return True

        if nums[start] + nums[end] < target:
            start = start + 1
        elif nums[start] + nums[end] > target:
            end = end - 1

    return False


## Return index
def twoSumIndex(nums, target):
    dic = {key: i for i, key in enumerate(nums)}
    i = 0

    while i < len(nums):
        res = target - nums[i]

        if dic.get(res) != None:
            return [i, dic.get(res)]
        else:
            i = i + 1


# Test
nums = [2, 3, 7, 4, 1, 6, 8]
target = 7
print(twoSumExist(nums, target))
print(twoSumIndex(nums, target))


# 3. (189)Rotate and array: Given an array, rotate the array to the right by k steps, where k is non-negative.
# How about use O(1) space
def rotateArray(nums, k):
    out = []
    for i in range(-k, 0):
        out.append(nums[i])

    for i in range(0, (len(nums) - k)):
        out.append(nums[i])

    return out


# Test
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotateArray(nums, k))


# 4. Is Unique: Implement an algorithm to determine if a string has all unique characters.
def uniqueString(str):
    s = set()

    for i in str:
        if (s.__contains__(i)):
            return True
        else:
            s.add(i)

    return False


# Test
print(uniqueString("leetcode"))


# 5. Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
def checkPermutation(str1, str2):
    d = {}

    for i in str1:
        if d.get(i) == None:
            d[i] = 1
        else:
            d[i] = d[i] + 1

    for i in str2:
        if d.get(i) == None:
            return False
        elif d.get(i) == 1:
            d.pop(i)
        elif d.get(i) > 1:
            d[i] = d[i] - 1

    if d == {}:
        return True

    return False


# Test
print(checkPermutation("leet", "ltee"))


# DAY 2
# LinkedList Class
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Leetcode 19 - Remove Nth node from End of List
def removeLinkedList(head, n):
    dummy = ListNode()
    dummy.next = head
    left = dummy
    right = dummy
    i = 0

    while i < n:
        right = right.next
        i = i + 1

    while right.next is not None:
        left = left.next
        right = right.next

    left.next = left.next.next

    return dummy.next


# Test
lls = [ListNode(), ListNode(), ListNode(), ListNode(), ListNode()]
vs = [1, 2, 3, 4, 5]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]

input = lls[0]
n = 2

out = removeLinkedList(input, n)


# LeetCode 83 - Remove duplicates from sorted Link List
def removeDupLinkedList(head):
    if head is None:
        return head

    temp = head

    while temp.next is not None:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next

    return head


# Test
lls = [ListNode(), ListNode(), ListNode(), ListNode(), ListNode()]
vs = [1, 1, 2, 3, 3]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]
input = lls[0]

out = removeDupLinkedList(input)


# LeetCode 86 - Partition List around a value X
def partitionList(head, x):
    if head is None or head.next is None:
        return head

    dummy = ListNode()
    dummy.val = -sys.maxsize - 1
    dummy.next = head
    left = dummy
    right = dummy

    while right is not None and right.val < x:
        right = right.next

    while right is not None and right.next is not None:

        while left.next is not None and left.next.val < x:
            left = left.next

        while right.next is not None and right.next.val >= x:
            right = right.next

        if right.next is not None and right.next.val < x:
            templ = left.next
            tempr = right.next.next
            left.next = right.next
            left.next.next = templ
            right.next = tempr
            left = left.next

    return dummy.next


# Test
lls = [ListNode(), ListNode(), ListNode(), ListNode(), ListNode(), ListNode()]
vs = [1, 4, 3, 2, 5, 2]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]
input = lls[0]
x = 3

out = partitionList(input, x)



# LeetCode 708 - Insert into a Sorted Circular Linked List
def insertSortedLinkedList(head, insertVal):
    if head is None:
        head = ListNode()
        head.val = insertVal
        head.next = head
        return head

    temp = ListNode()
    temp.val = insertVal

    if head.next is head:
        head.next = temp
        temp.next = head
        return head

    cur = head

    while cur.val <= cur.next.val:
        cur = cur.next
        if cur is head:
            break

    newcur = cur.next

    if newcur.val >= insertVal or cur.val <= insertVal:
        temp.next = newcur
        cur.next = temp
        return head

    while newcur.val < insertVal:

        if newcur.val <= insertVal and newcur.next.val >= insertVal:
            temp1 = newcur.next
            newcur.next = temp
            temp.next = temp1

        newcur = newcur.next

    return head


# Test
lls = [ListNode(), ListNode(), ListNode()]
vs = [3, 4, 1]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]

lls[2].next = lls[0]
input = lls[0]
insertVal = 2

out = insertSortedLinkedList(input, insertVal)

# LeetCode 1290 - Convert Binary Number in a Linked List to Integer
def convertBinaryLinkedList(head):
    temp = head
    count = 0
    sum = 0
    while temp.next != None:
        if temp.next != None:
            count = count + 1
        temp = temp.next

    temp = head

    for i in range(0, (count + 1)):
        sum = sum + temp.val * 2 ** (count - i)
        temp = temp.next

    return sum


# Test
lls = [ListNode(), ListNode(), ListNode(), ListNode(), ListNode()]
vs = [1, 1, 0, 0, 1]

for i in range(0, len(lls)):
    lls[i].val = vs[i]
    if (i + 1) < len(lls):
        lls[i].next = lls[(i + 1)]
input = lls[0]

print(convertBinaryLinkedList(input))
