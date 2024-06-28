import sys

tasks_amount = int(sys.stdin.readline().strip('\n'))
jobs = []
nodes = []
for i in range(tasks_amount):
    task_ready, task_lengths = list(map(int, sys.stdin.readline().strip().split())) 
    jobs.append((i + 1, task_ready, task_lengths))
    nodes.append(i + 1)

original_jobs = jobs.copy()
jobs.sort(key=lambda x: x[1])
print("[i,rj,pj]",jobs)

job_order_amount = int(sys.stdin.readline().strip('\n'))
job_order = []
for i in range(job_order_amount):
    operation = tuple(map(int, sys.stdin.readline().strip().split())) 
    job_order.append(operation)
print(job_order)

sorted_nodes = []
nodes_without_prev = nodes.copy()
node_without_prev = int

while nodes_without_prev:
    for i in range(len(job_order)):
        node_with_prev = int(job_order[i][1])
        if node_with_prev in nodes_without_prev:
            nodes_without_prev.remove(node_with_prev)
    for i in range(len(jobs)):
        if jobs[i][0] in nodes_without_prev:
            node_without_prev = jobs[i][0]
            break
    sorted_nodes.append(node_without_prev)
    nodes_to_remove = node_without_prev
    job_order = [op for op in job_order if op[0] != node_without_prev]
    print("node_without_prev",node_without_prev)
    print(nodes_without_prev)
    nodes_without_prev.remove(node_without_prev)
    nodes_without_prev = [node for node in nodes if node not in sorted_nodes]
    
print(sorted_nodes)
#for node in sorted_nodes:
#    print(node)
#print(sorted_nodes)
total_time = 0
for node_index in sorted_nodes:
    total_time += max(0, original_jobs[node_index - 1][1] - total_time) + original_jobs[node_index - 1][2]
    #print(node_index, total_time)

#total_time = sum(jobs[node_index - 1][2] for node_index in sorted_nodes)
print(total_time)
