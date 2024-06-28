# P | | Cmax
# algorytm listowy LPT - bierzemy obecnie najdłużesze zadanie

if __name__ == "__main__":
    m, n = map(int, input().split())

    employee_times = [0] * m
    jobs = []
    for i in range(n):
        jobs.append(int(input().strip()))

    jobs.sort(reverse=True) #posortuj malejąco

    for _ in range(len(jobs)):
        min_time, min_index = min((employee_time, index) for index, employee_time in enumerate(employee_times))
        #wybierz minimalnego pracownika o minimalnym czasie
        employee_times[min_index] += jobs[0]
        jobs.pop(0)

    print(max(employee_times))
