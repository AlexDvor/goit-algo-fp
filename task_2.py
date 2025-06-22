import matplotlib.pyplot as plt
import numpy as np


def draw_tree(x, y, length, angle, depth, ax):
    if depth == 0:
        return

    # Обчислення координат наступної точки
    x2 = x + length * np.cos(angle)
    y2 = y + length * np.sin(angle)

    # Малювання лінії
    ax.plot([x, x2], [y, y2], color="brown")

    # Кут повороту гілок
    angle_left = angle + np.pi / 4
    angle_right = angle - np.pi / 4

    # Скорочення довжини гілок
    new_length = length * 0.7

    # Рекурсивний виклик для гілок
    draw_tree(x2, y2, new_length, angle_left, depth - 1, ax)
    draw_tree(x2, y2, new_length, angle_right, depth - 1, ax)


def create_pythagoras_tree(depth):
    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis("off")

    # Початкові координати та параметри
    draw_tree(x=0, y=0, length=1, angle=np.pi / 2, depth=depth, ax=ax)

    plt.title(f"Дерево Піфагора (глибина рекурсії = {depth})", fontsize=12)
    plt.show()


create_pythagoras_tree(depth=7)
