N = int(input())  # liczba studentow przyslajaca zadania
zadanka = []
for _ in range(N):
    C, D = map(int, input().split())  # czas kiedy praca zostala przyslana i jej dlugosc
    zadanka.append((C, D)) 

print(zadanka)
zadania_z_kolejnoscia = [(i, zadanie) for i, zadanie in enumerate(zadanka)] #tworzymy sobie pary indeks i krotka
zadania_z_kolejnoscia.sort(key=lambda x: x[1][0]) #sortujemy zadania po gotowosci do wykonania
print(zadania_z_kolejnoscia)
laczny_czas = 0
wyniki = [0] * N

for i, (C, D) in zadania_z_kolejnoscia: #przechodze przez posortowana liste
    laczny_czas = max(laczny_czas, C) #biore max z aktualnego lacznego czasu i czasu gotowosci aktualnego zadania
    laczny_czas += D #laczny czas aktualizuje o dlugosc trwania aktualnego zadania
    wyniki[i] = laczny_czas #zapisuje kiedy sie zakonczylo aktualnie przetwarzane zadanie

for time in wyniki: #wypisujemy kazdy z wynikow
    print(time)

print(laczny_czas) #wypsiujemy laczny czas profesora