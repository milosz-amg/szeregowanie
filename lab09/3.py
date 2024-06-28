# flowshop z podanym uszeregowaniem
# F||-
# policzyc jak wyglada uszeregowanie dla danej kolejnosci zadan - uszeregowanie permutacjami
# programowanie dynamiczne
# DP - uszeregowanie z permutacji


if __name__ == "__main__":
    m, n = map(int, input().split())

    times=[]
    for i in range(n):
        times.append(list(map(int, input().split())))
    

    # for time in times:
        # print(time)

    C_matrix = [["-" for j in range(n+1)] for i in range(m+1)]

    # for row in C_matrix:
        # print(row)

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                C_matrix[i][j]=0
            else:
                C_matrix[i][j]=max(C_matrix[i-1][j], C_matrix[i][j-1])+times[i-1][j-1]

    end_times = C_matrix[-1][-m:]
    for end in C_matrix[-1][-m:]:
        print(end)