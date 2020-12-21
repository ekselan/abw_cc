# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Plan is to traverse each LL and extract node vals into array
        # Can then sum the arrays and reverse result to get solution
        # To sum the arrays, need to convert to single ints
        # Can write function to do this:
        def single_int(arr):
            '''Converts array into single integer'''
            a_str = [str(x) for x in arr]
            a_int = int("".join(a_str))
            return a_int

        # LL traverse and extract function
        def extract_ll(ll, arr):
            # base case
            if ll is None:
                return
            # lets etract the current node
            arr.append(ll.val)
            # extract the next nodes
            extract_ll(ll.next, arr)

        # With functions in place, can apply to each LL

        arr1 = []
        extract_ll(l1, arr1)
        int1 = single_int(arr1)

        arr2 = []
        extract_ll(l2, arr2)
        int2 = single_int(arr2)

        # print(int1)
        # print(int2)

        # Now can get sum
        res = int1 + int2

        # print(res)

        # Now need to convert sum into reversed array
        res = [int(x) for x in str(res)]
        res = res[::-1]

        # Need functions to create and add vals to LL
        def insert(root, val):
            temp = ListNode(val)

            if root is None:
                root = temp

            else:
                cur = root
                while cur.next:
                    cur = cur.next
                cur.next = temp

            return root

        def arr_to_ll(arr, n):
            root = None
            for i in range(0, n):
                root = insert(root, arr[i])
            return root

        n = len(res)
        ll = arr_to_ll(res, n)

        return ll
