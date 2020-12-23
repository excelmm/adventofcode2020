class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None

with open("input.txt", "r") as f:
    rawinput = f.read().splitlines()
input = []
for i in rawinput[0]:
    input.append(int(i))

nodes = {}

prev_node = None
for i in input:
    node = Node(i)
    nodes[i] = node
    if prev_node is not None:
        node.prev = prev_node
        prev_node.next = node
    prev_node = node

for i in range(len(input) + 1, 1000000 + 1):
    node = Node(i)
    nodes[i] = node
    if prev_node is not None:
        node.prev = prev_node
        prev_node.next = node
    prev_node = node

current = nodes[input[0]]
prev_node.next = current
current.prev = prev_node

for i in range(10000000):
    current_val = current.val

    cup_1 = current.next
    cup_2 = cup_1.next
    cup_3 = cup_2.next

    current.next = cup_3.next
    current.next.prev = current

    destination_val = current_val - 1
    if destination_val < 1:
        destination_val = 1000000
    while destination_val in (cup_1.val, cup_2.val, cup_3.val):
        destination_val -= 1
        if destination_val < 1:
            destination_val = 1000000
        
    
    destination = nodes[destination_val]
    cup_3.next = destination.next
    cup_3.next.prev = cup_3
    destination.next= cup_1
    cup_1.prev = destination

    current = current.next

    print(current.val)

while current.val != 1:
    current = current.next

print(current.next.val * current.next.next.val)