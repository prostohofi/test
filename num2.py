def bubble_sort(arr):
    n = len(arr)
    comparisons = 0

    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1  # Увеличиваем счетчик сравнений
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Если внутренний цикл не произвел обмен, значит массив отсортирован
        if not swapped:
            break

    return arr, comparisons

# Пример использования
arr = [64, 34, 25, 12, 22, 11, 90, 33, 76, 3]
sorted_arr, comparisons = bubble_sort(arr)

print("Отсортированный массив в порядке убывания:", sorted_arr)
print("Количество сравнений:", comparisons)