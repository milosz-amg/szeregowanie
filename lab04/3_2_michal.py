import sys

n = int(sys.stdin.readline().strip('\n'))

jobs = []

for i in range(n):
    ready, length, deadline  = list(map(int, sys.stdin.readline().strip().split())) 
    jobs.append([ready, length, deadline])

jobs.sort(key=lambda x: x[0])

current_time = min([t[0] for t in jobs])
jobs_realized = []
jobs_ready = []
while(True):
    for job in jobs[:]:
        if current_time == job[0]:
            jobs_ready.append(job)
            jobs.remove(job)
    for job in jobs_ready[:]:
        if job[1] == 0:
            jobs_realized.append(max(current_time - job[2], 0))
            jobs_ready.remove(job)

    if(len(jobs)==0 and len(jobs_ready)==0):
        break
    #print(f"jobs: {jobs}, jobs_ready: {jobs_ready}, jobs_realized: {jobs_realized}, current_time: {current_time}\n")
    jobs_ready.sort(key=lambda x: (x[2], x[1]))
    if jobs_ready:
        time_spended_on_doing_job = min([t[0] - current_time for t in jobs] + [jobs_ready[0][1]])
        jobs_ready[0][1] -= time_spended_on_doing_job
    else:
         time_spended_on_doing_job = min([t[0] - current_time for t in jobs])
    #print(f"time_spended_on_doing_job: {time_spended_on_doing_job}\n")
    current_time += time_spended_on_doing_job
    
#print(jobs_realized)
print(max(jobs_realized))