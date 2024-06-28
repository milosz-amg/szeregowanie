# 1 | prec | fmax   -   algorytm Lawlera
#   1) liczymy ile czasu zajmie wykonanie wszystkich zadan
#   2) szeregujemy od końca, wybierając te które wygeneruje najniejszy czas
#   3) usuwamy je z grafu
#   4) ponownie obliczamy najmniejszy koszt zadania
# alg khana po odwrócownych krawędziach

from cmath import inf


def calculate_cost(node,jobs,t):
    return jobs[node][1][1]*(t**2)+jobs[node][1][2]*t+jobs[node][1][3]

if __name__ == "__main__":
    n = int(input())
    jobs = []
    nodes = []
    for i in range(n):
        processing_t, a, b, c = map(int, input().split())
        jobs.append([i,(processing_t,a,b,c)])
        nodes.append(i)
    # print(jobs)
    # print(nodes)
    e =int(input())
    job_order=[]
    for i in range(e):
        job_before, current_job = map(int, input().split())
        job_order.append((job_before-1,current_job-1))
    # print(job_order)

    nodes_topo=[]
    nodes_without_suc=nodes.copy()
    node_with_suc=int

    time_sum = sum([job[1][0] for job in jobs])
    # print(time_sum)
    max_cost=-1

    while nodes_without_suc:    #analogicznie jak poprzednio sortujemy
        for i in range(len(job_order)):
            node_with_suc = int(job_order[i][0])
            if node_with_suc in nodes_without_suc:      #ale odwracamy kolejność poprzedniki <-> następniki
                nodes_without_suc.remove(node_with_suc)
        min_cost = float(inf)     #musi byc mniejsze od tej liczby
        min_node = int
        cost = 0
        for node in nodes_without_suc:
            cost =  calculate_cost(node,jobs,time_sum)  #oblicz koszt zadania
            if min_cost > cost:
                min_cost = cost
                min_node = jobs[node][0]
        nodes_topo.append(min_node)
        job_order = [j for j in job_order if j[1] != min_node] #wyrzuć porzucony węzeł
        nodes_without_suc.remove(min_node)
        nodes_without_suc = [n for n in nodes if n not in nodes_topo]
        time_sum -= jobs[min_node][1][0]
        if min_cost > max_cost:
            max_cost = min_cost
        
    print(max_cost)