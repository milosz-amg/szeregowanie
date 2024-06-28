# F2||Cmax
# najpierw wytnij, potem wierc - flowshop
# alg Johnsona - posortowac zadania w odpowiednim porządku

from ctypes import Union


if __name__ == "__main__":
    n = int(input())
    jobs = []
    for i in range(n):
        j, w = map(int, input().split())
        # p1, p2, id
        jobs.append((j, w, i+1))
    
    A = []
    B = []
    
    for job in jobs:
        if job[0] <= job[1]:
            A.append(job)
        else:
            B.append(job)

    A.sort(key=lambda x: x[0])
    B.sort(key=lambda x: x[1], reverse=True)
    A = A + B
    # print(A)
    
    time_a=0
    time_b=0

    for job in A:
        time_a += job[0]
        if time_b < time_a:
            time_b = time_a
        time_b += job[1]
        print(job[2],time_a ,time_b)
        