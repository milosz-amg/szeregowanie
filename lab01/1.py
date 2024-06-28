# 1||Cmax
def liczba_minut_na_sprawdzenie(n, prace):
    suma_stron = sum(prace)
    liczba_minut = suma_stron
    return liczba_minut

if __name__ == "__main__":
    n = int(input())
    prace = list(map(int, input().split()))
    liczba_minut = liczba_minut_na_sprawdzenie(n, prace)

    print(liczba_minut)
