def mcnaughton_algorithm(M, reports):
    # Oblicz sumę czasów wszystkich raportów oraz maksimum z czasów
    total_time = sum(reports)
    max_time = max(reports)
    
    # Oblicz czas maksymalny dla maszyny
    C_max = max(total_time / M, max_time)
    
    # Inicjalizuj listę zadań dla każdego urzędnika
    employee_reports = [[] for _ in range(M)]
    
    t = 0
    i = 0
    
    # Przypisz zadania do urzędników zgodnie z algorytmem McNaughtona
    for j, pj in enumerate(reports, start=1):
        if t + pj <= C_max:
            employee_reports[i].append((j, t, t + pj))
            t += pj
        else:
            employee_reports[i].append((j, t, C_max))
            t = pj - (C_max - t)
            i = (i + 1) % M
            employee_reports[i].append((j, 0, pj - (C_max - t)))
            t = pj - (C_max - t)
            i += 1
    
    return C_max, employee_reports

# Wczytaj liczbę urzędników i liczbę raportów
M, N = map(int, input().split())

# Wczytaj czasy trwania raportów
reports = [int(input()) for _ in range(N)]

# Oblicz czas maksymalny i plan pracy dla każdego urzędnika
C_max, employee_reports = mcnaughton_algorithm(M, reports)

# Wydrukuj wynik
print(C_max)  # Czas maksymalny, po którym wszyscy urzędnicy zakończą pracę
for i, reports in enumerate(employee_reports, start=1):
    print(f"{i}:", " ".join(f"{report[0]}[{report[1]},{report[2]}]" for report in reports))
