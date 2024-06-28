# 1| rj, pmtn | SUM:Cj              SRTP
# max: SUM(1->n): d - Cj    (d-minut w dniu)
#               = nd - SUM(1->n)    <=> min: SUM(j->n): Cj

# T - oznaczających odpowiednio liczbę minut, po której Eulalia pozna specyfikację
# C - liczbę minut potrzebną na jego wykonanie. 

# Przykładowe wejście:

# 6
# 2 4
# 4 1
# 8 2
# 9 3
# 11 1
# 12 1
from queue import PriorityQueue

if __name__ == "__main__":
    jobs_amount = int(input().strip())

    jobs_list = []

    for i in range(jobs_amount):
        arrival_t, execution_t = map(int, input().strip().split())
        jobs_list.append((execution_t, arrival_t))

    current_time = 0
    time_list = []
    jobs = PriorityQueue()

    while not jobs.empty() or jobs_list:
        while jobs_list and jobs_list[0][1] == current_time:
            execution_t, arrival_t = jobs_list.pop(0)
            jobs.put((execution_t, arrival_t))

        current_time += 1
        if not jobs.empty():
            execution_t, arrival_t = jobs.get()

            execution_t -= 1

            if execution_t == 0:
                time_list.append((current_time, arrival_t))
            else:
                jobs.put((execution_t, arrival_t))
                
    time_list.sort(key=lambda x: x[1])
    for time in time_list:
        print(time[0])
    
    
    