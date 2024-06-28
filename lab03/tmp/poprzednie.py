import sys

tasks_amount, operations_amount = map(int, sys.stdin.readline().strip().split())

tasks_length = []
nodes = []
for i in range(tasks_amount):
    task_lengths = list(map(int, sys.stdin.readline().strip().split()))  # Split the line into individual integers
    tasks_length.append((i + 1, task_lengths))
    nodes.append(i + 1)

operations = []
for i in range(operations_amount):
    operation = tuple(map(int, sys.stdin.readline().strip().split()))  # Split the line into two separate integers
    operations.append(operation)


sorted_nodes = []
nodes_without_prev = nodes.copy()


while nodes_without_prev:
    for i in range(len(operations)):
        node_with_prev = int(operations[i][1])
        if node_with_prev in nodes_without_prev:
            nodes_without_prev.remove(node_with_prev)
    sorted_nodes.append(nodes_without_prev[0])
    nodes_to_remove = nodes_without_prev[0]
    operations = [op for op in operations if op[0] != nodes_without_prev[0]]
    nodes_without_prev.pop(0)
    nodes_without_prev = [node for node in nodes if node not in sorted_nodes]
    

for node in sorted_nodes:
    print(node)

total_time = 0
total_time = sum(tasks_length[node_index - 1][1][0] for node_index in sorted_nodes)
print(total_time)
