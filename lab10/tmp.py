import sys
 
machine_amount, tasks_amount = map(int, sys.stdin.readline().strip().split())
tasks = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(tasks_amount)]
 
total_times = [(i, sum(tasks[i])) for i in range(tasks_amount)]
total_times.sort(key=lambda x: x[1], reverse=True)
print(total_times)
 
def calculate_total_time(sequence, tasks, machine_amount):
    machine_time = [0] * machine_amount
    for task_index in sequence:
        times = tasks[task_index]
        for i in range(machine_amount):
            if i == 0:
                machine_time[i] += times[i]
            else:
                if machine_time[i] < machine_time[i-1]:
                    machine_time[i] = machine_time[i-1]
                machine_time[i] += times[i]
    return machine_time[-1]
 
 
sequence = []
for i, _ in total_times:
    min_time = 100000000000
    best_sequence = None
    for pos in range(len(sequence) + 1):
        new_sequence = sequence[:pos] + [i] + sequence[pos:]
        current_time = calculate_total_time(new_sequence, tasks, machine_amount)
        if current_time < min_time:
            min_time = current_time
            best_sequence = new_sequence
    sequence = best_sequence
 
best_time = calculate_total_time(sequence, tasks, machine_amount)
 
print(best_time)
print(' '.join(map(str, [x + 1 for x in sequence])))