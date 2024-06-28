# Define the jobs list and the topo_order list
jobs = [[1, 1, 0], [0, 3, 1], [10, 3, 2], [2, 2, 3], [4, 1, 4], [1, 2, 5]]

topo_order = [5, 1, 2, 3, 4, 0]

# Sort the jobs list by the topo_order
sorted_jobs = sorted(jobs, key=lambda x: topo_order.index(x[2]))

# Print the sorted jobs list
print(sorted_jobs)
