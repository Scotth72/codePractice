# class ListNode(object):
#     def __init__(self, x):
#         self.value =x
#         self.next = None

def remove_kth_from_end(head, k):
    llarray = list() # create a list to append the nodes too

    cur = head  # first pointer
    while cur is not None:
        llarray.append(cur) # adds/appends the nodes to the list
        cur = cur.next  #  iterate through the array

        positive = (len(llarray) - k) -1 # this gives me the node before the k

        if positive >= 0:
            counter = positive

            cur1 = head # second pointer
            while counter != 0:  
                cur1.next = head # moves allong
                counter -= 1

            if k == 0:            
                cur1.next = None
            else:
                cur1.next = cur1.next.next # move the pointer to next node to pass the kth node

        elif positive == -1:
            head = head.next

        return head                    

    # Time complexity O(n)
        


