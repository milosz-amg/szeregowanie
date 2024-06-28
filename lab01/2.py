# 1||wj Cj
if __name__ == "__main__":
    N = int(input())
    orders = []

    for i in range(N):
        C, K = map(int, input().split())
        orders.append([C,K, C/K])

orders = sorted(orders, key=lambda x:x[2])

days_of_delay=0
min_sum=0

for i in range(N):
    days_of_delay += orders[i][0]
    min_sum += orders[i][1] * days_of_delay

print(min_sum)