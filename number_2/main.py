import threading
import random
import math
import time

lock = threading.Lock()

def input_data():
    """Запрос чисел у пользователя и сохранение их в список."""
    numbers = input("Введите числа через пробел: ")
    numbers = list(map(int, numbers.split()))  # Преобразуем строку в список чисел
    return numbers


#Поток #1
def find_max(numbers):
    """Находит максимум в списке 5 раз."""
    numbers_print = []
    step = 1
    for _ in range(5):
        max_value = max(numbers)
        with lock:
            print(f"{step}. Максимум: {max_value}")
        step+=1
        time.sleep(1)  # Задержка между выводами для имитации работы потока

#Поток #2
def find_min(numbers):
    """Находит минимум в списке 5 раз."""
    numbers_print = []
    step = 1
    for _ in range(5):
        min_value = min(numbers)
        with lock:
            print(f"{step}. Минимум: {min_value}")
        step+=1
        time.sleep(1)  # Задержка между выводами для имитации работы потока

def main():
    numbers = input_data()  # Получаем данные от пользователя

    # Создаем потоки для поиска максимума и минимума
    max_thread = threading.Thread(target=find_max, args=(numbers,))
    min_thread = threading.Thread(target=find_min, args=(numbers,))

    # Запускаем потоки
    max_thread.start()
    min_thread.start()

    # Ожидаем завершения потоков
    max_thread.join()
    min_thread.join()

if __name__ == "__main__":
    main()
