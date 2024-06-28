def process_orders(orders):
    orders.sort(key=lambda x: x[0])

    current_time = min(order[0] for order in orders)
    total_penalty = 0

    while orders:
        available_orders = [order for order in orders if order[0] <= current_time]
        if not available_orders:
            current_time = min(order[0] for order in orders)
            continue

        next_time_candidates = [order[0] for order in orders if order[0] > current_time]
        if next_time_candidates:
            next_time = min(next_time_candidates)
        else:
            break

        selected_order = min(available_orders, key=lambda x: x[2])

        l = min(selected_order[1], next_time - current_time)

        total_penalty += max(0, current_time + l - selected_order[2])

        if selected_order[1] <= l:
            orders.remove(selected_order)
        else:
            orders.remove(selected_order)
            orders.append((current_time + l, selected_order[1] - l, selected_order[2]))

        current_time += l

    return total_penalty

N = int(input())
orders = []

for _ in range(N):
    R, P, D = map(int, input().split())
    orders.append((R, P, D))
    
total_penalty = process_orders(orders)
print(total_penalty)