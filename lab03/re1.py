# 1 | prec, rj | Cmax
#   1) posortowac topoplogiczni graf, 
#   2) aktualizowac czas gotowosci rj
#       Ji -> Jj 
#       ri=5, pi=7    rj=9 -> rj=12
#   3) posortowac po rj w górę

if __name__ == "__main__":
    n = int(input())
    jobs = []
    nodes = []

    for i in range(n):
        arrival_t, execution_t  = map(int, input().split())
        jobs.append([i,arrival_t, execution_t]) #[rj, pn, index do printowania]
        nodes.append(i)

    jobs.sort(key=lambda x: x[1])
    # print("[i,rj,pj]:",jobs)

    e = int(input())
    job_order=[]
    for i in range(e):
        job_before, current_job = map(int, input().split())
        job_order.append((job_before-1,current_job-1))
    # print(job_order)
    # posortuj topologiczie
    nodes_topo=[]
    nodes_without_prev = nodes.copy()
    node_without_prev = int

    while nodes_without_prev:
        for i in range(len(job_order)):
            node_with_prev = int(job_order[i][1])
            if node_with_prev in nodes_without_prev:
                nodes_without_prev.remove(node_with_prev)
        for i in range(len(jobs)):
            if jobs[i][0] in nodes_without_prev:
                node_without_prev = jobs[i][0]
                break
        nodes_topo.append(node_without_prev)
        nodes_to_remove = node_without_prev
        job_order = [op for op in job_order if op[0] != node_without_prev]
        # print("node_without_prev",node_without_prev)
        # print(nodes_without_prev)
        nodes_without_prev.remove(node_without_prev)
        nodes_without_prev = [n for n in nodes if n not in nodes_topo]
    
    # print(nodes_topo)
    #aktualizacja rj
    sorted_jobs = sorted(jobs, key=lambda x: nodes_topo.index(x[0]))
    # print(sorted_jobs)
    for i in range(1,len(sorted_jobs)):
        new_rj = max(sorted_jobs[i-1][1]+sorted_jobs[i-1][2],sorted_jobs[i][1])
        sorted_jobs[i][1] = new_rj
    # print(sorted_jobs)
    time = sorted_jobs[-1][1]+sorted_jobs[-1][2]
    print(time)

    