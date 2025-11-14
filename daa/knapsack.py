def fractional_knapsack(w, v, cap):
    items = sorted([(v[i] / w[i], w[i], v[i]) for i in range(len(w))], reverse=True)

    total = 0
    for ratio, weight, value in items:
        if cap >= weight:
            cap -= weight
            total += value
        else:
            total += ratio * cap
            break
    return total


# Driver
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum Value:", fractional_knapsack(weights, values, capacity))
