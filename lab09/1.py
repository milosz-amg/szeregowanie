# O2||Cmax
# tylko wzoru na Cmax uzyc

if __name__ == "__main__":
    n = int(input())
    pj = []
    pw = []
    maxpair = 0

    for i in range(n):
        j, w = map(int, input().split())
        pj.append(j)
        pw.append(w)
        if j + w > maxpair:
            maxpair = j + w

    # for i in range(n):
    #     if pj[i]+pw[j]>maxpair:
    #         maxpair=pj[i]+pw[j]

    Cmax = max(sum(pj),sum(pw),maxpair)
    print(Cmax)