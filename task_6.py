def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )

    total_calories = 0
    chosen = []

    for name, info in sorted_items:
        if info["cost"] <= budget:
            budget -= info["cost"]
            total_calories += info["calories"]
            chosen.append(name)

    return total_calories, chosen


def dynamic_programming(items, budget):
    item_list = list(items.items())
    n = len(item_list)

    # dp[i][b] = максимальні калорії при використанні перших i предметів з бюджетом b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, info = item_list[i - 1]
        cost = info["cost"]
        calories = info["calories"]
        for b in range(budget + 1):
            if cost > b:
                dp[i][b] = dp[i - 1][b]
            else:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)

    b = budget
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name, info = item_list[i - 1]
            chosen.append(name)
            b -= info["cost"]

    return dp[n][budget], chosen[::-1]


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 70

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("\n👉 Greedy Algorithm:")
print(f"Calories: {greedy_result[0]}, Items: {greedy_result[1]}")

print("\n👉 Dynamic Programming:")
print(f"Calories: {dp_result[0]}, Items: {dp_result[1]}")
