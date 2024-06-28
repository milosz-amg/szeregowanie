#1|prec|Cmax

N, E = map(int, input().split()) #liczba operacji i lcizba informacji
operations = [int(input()) for _ in range(N)] # czas wykonania kolejnych operacji
order = [tuple(map(int, input().split())) for _ in range(E)] # operacje k wykonac przed operacja l

time_taken = [0] * N #czas poswiec ony danej operacji, na poczatku wszystkie 0
graph = [[] for _ in range(N)] #graf zaleznosci, by wiedziec ktore operacje musimy przed dana operacja wykonac
total_time = 0 #zmienna do sumowania calego lacznego czasu skladania szafy

for k, l in order: #na podstawie zaleznosci, tworzymy graf
    graph[l - 1].append(k - 1) #odejmujemy 1 by miec indeksy od 0

print(graph)

while True:
    L = None
    for i in range(N): 
        #jesli time_taken[i] == 0 to znaczy ze jeszcze nie bylo wykonane
        #all(time_taken[j] for j in graph[i]) sprawdzamy czy wszystkie operacje wymagane wczesniej sa zrobione
        if time_taken[i] == 0 and all(time_taken[j] for j in graph[i]): 
            L = i #wiemy ze jest gotowe, przypisujemy do L
            break
    if L is None:
        break
    total_time += operations[L] #dodajemy czas wykonania danej operacji do lacznego czasu
    time_taken[L] = total_time #aktualizujemy
    print(L + 1) #powiekszamy o 1 bo zmniejszalismy w 12 lini 1