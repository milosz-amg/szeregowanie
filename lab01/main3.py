import sys
from queue import PriorityQueue

tasks_amount = int(sys.stdin.readline().strip())

tasks = PriorityQueue()
tasks_list = []
for i in range(tasks_amount):
    arrival_time, execution_time = map(int, sys.stdin.readline().strip().split())
    tasks_list.append((execution_time, arrival_time))

current_time = 0

time_list = []

while not tasks.empty() or tasks_list:
    while tasks_list and tasks_list[0][1] == current_time:
        execution_time, arrival_time = tasks_list.pop(0)
        tasks.put((execution_time, arrival_time))

    current_time += 1
    if not tasks.empty():
        execution_time, arrival_time = tasks.get()

        execution_time -= 1

        if execution_time == 0:
            time_list.append((current_time, arrival_time))
        else:
            tasks.put((execution_time, arrival_time))

time_list.sort(key=lambda x: x[1])
for time in time_list:
    print(time[0])