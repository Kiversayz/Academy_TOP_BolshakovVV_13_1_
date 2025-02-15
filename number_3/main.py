import threading
import time

lock = threading.Lock()

def input_data():
    """Запрос чисел у пользователя и сохранение их в список."""
    numbers = input("Введите числа через пробел: ")
    numbers = list(map(int, numbers.split()))  # Преобразуем строку в список чисел
    return numbers

def find_sum(numbers):
    """Находит сумму элементов списка 5 раз с синхронизацией вывода."""
    for _ in range(5):
        total_sum = sum(numbers)
        with lock:
            print(f"Сумма элементов: {total_sum}")
        time.sleep(1)

def find_average(numbers):
    """Находит среднее арифметическое списка 5 раз с синхронизацией вывода."""
    for _ in range(5):
        average = sum(numbers) / len(numbers) if numbers else 0  # Защита от деления на 0
        with lock:
            print(f"Среднее арифметическое: {average}")
        time.sleep(1)

def main():
    numbers = input_data()  # Получаем данные от пользователя

    # Создаем потоки для нахождения суммы и среднего арифметического
    sum_thread = threading.Thread(target=find_sum, args=(numbers,))
    average_thread = threading.Thread(target=find_average, args=(numbers,))

    # Запускаем потоки
    sum_thread.start()
    average_thread.start()

    # Ожидаем завершения потоков
    sum_thread.join()
    average_thread.join()

if __name__ == "__main__":
    main()



