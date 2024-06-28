from cmath import inf
from functools import total_ordering

def calculate_total_t(seq, tasks, machine_amount):
    machine_t = [0] * machine_amount
    for task_index in seq:
        t = tasks[task_index]
        for i in range(machine_amount):
            if i == 0:
                machine_t[i] += t[i]
            else:
                if machine_t[i] < machine_t[i-1]:
                    machine_t[i] = machine_t[i-1]
                machine_t[i] += t[i]
    return machine_t[-1]

if __name__ == "__main__":
    machine_amount, tasks_amount = map(int, input().split())
    tasks=[]
    for i in range (tasks_amount):
        tasks.append(list(map(int,input().split())))

    total_t=[]
    for i in range(tasks_amount):
        total_t.append((i,sum(tasks[i])))
    total_t.sort(key=lambda x: x[1], reverse=True)

    seq = []
    for i, _ in total_t:
        min_t = float(inf)
        best_seq = None
        for pos in range(len(seq) + 1):
            new_seq = seq[:pos] + [i] + seq[pos:]
            current_t = calculate_total_t(new_seq, tasks, machine_amount)
            if current_t < min_t:
                min_t = current_t
                best_seq = new_seq
        seq = best_seq
    
    best_t = calculate_total_t(seq, tasks, machine_amount)
    print(best_t)
    print(' '.join(map(str, [x + 1 for x in seq])))