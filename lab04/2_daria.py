N = int(input())
orders = []
for _ in range(N):
    P, D = map(int, input().split())
    orders.append((P, D))
orders.sort(key=lambda x: x[1])
#print(orders) 
t = 0
S = []
for order in orders:
    P, D = order
    t += P
    S.append(P)
    if t > D:
        max_element = max(S)
 
        S.remove(max_element)
        t -= max_element
print(len(S))