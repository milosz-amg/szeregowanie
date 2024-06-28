# Problem 1 | rj | Cmax
# posortowac po rj w górę
# policzyc kiedy sie zakonczy i kiedy sie skonczy

if __name__ == "__main__":
    n = int(input())
    jobs = []
    finish_times={}
    current_time=0

    for i in range(n):
        arrival_t, execution_t  = map(int, input().split())
        jobs.append([arrival_t, execution_t, i]) #[rj, pn, index do printowania]

    jobs.sort(key=lambda x: x[0])
    # print(jobs)

    for j in range(0, n):
        # print("c_t:", current_time,"rj: ", jobs[j][0], "ep:",jobs[j][1])
        current_time = max(current_time,jobs[j][0])
        current_time = current_time + jobs[j][1]
        finish_times[jobs[j][2]] = current_time

    # sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[0]))
    sorted_finish_times = dict(sorted(finish_times.items(), key=lambda item: item[0]))
    for key, value in sorted_finish_times.items():
        print(value)
    print(current_time)