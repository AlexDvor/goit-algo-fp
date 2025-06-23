import random
import matplotlib.pyplot as plt


def monte_carlo_dice_simulation(num_trials=100000):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        results[total] += 1

    # Розрахунок ймовірностей
    probabilities = {key: (value / num_trials) * 100 for key, value in results.items()}
    return probabilities, results


def plot_probabilities(probabilities, title):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.figure(figsize=(10, 6))
    bars = plt.bar(sums, probs, color="skyblue", edgecolor="black")

    for bar, p in zip(bars, probs):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{p:.2f}%",
            ha="center",
            va="bottom",
        )

    plt.xticks(sums)
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Імовірність (%)")
    plt.title(title)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


def analytical_probabilities():
    total_outcomes = 36
    occurrences = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
    return {k: (v / total_outcomes) * 100 for k, v in occurrences.items()}


# Симуляція
simulated_probs, counts = monte_carlo_dice_simulation(100000)

# Аналітичні
theoretical_probs = analytical_probabilities()

# Виведення
print("Сума | Монте-Карло (%) | Теоретично (%)")
for i in range(2, 13):
    print(f"{i:>4} | {simulated_probs[i]:>14.2f} | {theoretical_probs[i]:>14.2f}")

# Графіки
plot_probabilities(simulated_probs, "Ймовірності (Монте-Карло)")
plot_probabilities(theoretical_probs, "Ймовірності (Теоретичні)")
