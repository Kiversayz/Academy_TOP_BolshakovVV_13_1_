import threading
import random
import math
import time

#Поток #1
def generate_numbers(filename):
    """Заполняем файл случайными числами."""
    try:
        with open(filename, 'w') as f:  # Открываем файл на запись
            for _ in range(100):  # Генерируем 100 случайных чисел
                num = random.randint(1, 100)  # Генерируем случайное число от 1 до 100
                f.write(str(num) + '\n')  # Записываем число в файл
        print("Файл успешно заполнен случайными числами.")
    except Exception as e:
        print(f"Ошибка при заполнении файла: {e}")

#Поток №2
def is_prime(num):
    """Проверка, является ли число простым."""
    if num <= 1:
        return False  # Числа меньше или равные 1 не простые
    for i in range(2, int(math.sqrt(num)) + 1):  # Проверяем до квадратного корня числа
        if num % i == 0:
            return False  # Если делится, то не простое
    return True  # Если не делится ни на одно число, то простое

def find_primes(filename, result_filename):
    """Находим простые числа в файле и записываем в новый файл."""
    try:
        with open(filename, 'r') as f:  # Открываем файл для чтения
            numbers = f.readlines()  # Читаем все строки файла

        primes = []  # Список для хранения простых чисел
        for line in numbers:
            num = int(line.strip())  # Убираем лишние пробелы и конвертируем строку в число
            if is_prime(num):
                primes.append(num)  # Если число простое, добавляем его в список простых чисел

        # Записываем простые числа в новый файл
        with open(result_filename, 'w') as f:
            for prime in primes:
                f.write(str(prime) + '\n')

        print("Результаты поиска простых чисел записаны в файл.")
    except Exception as e:
        print(f"Ошибка при поиске простых чисел: {e}")

#Поток №3
def calculate_factorials(filename, result_filename):
    """Вычисляем факториал для каждого числа в файле и записываем в новый файл."""
    try:
        with open(filename, 'r') as f:
            numbers = f.readlines()  # Читаем все строки файла

        factorials = []  # Список для хранения факториалов
        for line in numbers:
            num = int(line.strip())  # Убираем лишние пробелы и конвертируем строку в число
            factorial = math.factorial(num)  # Вычисляем факториал
            factorials.append(factorial)

        # Записываем факториалы в новый файл
        with open(result_filename, 'w') as f:
            for fact in factorials:
                f.write(str(fact) + '\n')

        print("Результаты вычислений факториалов записаны в файл.")
    except Exception as e:
        print(f"Ошибка при вычислении факториалов: {e}")

# Проверочный код
def main():
    file_path = input("Введите путь к файлу: ")

    start_time_1 = time.time()

    # Поток для генерации чисел
    generate_thread = threading.Thread(target=generate_numbers, args=(file_path,))
    generate_thread.start()
    generate_thread.join()
    
    end_time_1 = time.time()

    # Потоки для поиска простых чисел и вычисления факториалов
    prime_thread = threading.Thread(target=find_primes, args=(file_path, rf'number_1\primes.txt'))
    factorial_thread = threading.Thread(target=calculate_factorials, args=(file_path, fr'number_1\factorials.txt'))

    
    start_time_2 = time.time()
    prime_thread.start()
    
    start_time_3 = time.time()
    factorial_thread.start()

    prime_thread.join()
    end_time_2 = time.time()
    
    factorial_thread.join()
    end_time_3 = time.time()

    print(
        f"Время потока 1: {round(end_time_1 - start_time_1,5)} секунд.\n"
        f"Время потока 2: {round(end_time_2 - start_time_2,5)} секунд.\n"
        f"Время потока 3: {round(end_time_3 - start_time_3,5)} секунд.\n"
          )

if __name__ == "__main__":
    main()