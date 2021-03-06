class ListNode(object):
    def _init_(self, x):
        self.val = x
        self.next = None 
        
class Solutions:
    def addTwoNumbers(self, l1, l2):

        print('')
        print('inside function...')
        
        # Declare pointers for traversal. Added for clarity.
        p1 = l1
        p2 = l2

        # Declare current carryover.

        currentCarry = 0

        # Declare curr variable to traverse and add new nodes to new list

        head = cur = ListNode(0)

        # Iteration condition.

        while p1 or p2 or currentCarry:

            print(p1.val, p2.val, currentCarry)

            # Determine current value nd carry over.

            currentVal = currentCarry
            currentVal += 0 if p1 is None else p1.val
            currentVal += 0 if p2 is None else p2.val
            if currentVal >= 10:
                currentCarry -= 10
                currentCarry = 1
            else:
                currentCarry = 0

            print(currentVal, currentCarry)

            # Ad current value as it will always as least be "1".
            cur.next = ListNode(currentVal)
            cur = cur.next    

            # Add base cases for iterating linked lists.
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next 
            elif p2 is None:
                p1 = p1.next 
            else:
                p1 = p1.next 
                p2 = p2.next 

            print('exiting...') 
            print('')

            # Return next node.
            return head.next 
            
                





