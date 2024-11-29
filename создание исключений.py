class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        print(self.message)

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin) and self.__is_valid_numbers(numbers):
            self.__vin = vin
            self.__numbers = numbers
            print(f'{self.model} успешно создан')
        else:
            pass
    def __is_valid_vin(self, vin_number):
        try:
            if isinstance(vin_number, float):
                raise IncorrectVinNumber('Некорректный тип vin номер')
            if not 1000000 <= vin_number <= 9999999:
                raise  IncorrectVinNumber('Неверный диапозон для vin номера')
        except IncorrectVinNumber:
            pass
        else:
            return True

    def __is_valid_numbers(self, numbers):
        try:
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Неверная длина номера')
        except IncorrectCarNumbers:
            pass
        else:
            return True

car1 = Car('Modul 1', 1000000, 'f123dj')
car2 = Car('Modul 2', 300, 'т001тр')
car3 = Car('Modul 3', 2020202, 'нет номера')


