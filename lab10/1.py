if __name__ == "__main__":
    n = int(input())
    A=[]
    B=[]

    for i in range(n):
        cutting_t, added_t, decorating_t = map(int, input().split())
 
        if cutting_t + added_t <= decorating_t + added_t:
            A.append([cutting_t, added_t, decorating_t])
        else:
            B.append([cutting_t, added_t, decorating_t])
 
    A.sort(key=lambda x: x[0] + x[1])
    B.sort(key=lambda x: x[2] + x[1], reverse=True)
    
    tasks = A + B
    machine_1 = 0
    machine_2 = 0
    machine_3 = 0
    
    for task in tasks:
        machine_1 += task[0]
        if machine_1 > machine_2:
            machine_2 = machine_1
        machine_2 += task[1]
        if machine_2 > machine_3:
            machine_3 = machine_2
        machine_3 += task[2]

    print(machine_3)