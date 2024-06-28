# 1||Lmax
# po dj rosnąco

from cmath import inf


if __name__ == "__main__":
    # print("hw")
    n = int(input())
    jobs = []
    L_max = float(inf)*-1

    for i in range(n):
        processing_t, due_date = map(int, input().split())
        jobs.append((processing_t,due_date))

    jobs_sorted = sorted(jobs, key=lambda x: x[1])

    t = 0
    for job in jobs_sorted:
        t += job[0]
        current_delay = t-job[1]
        # print("t:",t,"  dj:",job[1], "  c_dj:", current_delay)
        if current_delay > L_max:
            L_max = current_delay
    
    print(L_max)