import sys

tasks_amount = int(sys.stdin.readline().strip())

tasks_lengths = []
nodes = []
for i in range(tasks_amount):
    task_length, a, b, c = list(map(int, sys.stdin.readline().strip().split())) 
    tasks_lengths.append((i+1, task_length, a, b, c))
    nodes.append(i + 1)

operations_amount = int(sys.stdin.readline().strip())

operations = []
for i in range(operations_amount):
    operation = tuple(map(int, sys.stdin.readline().strip().split())) 
    operations.append(operation)

sorted_nodes = []
nodes_without_next = nodes.copy()

sum_of_length = sum([task[1] for task in tasks_lengths])
overall_max_cost = 0
while nodes_without_next:
    for i in range(len(operations)):
        node_with_next = int(operations[i][0])
        if node_with_next in nodes_without_next:
            nodes_without_next.remove(node_with_next)
    min_cost = 1000
    min_node = int
    cost = 1000
    for node in nodes_without_next:
        cost = tasks_lengths[node-1][2]*(sum_of_length**2) + tasks_lengths[node-1][3]*sum_of_length + tasks_lengths[node-1][4]
        if min_cost > cost:
            min_cost = cost
            min_node = tasks_lengths[node-1][0]
    sorted_nodes.append(min_node)
    nodes_to_remove = min_node
    operations = [op for op in operations if op[1] != min_node]
    nodes_without_next.remove(min_node)
    nodes_without_next = [node for node in nodes if node not in sorted_nodes]
    sum_of_length -= tasks_lengths[min_node-1][1]
    if min_cost > overall_max_cost:
        overall_max_cost = min_cost

print(overall_max_cost)