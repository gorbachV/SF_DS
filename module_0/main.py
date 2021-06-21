import numpy as np


def game_core_v2(number, max_number=100):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, max_number + 1)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number, max_number=100):
    """Делим диапазон загаданых числе пополам, если не угадали, то мы знаем число было болшьше
    или меньше, а значит угадываем в оставшейся половине. Оставшуюся половину снова делим пополам,
    отгадываем - не угадали? Берем половину от оставшейся половины и снова угадываем... Пока не угадаем"""
    count = 1
    left = 1  # левая граница диапазона
    right = max_number  # правая граница диапазона
    predict = int((right + left) / 2)  # берем середину диапазона
    while number != predict:
        count += 1
        if number > predict:
            left = predict + 1  # сдвигаем левую границу
        elif number < predict:
            right = predict - 1  # сдвигаем правую границу
        predict = int((right + left) / 2)
    return count  # выход из цикла, если угадали


def ceil_number(number):
    """Округляем в большую сторону"""
    if number != 1 and number % 2 > 0:
        return int(number) + 1
    else:
        return int(number)


def score_game(game_core, max_number=100):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, max_number + 1, size=1000)
    for number in random_array:
        count_ls.append(game_core(number, max_number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# Проверяем
score_game(game_core_v3, 100)

