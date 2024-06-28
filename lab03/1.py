# 1 | prec, rj | Cmax
#   1) posortowac topoplogiczni graf, 
#   2) aktualizowac czas gotowosci rj
#       Ji -> Jj 
#       ri=5, pi=7    rj=9 -> rj=12
#   3) posortowac po rj w górę

if __name__ == "__main__":
    n = int(input())
    jobs = []

    for i in range(n):
        arrival_t, execution_t  = map(int, input().split())
        jobs.append([arrival_t, execution_t, i]) #[rj, pn, index do printowania]

    e = int(input())
    job_order=[]
    for i in range(e):
        job_before, current_job = map(int, input().split())
        job_order.append((job_before-1,current_job-1))

    pred_lists=[[] for i in range(n)]   #tworzenie list poprzednikow
    jobs_done=[]                        #lista zadan dotychczas wykonanych
    jobs_mark_done=[0]*n                #lista znacznikow czy i-te zadanie jest wykonane
    for order in job_order:
        before, current = map(int,order)
        pred_lists[current].append(before)

    total_time=0
    topo_order=[]
    while len(jobs_done)!=n:  #V!= empty_set - nie usuwam zadan, wiec sprawdzam czy wszystkie zostaly wykonane
        for i in range(n):
            if jobs_mark_done[i] == 0 and all(jobs in jobs_done for jobs in pred_lists[i]): #jesli zadanie nie bylo jeszcze wykonane i jego poprzednicy są wykonani
                jobs_mark_done[i]=1
                jobs_done.append(i)
                topo_order.append(i)
                break
    
    print("jobs",jobs)  #[redy, processing, index]
    print("----------------------------------------------")
    print("pred_list",pred_lists)
    print("----------------------------------------------")
    print("topo_order",topo_order)
    print("----------------------------------------------")

    jobs = sorted(jobs, key=lambda x: topo_order.index(x[2]))

    for i in range(1,n):
        current_job_index = i
        before_job_index = i-1
        current_job_ready_time = jobs[current_job_index][0]
        current_job_ready_time = max(current_job_ready_time,jobs[before_job_index][0]+jobs[before_job_index][1])
        jobs[i][0]=current_job_ready_time

    print("jobs_in_topo_rj_edited",jobs)

    print("total_time", jobs[len(jobs)-1][0]+jobs[len(jobs)-1][1])

