#1||suma Uj
# po dj w górę, dodawanie do zbioru i ewentualne usówanie

if __name__ == "__main__":
    n = int(input())
    jobs = []

    for i in range(n):
        processing_t, due_date = map(int, input().split())
        jobs.append((processing_t,due_date))

    jobs = sorted(jobs, key=lambda x: x[1])
    t = 0
    jobs_set = set()

    for job in jobs:
        t += job[0]
        # print("t:",t,"  j_s:",jobs_set)
        jobs_set.add(job)
        if t > job[1]:
            max_elem = max(jobs_set, key=lambda x:x[0])
            jobs_set.remove(max_elem)
            t -= max_elem[0]
        
    print(len(jobs_set))