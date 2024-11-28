def prrsonal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:

        for j in i:

            try:
                result += j
            except TypeError:
                incorrect_data += 1
                print(f'некорректный тип данных для подсчета суммм - {j}')
    return result, incorrect_data

def calculate_avarage(*numbers):
    if isinstance(*numbers, int):
        return None
    try:
        tuple_pers_sum = personal_sum(*numbers)

        return tuple_pers_sum[0] / (len(*numbers) - tuple_pers_sum[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return f'В numbers записан некорректный тип данных'

print(f'результат 1: {calculate_avarage("1, 2, 3")}')
print(f'результат 2: {calculate_avarage([1, "строка", 3, "Еще строка"])}')
print(f'результат 3: {calculate_avarage(567)}')
print(f'результат 4: {calculate_avarage(42, 15, 36, 13])}')
