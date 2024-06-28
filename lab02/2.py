# Problem 1 | prec | Cmax
# Cmax = Suma
# posortowac graf topologicznie - wybieramy zawsze to z najniższym numerem
# za każdym razem algorytmem khana przejrzec wszystkie dostepne i wybrac to z najnizszym numerem

if __name__ == "__main__":
    n, e  = map(int, input().split())

    job_execution_time=[]
    for i in range(n):
        job_execution_time.append(int(input().strip()))
        
    job_order=[]
    for i in range(e):
        job_before, current_job = map(int, input().split())
        job_order.append((job_before-1,current_job-1))  #-1 żeby pasowało z indexami

    pred_lists=[[] for i in range(n)]   #tworzenie list poprzednikow
    jobs_done=[]                        #lista zadan dotychczas wykonanych
    jobs_mark_done=[0]*n                #lista znacznikow czy i-te zadanie jest wykonane
    for order in job_order:
        before, current = map(int,order)
        pred_lists[current].append(before)

    print(pred_lists)
    print(jobs_done)
    print(jobs_mark_done)

    total_time=0
    while len(jobs_done)!=len(job_execution_time):  #V!= empty_set - nie usuwam zadan, wiec sprawdzam czy wszystkie zostaly wykonane
        for i in range(n):
            if jobs_mark_done[i] == 0 and all(jobs in jobs_done for jobs in pred_lists[i]): #jesli zadanie nie bylo jeszcze wykonane i jego poprzednicy są wykonani
                print(i)
                jobs_mark_done[i]=1
                jobs_done.append(i)
                total_time += job_execution_time[i]
                break
    print(total_time)

