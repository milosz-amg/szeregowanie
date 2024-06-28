# P | pmtn | Cmax
# alg McNaughtona
# nie przestawiac maszyn, nie przestawiac zadan
# jak umieszczamy zadanie na koncu

def pretty_print(C_max, m, employee_jobs):
    print(f"{int(C_max)}")
    for i, ej in enumerate(employee_jobs):
        line = f"{i+1}: "
        for ts in ej:
            line += f"{ts[0]+1}[{int(ts[1])},{int(ts[2])}] "
        print(line)
            

if __name__ == "__main__":
    m, n = map(int, input().split())
    jobs=[]
    for id in range(n):
        jobs.append((int(input())))
        #[(id, time),....]

    # print(jobs)

    total_time = sum(jobs)
    max_time = max(jobs)
    C_max = max(total_time / m, max_time)

    employee_jobs=[[] for _ in range(m)]
    # print(employee_jobs)

    t = 0
    i = 0

    for j in range(n):
        if t + jobs[j] <= C_max:
            employee_jobs[i].append((j, t, t + jobs[j]))
            t += jobs[j]
        else:
            if t < C_max:
                employee_jobs[i].append((j, t, C_max))
            employee_jobs[i+1].append((j, 0, jobs[j] - (C_max - t)))
            i += 1
            t = jobs[j] - (C_max - t)

    pretty_print(C_max,m,employee_jobs)

