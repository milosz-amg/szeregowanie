#1|rj,pmtn|Lmax
# alg Horna (EDD z powtórzeniami)

if __name__ == "__main__":
    n = int(input())
    jobs=[]

    for i in range(n):
        ready, length, deadline  = list(map(int, input().strip().split())) 
        jobs.append([ready, length, deadline])

    jobs = sorted(jobs, key=lambda x: x[0])
    # print("(rj,pj,dj):",jobs)
    # print("curr_t: ",current_time)
    current_time = min([t[0] for t in jobs])
    jobs_done = []
    jobs_ready = []

    while(True):
        jobs_cp = jobs
        # print(jobs_cp)
        for job in jobs_cp:
            if current_time == job[0]:  #jezeli czas taki jak ready_t
                jobs_ready.append(job)
                jobs.remove(job)
        # print(jobs_ready)
        for job in jobs_ready[:]:
            if job[1] == 0:
                jobs_done.append(max(current_time - job[2], 0))
                jobs_ready.remove(job)
        # print(jobs_ready)

        if(len(jobs)==0 and len(jobs_ready)==0):
            break           #repeat until
        jobs_ready.sort(key=lambda x: (x[2], x[1])) #uszereguj w przedziale

        if jobs_ready:
            time_spended_on_job = min([t[0] - current_time for t in jobs] + [jobs_ready[0][1]])
            jobs_ready[0][1] -= time_spended_on_job
        else:
            time_spended_on_job = min([t[0] - current_time for t in jobs])
        current_time += time_spended_on_job
    
print(max(jobs_done))

    
    
    