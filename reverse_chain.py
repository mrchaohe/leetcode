
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
# 反转链表
def reverse_chain(node):
    head = node
    pre = None
    while head.next is not None:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur

    head.next = pre
    return head

if __name__ == "__main__":
   

    syb = Node(
        value=1,
        next = Node(
            value=3,
            next = Node(
                value=5,
                next = Node(
                    value=7
                )
            )
        )
    )

    t = reverse_chain(syb)
    
    while t is not None:
       
        print(t.value)
        t = t.next