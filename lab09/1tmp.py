if __name__ == "__main__":
    n = int(input())
    jobs = []
    for i in range(n):
        j, w = map(int, input().split())
        jobs.append((j, w, i+1))
    
    A = []
    B = []
    
    for job in jobs:
        if job[0] <= job[1]:
            A.append(job)
        else:
            B.append(job)

    # Sortowanie A rosnąco po pierwszym elemencie
    A.sort(key=lambda x: x[0])
    
    # Sortowanie B malejąco po drugim elemencie
    B.sort(key=lambda x: x[1], reverse=True)
    
    print("Zadania do wycinania (A):")
    print(A)  # Wypisanie zadań do wycinania
    print("Zadania do wiercenia (B):")
    print(B)  # Wypisanie zadań do wiercenia
    
    # Łączenie zadań
    A = A + B
    print("Kolejność wykonywania zadań (A + B):")
    print(A)
    
    time_a = 0
    time_b = 0

    print("Numer zadania | Koniec przetwarzania A | Koniec przetwarzania B")
    for job in A:
        # Jeśli czas zakończenia przetwarzania w A jest mniejszy lub równy czasowi zakończenia przetwarzania w B
        # To zadanie B nie może być wykonane przed zakończeniem przetwarzania zadania A
        end_a = time_a + job[0]
        end_b = max(time_b, end_a) + job[1]  # B nie może zacząć się, dopóki A nie zakończy się

        print(f"{job[2]} | {end_a} | {end_b}")

        time_a = end_a
        time_b = end_b
