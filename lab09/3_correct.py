# flowshop z podanym uszeregowaniem
# F||-
# policzyc jak wyglada uszeregowanie dla danej kolejnosci zadan - uszeregowanie permutacjami
# programowanie dynamiczne
# DP - uszeregowanie z permutacji


if __name__ == "__main__":
    m, n = map(int, input().split())

    machines = [0] * m
    end_times=[]
    for _ in range(n):
        times = list(map(int, input().split()))
        
        for i in range(m):
            if i == 0:
                machines[i] += times[i]
            else:
                if machines[i] < machines[i-1]:
                    machines[i] = machines[i-1]
                    
                machines[i] += times[i]
        end_times.append(machines[-1])
        
    for elem in end_times:
        print(elem)