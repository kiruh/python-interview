def knapsack(capacity, weights, values, n):
    if n == 0 or capacity == 0:
        return 0
    weight = weights[n-1]
    value = values[n-1]
    if weight > capacity:
        return knapsack(capacity, weights, values, n-1)
    else:
        return max(
            value + knapsack(capacity-weight, weights, values, n-1),
            knapsack(capacity, weights, values, n-1)
        )


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)
print(knapsack(capacity, weights, values, n))
