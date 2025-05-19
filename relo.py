import numpy as np

def regular_polygon_Relo(n: int = 3, center: np.ndarray = np.array([0, 0]), r: float = 1, N: int = 100) -> np.ndarray:
    """
    Генерирует координаты точек, описывающих границу правильного многоугольника Рело.

    :param n: Количество вершин (нечетное целое число > 2), по умолчанию 3
    :param center: Координаты центра (массив numpy), по умолчанию np.array([0, 0])
    :param r: Ширина многоугольника (положительное число), по умолчанию 1
    :param N: Количество точек для одной стороны (натуральное число), по умолчанию 100
    :return: Матрица (numpy ndarray), где каждая строка содержит координаты точек границы
    """
    if center is None:
        center = np.array([0.0, 0.0])
    else:
        center = np.array(center, dtype=float)

    assert isinstance(n, int) and n > 2 and (n % 2 == 1), "n must be an odd integer greater than 2"
    assert center.shape == (2,), "center must be a 2-element array representing (x, y)"
    assert isinstance(r, (int, float)) and r > 0, "r must be a positive number"
    assert isinstance(N, int) and N > 0, "N must be a positive integer"
    
    l: float = 2 * r * np.sin(np.pi / (2 * n))
    R: float = l / (2 * np.sin(np.pi / n))
    angles: np.ndarray = np.arange(0, 2 * np.pi, 2 * np.pi / n)
    vertices: np.ndarray = center + R * np.column_stack((np.cos(angles), np.sin(angles)))
    
    alpha: float = 2 * np.pi / n   
    beta: float = alpha / 2        
    arc_angles: np.ndarray = np.linspace(-beta / 2, beta / 2, N)

    sides_list = [
        vertices[i] + r * np.column_stack((
            np.cos(arc_angles + np.pi + i * alpha),
            np.sin(arc_angles + np.pi + i * alpha)
        ))
        for i in range(n)
    ]
    sides: np.ndarray = np.concatenate(sides_list, axis=0)
    
    return sides

if __name__ == "__main__":
    polygon = regular_polygon_Relo(7, np.array([0, 0]), 10, 100)

    plt.figure(figsize=(6, 6))
    plt.plot(polygon[:, 0], polygon[:, 1], 'b-', lw=2, label='Граница многоугольника Рело')
    plt.axis('equal')
    plt.title("Многоугольник Рело для n = 7")
    plt.legend()
    plt.show()

    print("Type annotations:")
    print(regular_polygon_Relo.__annotations__)
    
    print("\nFunction docstring:")
    print(regular_polygon_Relo.__doc__)