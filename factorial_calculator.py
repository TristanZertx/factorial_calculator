import math

def calculate_factorial(n):
    """Вычисляет факториал числа с использованием math.factorial"""
    return math.factorial(n)

def main():
    print("Программа вычисления факториала числа")
    
    try:
        # Запрос ввода и преобразование в целое число
        user_input = input("Введите положительное целое число: ")
        number = int(user_input)
        
        # Проверка на отрицательное значение
        if number < 0:
            raise ValueError("Число не может быть отрицательным")
        
        # Вычисление факториала
        result = calculate_factorial(number)
        print(f"Факториал числа {number} равен: {result}")
    
    except ValueError as e:
        # Обработка нечислового ввода и отрицательных чисел
        print(f"Ошибка: {str(e) or 'Введено нечисловое значение или нецелое число'}")

if __name__ == "__main__":
    main()